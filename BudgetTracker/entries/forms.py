from django import forms

# here put all the forms in this app

ENTRY_TYPE_CHOICES = [
    ("Income","Income"),
    ("Expense","Expense")
]

CATEGORY_CHOICES = [
    # expense categories
    ("Food","Food"),
    ("Housing","Housing"), 
    ("Transportation","Transportation"),
    ("Fun & Entertainment","Fun & Entertainment"),
    ("Investing","Investing"),
    ("Interest & Debts","Interest & Debts"),
    # income categories
    ("Allowance","Allowance"),
    ("Work","Work"),
    ("Investment Returns","Investment Returns")
]

class EntryForm(forms.Form):
    """This is the new entry form"""
    entry_type = forms.ChoiceField(
        required=True,
        widget=forms.Select,
        choices=ENTRY_TYPE_CHOICES,
        label="Type"
    )
    description = forms.CharField(max_length=120,label="Description")
    category = forms.ChoiceField(
        required=True,
        widget=forms.Select,
        choices=CATEGORY_CHOICES,
        label="Category"
    )
    date = forms.DateField(
        widget=forms.DateInput(format=('%d-%m-%Y'), 
                               attrs={"type":"date"}))
    amount = forms.DecimalField(decimal_places=2)