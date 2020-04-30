from rest_framework import serializers
from .models import *


class CommonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['name', 'company_id']


class MutualFreindDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['name', 'age', 'address', 'phone']



class PersonDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['name', 'age', "favourite_fruit", 'favourite_vegetable']