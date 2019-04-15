import datetime
import random

from django.db.models import Max
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User,Company,Transfer
from rest_framework import viewsets, status
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

    # Random user
    # max_id = User.objects.all().aggregate(max_id=Max('id'))['max_id']
    # pk = random.randint(1, max_id)
    # rand_user = User.objects.get(pk=pk)
    # print(rand_user)


# REST api end-points
class UserViewSet(APIView):

    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request):
        print(request.data)
        serializer = UserSerializer(request.data)
        User.objects.get(id=serializer['id']).update(**serializer)
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        serializer = UserSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_200_OK)




class CompanyViewSet(viewsets.ModelViewSet, APIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def update(self, request, pk=None):
        pass



class TransferViewSet(viewsets.ModelViewSet, APIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

    def post(self, request):
        print(request.data)
        return Response(status=status.HTTP_200_OK)

