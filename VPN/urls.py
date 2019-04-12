from django.contrib import admin
from django.urls import path, include
from main.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'transfer', TransferViewSet)

urlpatterns = [

    # ADMIN URL
    path('admin/', admin.site.urls),

    # MY URLS 

    path('', main, name='main'),
    path('user/', user, name='user'),
    path('company/', company, name='company'),
    path('transfer/', transfer, name='transfer'),

    # REST API URL
    path('api/', include(router.urls)),
]
