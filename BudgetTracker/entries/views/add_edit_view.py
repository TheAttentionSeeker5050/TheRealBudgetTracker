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

from django.views.generic.edit import CreateView, UpdateView



class CreateEntryView(CreateView):
    model = Entry
    fields = ['entry_type', "description", "category", "date", "amount"]
    template_name = 'entries/new.html'
    success_url = "/entries"


class EntryEditView(UpdateView):
    """Edit an existing entry"""
    template_name = 'entries/edit.html'
    model = Entry
    fields = ['entry_type', "description", "category", "date", "amount"]
    success_url = "/entries"
