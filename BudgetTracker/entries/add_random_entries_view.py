import sqlite3
from entries.models import Entry

for entry in entries_array:
    entry_var = Entry.objects.create(entry_type=entry["entry_type"], description=entry["description"], category=entry["category"], date=entry["date"], amount=entry["amount"])
    entry_var.save()


# for erasing all data 
Entry.objects.all().delete()