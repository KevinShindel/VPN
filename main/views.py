from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

# Functions View
def home(request):
    return render(request, 'index.html')

#REST api end-poinst
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class AbuseViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = AbuseSerializer
