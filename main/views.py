from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from .serializers import *
from .models import User, Company, Transfer


# Functions View
def main(request):
    return render(request, 'index.html')


def user(request):
    return render(request, 'user.html', context={"companies": Company.objects.all()})


def company(request):
    return render(request, 'company.html')


def transfer(request):
    return render(request, 'transfer.html')


def abusers(request):
    return render(request, 'abusers.html')


class UserViewSet(viewsets.ModelViewSet,APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.data)
        User.objects.get(id=serializer['id']).update(**serializer)
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_200_OK)


class CompanyViewSet(viewsets.ModelViewSet, APIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # def update(self, request, pk=None):
    #     pass


class TransferViewSet(viewsets.ModelViewSet, APIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

    def post(self, request):
        print(request.data)
        return Response(status=status.HTTP_200_OK)


class AbusersViewSet(viewsets.ModelViewSet, APIView):
    queryset = Company.objects.all()
    serializer_class = AbuserSerializer
