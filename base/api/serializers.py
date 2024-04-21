# classes that take a python object to convert into json object
from rest_framework.serializers import ModelSerializer, CharField, Serializer
from base.models import Room, User, Problem, Topic, Submission, Contest, RatingChange, Leetcode, Codechef, Codeforces, Message


class BasicUserSerializer(ModelSerializer):
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
class LeetcodeSerializer(ModelSerializer):
    class Meta:
        model = Leetcode
        fields = '__all__'
class CodechefSerializer(ModelSerializer):
    class Meta:
        model = Codechef
        fields = '__all__'


class CodeforcesSerializer(ModelSerializer):
    class Meta:
        model = Codeforces
        fields = '__all__'

class UserSerializer(ModelSerializer):
    leetcode = LeetcodeSerializer()
    codechef = CodechefSerializer()
    codeforces = CodeforcesSerializer()
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

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
class RoomSerializer(ModelSerializer): 
    topic = TopicSerializer()
    class Meta: 
        model = Room
        fields = '__all__'
class UserLoginSerializer(Serializer):
    username = CharField(max_length=255)
    password = CharField(max_length=128)

class ProblemSerializer(ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'


class SubmissionSerializer(ModelSerializer):
    problem = CharField(source='problem.title', read_only=True)
    class Meta:
        model = Submission
        # all fields except created_at, last_edited_at, submitted_by
        exclude = ['created_at', 'last_edited_at', 'submitted_by']

class ContestSerializer(ModelSerializer):
    class Meta:
        model = Contest
        exclude = ['created_at', 'last_edited_at']


class RatingChangeSerializer(ModelSerializer):
    contest = ContestSerializer()  # Nested serializer for Contest

    class Meta:
        model = RatingChange
        exclude = ['created_at', 'last_edited_at']

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        exclude = ['room']