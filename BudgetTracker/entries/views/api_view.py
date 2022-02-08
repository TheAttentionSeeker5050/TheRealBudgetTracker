from rest_framework import viewsets, generics
from entries.serializers import EntrySerializer
from entries.models import Entry

from django.shortcuts import render

# Create your views here.

class EntryApiView(generics.ListCreateAPIView):
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()