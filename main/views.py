import json

from django.db.models import Sum
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.utils import DataGenerator
from .models import User, Company, Transfer
from .serializers import *


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


def report(request):
    result = []
    report_date = request.GET.get('month', '')
    for company in Company.objects.all():
        users_traffic = Transfer.objects.filter(
                                                user__company=company,
                                                date__month=report_date,).aggregate(sum=Sum('traffic'))
        if users_traffic['sum'] and users_traffic['sum'] > company.quote:
            result.append({
                'name': company.name,
                'traffic': users_traffic['sum'],
                'quote': company.quote
            })
    return HttpResponse(json.dumps({'data': result, 'count': len(result)}))


def generate(request):
    DataGenerator().process()
    return HttpResponse(json.dumps({'status': True}))


class UserViewSet(viewsets.ModelViewSet, APIView):
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


class TransferViewSet(viewsets.ModelViewSet, APIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

