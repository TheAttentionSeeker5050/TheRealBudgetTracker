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



def new_entry_view(request):
    """This is the default new entry view"""

    # if it is a post we need to request the input data
    if request.method == "POST":
        # create a post instance and populate it with the data from the request
        form = EntryForm(request.POST)

        if form.is_valid():
            # Processs the date in the form and return cleaned data
            entry_type = form.cleaned_data["entry_type"]
            description = form.cleaned_data["description"]
            category = form.cleaned_data["category"]
            date = form.cleaned_data["date"]
            amount = form.cleaned_data["amount"]

            # we save the cleaned data
            q = Entry(entry_type=entry_type, description=description, category=category, date=date, amount=amount)
            q.save()
            return redirect("entries_log")

    # or if a get well create a blank form
    else:
        form = EntryForm()
        


    return render(request, "entries/new.html", {"form":form})


from django.views.generic.edit import UpdateView

class EntryEditView(UpdateView):
    """Edit an existing entry"""
    template_name = 'entries/edit.html'
    model = Entry
    fields = ['entry_type', "description", "category", "date", "amount"]
    success_url = "/entries"
