from django.contrib import admin
from django.urls import path, include
from main.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'abuse', AbuseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/', include(router.urls)),
]
