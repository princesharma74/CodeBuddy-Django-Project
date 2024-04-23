from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Contest
from rest_framework import status
from .serializers import ContestSerializer

@api_view(['GET'])
def getContests(request):
    contests = Contest.objects.all()
    serializer = ContestSerializer(contests, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getUpcomingContests(request):
    # filter the contests that are yet to start wrt start_time
    contests = Contest.objects.filter(start_time__gt=datetime.now())
    serializer = ContestSerializer(contests, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def createContest(request):
    data = []
    for contest in request.data: 
        if Contest.objects.filter(title=contest['title']).exists():
            # update the contest
            contest_obj = Contest.objects.get(title=contest['title'])
            contest_obj.url = contest.get('url', None)
            contest_obj.platform = contest.get('platform', None)
            contest_obj.start_time = contest.get('start_time', None)
            contest_obj.save()
        serializer = ContestSerializer(data=contest)
        if serializer.is_valid():
            serializer.save()
        data.append(serializer.data)
    return Response(data, status=status.HTTP_201_CREATED)

# @api_view(['GET'])
# def getContest(request):
#     if 'title' not in request.data:
#         return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
#     title = request.data['title']
#     if not Contest.objects.filter(title=title).exists():
#         return Response({'error': 'Contest does not exist'}, status=status.HTTP_404_NOT_FOUND)
#     contest = Contest.objects.get(title=title)
#     serializer = ContestSerializer(contest, many=False)
#     return Response(serializer.data, status=status.HTTP_200_OK)