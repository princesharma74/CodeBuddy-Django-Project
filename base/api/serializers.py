# classes that take a python object to convert into json object
from rest_framework.serializers import ModelSerializer
from base.models import Room

class RooomSerializer(ModelSerializer): 
    class Meta: 
        model = Room
        fields = '__all__'