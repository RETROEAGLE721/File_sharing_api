from rest_framework import serializers
from.models import Users,file_datas,operation

class Users_serializers(serializers.ModelSerializer):
    class Meta:
        model = Users 
        fields = '__all__'

class Operation_serializers(serializers.ModelSerializer):
    class Meta:
        model = operation 
        fields = '__all__'


class file_datas_serializers(serializers.ModelSerializer):
    class Meta:
        model = file_datas 
        fields = '__all__'