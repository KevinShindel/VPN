# REST FRAMEWORK
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User as AdminUser, Group as AdminGroup


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdminUser
        fields = ('username', 'first_name', 'last_name',  'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdminGroup
        fields = ('name', 'permissions')


class UserViewSet(viewsets.ModelViewSet):
    queryset = AdminUser.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
