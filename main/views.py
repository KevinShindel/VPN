from django.db.models import Sum
from django.http.response import JsonResponse
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from rest_framework import viewsets
from rest_framework.views import APIView

from main.utils import DataGenerator
from .serializers import *


class MainView(TemplateView):
    template_name = 'index.html'


class UserView(TemplateView, ContextMixin):
    template_name = 'user.html'
    extra_context = {"companies": Company.objects.all()}


class CompanyView(TemplateView):
    template_name = 'company.html'


class TransferView(TemplateView):
    template_name = 'transfer.html'


class AbusersView(TemplateView):
    template_name = 'abusers.html'


def report(request):
    result = []
    report_date = request.GET.get('month', '')
    for company_item in Company.objects.all().values('id', 'quote', 'name'):
        users_traffic = Transfer.objects.filter(user__company_id=company_item['id'],
                                                date__month=report_date).\
                                         aggregate(sum=Sum('traffic'))
        if users_traffic['sum'] and users_traffic['sum'] > company_item['quote']:
            result.append({
                'name': company_item['name'],
                'traffic': users_traffic['sum'],
                'quote': company_item['quote']
            })
    return JsonResponse({'data': result, 'count': len(result)})


def generate(request):
    DataGenerator().process()
    return JsonResponse({'status': True})


class UserViewSet(viewsets.ModelViewSet, APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CompanyViewSet(viewsets.ModelViewSet, APIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class TransferViewSet(viewsets.ModelViewSet, APIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

