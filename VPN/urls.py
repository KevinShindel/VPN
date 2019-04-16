from django.contrib import admin
from django.urls import path, include
from main.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'transfer', TransferViewSet)
router.register(r'abusers', AbusersViewSet)

urlpatterns = [

    # ADMIN URL
    path('admin/', admin.site.urls),

    # MY URLS 

    path('', main, name='main'),
    path('user/', user, name='user'),
    path('company/', company, name='company'),
    path('transfer/', transfer, name='transfer'),
    path('abusers/', abusers, name='abusers'),

    # REST API URL
    path('api_auth/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
