from django.shortcuts import render
from .models import User, Company, Transfer
from rest_framework import viewsets
from django.contrib.auth.models import User as AdminUser, Group as AdminGroup
from .serializers import UserSerializer,GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = AdminUser.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = AdminGroup.objects.all()
    serializer_class = GroupSerializer


def home(request):
    return render(request, 'index.html')


def user(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'user.html', context)


def company(request):
    companies = Company.objects.all()
    context = {
        'companies': companies
    }
    return render(request, 'company.html', context)


def abusers(request):
    logs = Transfer.objects.all()
    context = {
        'logs': logs
    }
    return render(request, 'abusers.html', context)

