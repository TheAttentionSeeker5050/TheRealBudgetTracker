from rest_framework import serializers, permissions
from .models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', "username", 'entry_type', 'description', 'category', "date", "amount")