# REST FRAMEWORK
from rest_framework import serializers
from .models import *

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('pk','first_name', 'last_name', 'email', 'company')

    def add(self,data):
        return User.objects.create(data)

    def edit(self, instance, data):
        instance.first_name = data.get('first_name',instance.first_name)
        instance.last_name = data.get('last_name',instance.last_name)
        instance.email = data.get('email',instance.email)
        instance.company = data.get('company',instance.company)
        instance.save()
        return instance

    def delete(self,instance,data):
        instance.delete()
        return instance
        

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('pk', 'name', 'quote')

    def add(self,data):
        return Company.objects.create(data)

    def edit(self, instance, data):
        instance.name = data.get('name',instance.name)
        instance.quote = data.get('quote',instance.quote)
        instance.save()
        return instance

    def delete(self,instance,data):
        instance.delete()
        return instance

class AbuseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transfer
        fields = ('pk','user', 'date', 'resource', 'traffic')
