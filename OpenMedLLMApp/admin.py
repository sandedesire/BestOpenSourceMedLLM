from django.contrib import admin

# Register your models here.
from .models import User, Entry

admin.site.register(User)
admin.site.register(Entry)

