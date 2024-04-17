from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import  Problem
from .serializers import  ProblemSerializer
from rest_framework import status

@api_view(['GET'])
def getProblems(request):
    problems = Problem.objects.all()
    serializer = ProblemSerializer(problems, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET'])
def getProblemsByUser(request, pk):
    problems = Problem.objects.filter(submitted_by=pk)
    serializer = ProblemSerializer(problems, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)