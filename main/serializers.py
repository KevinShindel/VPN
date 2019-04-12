# REST FRAMEWORK
from rest_framework import serializers
from .models import *


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'company')
        datatables_always_serialize = ('id',)


class CompanySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'quote')
        datatables_always_serialize = ('id',)


class TransferSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Transfer
        fields = ('id', 'user', 'date', 'resource', 'traffic')
        datatables_always_serialize = ('id',)
