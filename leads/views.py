from django.shortcuts import render
from leads.models import Lead 
from rest_framework import viewsets, permissions
from .serializers import LeadSerializers


# Create your views here.

# Lead View 

class LeadViewSet (viewsets.ModelViewSet): 
    queryset = Lead.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializers

