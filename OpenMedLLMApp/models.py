from django.db import models

# Create your models here.
class User(models.Model):
    """A User enters a QUERY to the LLM, the LLM produces a RESPONSE, and we store also the DATE"""
    query = models.TextField()
    response = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a  string representation of the model """
        return self.query + " " + self.response


class Entry(models.Model):
    """A User enters a QUERY to the LLM, the LLM produces a RESPONSE, and we store also the DATE"""
    query = models.TextField()
    response = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a  string representation of the model """
        return self.query + " " + self.response

