from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Contest
from .serializers import ContestSerializer

@api_view(['GET'])
def getContests(request):
    contests = Contest.objects.all()
    serializer = ContestSerializer(contests, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createContest(request):
    serializer = ContestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getContest(request):
    title = request.data['title']
    contest = Contest.objects.get(title=title)
    serializer = ContestSerializer(contest, many=False)
    return Response(serializer.data)