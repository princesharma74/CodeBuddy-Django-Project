# classes that take a python object to convert into json object
from rest_framework.serializers import ModelSerializer, CharField, Serializer, ValidationError
from base.models import Room, User, Problem, Topic, Submission, Contest, RatingChange

class RoomSerializer(ModelSerializer): 
    class Meta: 
        model = Room
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Or specify the fields you want to include
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))  # Set password securely
        return super().update(instance, validated_data)


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

class ContestSerializer(ModelSerializer):
    class Meta:
        model = Contest
        fields = '__all__'


class RatingChangeSerializer(ModelSerializer):
    contest = ContestSerializer()  # Nested serializer for Contest

    class Meta:
        model = RatingChange
        fields = '__all__'