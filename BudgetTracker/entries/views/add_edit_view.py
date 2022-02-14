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
from django.contrib.auth.mixins import LoginRequiredMixin

# from users.views import LoginRequiredMixin





class CreateEntryView(LoginRequiredMixin , CreateView):
    login_url = "/login"
    redirect_field_name = "login"
    model = Entry
    fields = ['entry_type', "description", "category", "date", "amount"]
    template_name = 'entries/new.html'
    success_url = "/entries"
    
    
    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class EntryEditView(LoginRequiredMixin, UpdateView):
    """Edit an existing entry"""
    login_url = "/login"
    redirect_field_name = "login"
    
    template_name = 'entries/edit.html'
    model = Entry
    fields = ['entry_type', "description", "category", "date", "amount"]
    success_url = "/entries"
    
