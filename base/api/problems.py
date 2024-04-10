from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from base.models import Room, User, Problem, Topic, Submission
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from .serializers import RoomSerializer, UserSerializer, ProblemSerializer, TopicSerializer, SubmissionSerializer, UserLoginSerializer

@api_view(['GET'])
def getProblems(request, pk):
    problems = Problem.objects.filter(submitted_by=pk)
    serializer = ProblemSerializer(problems, many=True)
    return Response(serializer.data)