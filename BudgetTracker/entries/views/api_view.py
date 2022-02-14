from django.shortcuts import render

# import from the rest framework
from rest_framework import viewsets, generics, permissions
from rest_framework.views import APIView

# import our model
from entries.models import Entry

# import serializers
from entries.serializers import EntrySerializer

# import mixins
from rest_framework import mixins


# Create your views here.

class EntryApiViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    # queryset = Entry.objects.all()
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self, username=None):
        user = self.request.user
        return Entry.objects.filter(username=user)
        
class EntryList(generics.ListCreateAPIView):
    
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Entry.objects.filter(username=user)

class EntryListByYear(generics.ListCreateAPIView):
    
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Entry.objects.filter(username=user, date__year=self.year, date__month=self.month)

    def dispatch(self, request, *args, **kwargs):
        """Here we get the values of the url tags """
        self.year = kwargs["year"]
        self.month = kwargs["month"]
        
        return super(EntryListByYear, self).dispatch(request, *args, **kwargs)