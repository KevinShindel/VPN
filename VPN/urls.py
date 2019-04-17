from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from main.views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'transfer', TransferViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main, name='main'),
    path('user/', user, name='user'),
    path('company/', company, name='company'),
    path('transfer/', transfer, name='transfer'),

    path('abusers/', abusers, name='abusers'),
    path('abusers/report/', report, name='report'),
    path('abusers/generate/', generate, name='generate'),

    # REST API URL
    path('api_auth/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
