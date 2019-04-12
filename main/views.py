from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

# Functions View
def main(request):
    return render(request, 'index.html')

def user(request):
    return render(request, 'user.html')

def company(request):
    return render(request, 'company.html')

def transfer(request):
    return render(request, 'transfer.html')


#REST api end-poinst
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
