# classes that take a python object to convert into json object
from rest_framework.serializers import ModelSerializer, CharField, Serializer
from base.models import Room, User, Problem, Topic, Submission, Contest, RatingChange, Leetcode, Codechef, Codeforces, Message


class LeetcodeSerializer(ModelSerializer):
    class Meta:
        model = Leetcode
        exclude = ['id']
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
class CodechefSerializer(ModelSerializer):
    class Meta:
        model = Codechef
        exclude = ['id']
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class CodeforcesSerializer(ModelSerializer):
    class Meta:
        model = Codeforces
        exclude = ['id']    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class BasicUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def update(self, instance, validated_data):
        # Update all the specified attributes
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.gender = validated_data.get('gender', instance.gender)

        # Hash the password if provided
        password = validated_data.get('password')
        instance.set_password(password)
        # Save the updated instance
        instance.save()
        return instance

class UserSerializer(ModelSerializer):
    leetcode = LeetcodeSerializer(many=False)
    codechef = CodechefSerializer(many=False)
    codeforces = CodeforcesSerializer(many=False)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Update all the specified attributes
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.gender = validated_data.get('gender', instance.gender)

        # Hash the password if provided
        password = validated_data.get('password')
        instance.set_password(password)
        # Save the updated instance
        instance.save()
        return instance

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
class RoomSerializer(ModelSerializer): 
    topics = TopicSerializer(many=True)
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

class BasicRatingChangeSerializer(ModelSerializer):

    class Meta:
        model = RatingChange
        fields = '__all__'
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        exclude = ['room']