from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from main.views import (UserView, UserViewSet, CompanyViewSet, TransferViewSet, MainView,
                        CompanyView, TransferView, AbusersView, report, generate)

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('company', CompanyViewSet)
router.register('transfer', TransferViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('user/', UserView.as_view(), name='user'),
    path('company/', CompanyView.as_view(), name='company'),
    path('transfer/', TransferView.as_view(), name='transfer'),
    path('abusers/', AbusersView.as_view(), name='abusers'),
    path('abusers/report/', report, name='report'),
    path('abusers/generate/', generate, name='generate'),
    # REST API URL
    path('api_auth/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
