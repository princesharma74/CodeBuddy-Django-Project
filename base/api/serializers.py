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
        fields = ['user', 'rating_change', 'rank', 'final_rating', 'number_of_problems_solved', 'time_taken', 'contest']

    def create(self, validated_data):
        contest_data = validated_data.pop('contest')
        contest, _ = Contest.objects.get_or_create(**contest_data)
        rating_change = RatingChange.objects.create(contest=contest, **validated_data)
        return rating_change