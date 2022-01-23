# view related imports
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# import the models
from entries.models import Entry

# import the forms
from .forms import EntryForm

# Create your views here.

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

def entry_log_view(request):

    all_entries = Entry.objects.all()

    # we render the site
    return render(request, "entries/entries_log.html", {"entries": all_entries})

def summary_view(request):

    all_income = Entry.objects.all().filter(entry_type="income")
    all_expense = Entry.objects.all().filter(entry_type="expense")

    total_income=0
    total_expense=0

    for entry in all_income:
        total_income = entry.amount + total_income
    
    for entry in all_expense:
        total_expense = entry.amount + total_expense

    print(total_expense)
    print(total_income)



    balance = total_income - total_expense
        

    return render(request, "entries/summary.html", {"income":total_income, "expense":total_expense, "balance":balance})

from django.views.generic.edit import UpdateView

class EntryEditView(UpdateView):
    template_name = 'entries/edit.html'
    model = Entry
    fields = ['entry_type', "description", "category", "date", "amount"]
    success_url = "/entries"
    
