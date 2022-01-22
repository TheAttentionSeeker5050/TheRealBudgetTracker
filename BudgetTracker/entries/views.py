from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from entries.models import Entry

def new_entry_view(request):
    return render(request, "entries/new.html", {})

