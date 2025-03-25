from transformers import AutoTokenizer
import transformers
import torch
from transformers import pipeline

from django.db.models.sql import Query
from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
#from openai import OpenAI
from django.conf import settings

from OpenMedLLMApp.models import Entry
from django.shortcuts import render,redirect
from .forms import EntryForm




# Create your views here.

#Hold ALL LLM Queries AND Responses
#Display Content of this list on Page StartUp

list = []

#Model Selection
pipe = pipeline("text-generation", model="skumar9/Llama-medx_v3.2")


def index(request):
    """The home page for Our App"""


    return render(request,'OpenMedLLMApp/index.html')

def entries(request):
    """Show All Entries"""
    #entries = Entry.objects.order_by('date')
    context = {'entries': list }
    return render(request, 'OpenMedLLMApp/entries.html',context)


def new_query(request):
    """Make a new query"""

    if request.method != 'POST':
        # No data submitted; Create a blank form.
        form = EntryForm()

    else:
        # POST data submitted; Process the data

        form = EntryForm(request.POST)

        #Get The QUERY String
        query = request.POST['query']

        #Send the QUERY String to An LLM for Generation
        #model="skumar9/Llama-medx_v3.2" ranked 6th on the Leader Board
        messages = [
            {"role": "user", "content": query},
        ]
        outputs = pipe(messages)
        print(outputs[0]["generated_text"])

        #Save LLM Generation in list
        list.append(outputs[0]["generated_text"])

        #Display list on Page StartUp

        if form.is_valid():
            form.save()
            return redirect('OpenMedLLMApp:entries')
    # Display a blank or invalid form
    context = {'form':form}
    return render(request, 'OpenMedLLMApp/new_query.html', context)