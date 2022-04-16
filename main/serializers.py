from rest_framework import serializers

from .models import Company, User, Transfer


class CompanySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    DT_RowID = serializers.SerializerMethodField()
    DT_RowAttr = serializers.SerializerMethodField()

    def get_DT_RowID(self, company):
        return 'row_%d' % company.pk

    def get_DT_RowAttr(self, transfer):
        return {'data_pk': transfer.pk}

    class Meta:
        model = Company
        fields = ('id', 'name', 'quote', 'DT_RowID', 'DT_RowAttr')
        datatables_always_serialize = ('id',)


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    company_name = serializers.ReadOnlyField(source='company.name')
    DT_RowID = serializers.SerializerMethodField()
    DT_RowAttr = serializers.SerializerMethodField()

    def get_DT_RowID(self, user):
        return 'row_%d' % user.pk

    def get_DT_RowAttr(self, user):
        return {'data_pk': user.pk}

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'company', 'company_name', 'DT_RowID', 'DT_RowAttr')
        datatables_always_serialize = ('id',)


class TransferSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_name = serializers.ReadOnlyField(source='user.first_name')
    user = UserSerializer()
    DT_RowID = serializers.SerializerMethodField()
    DT_RowAttr = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    def get_date(self, transfer: Transfer):
        return transfer.date.strftime('%c')

    def get_DT_RowID(self, transfer):
        return 'row_%d' % transfer.pk

    def get_DT_RowAttr(self, transfer):
        return {'data_pk': transfer.pk}

    class Meta:
        model = Transfer
        fields = ('id', 'user_name', 'user', 'date', 'resource', 'traffic', 'DT_RowID', 'DT_RowAttr')
        datatables_always_serialize = ('id',)
