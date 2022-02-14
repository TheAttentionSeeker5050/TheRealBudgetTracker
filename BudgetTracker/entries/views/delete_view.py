# view related imports
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# import the models
from entries.models import Entry

# import the forms
from entries.forms import EntryForm

# import time functions
from django.utils import timezone


# import delete class based view 
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

class EntryDeleteView(DeleteView):
    """Our delete entry view"""
    # define our model
    model = Entry

    # the template
    template_name = "entries/delete.html"
    context_object_name = 'deleteview'

    def get_success_url(self):
        # return a redirection
        return reverse_lazy('entries_log')