from rest_framework import serializers
from .models import *  
from rest_framework.authtoken.models import Token

class PridictDiseaseModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlantDisease
        fields = "__all__"
        extra_kwargs = {
        'PerdictedDisease': {'required': False},
        'ImageFile':{'required':True}
        } 