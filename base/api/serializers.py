# classes that take a python object to convert into json object
from rest_framework.serializers import ModelSerializer, CharField, Serializer
from base.models import Room, User, Problem, Topic, Submission

class RoomSerializer(ModelSerializer): 
    class Meta: 
        model = Room
        fields = '__all__'

from django.contrib.auth.hashers import make_password

class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)  # Add this line

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class UserLoginSerializer(Serializer):
    username = CharField(max_length=255)
    password = CharField(max_length=128)

class ProblemSerializer(ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class SubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'