from django.contrib import admin
from django.urls import path, include
from main.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('user/', user, name='user'),
    path('company/', company, name='company'),
    path('abusers/', abusers, name='abusers'),
    path('api/', include(router.urls)),
]
