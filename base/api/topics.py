from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Topic, Room
from .serializers import TopicSerializer
from rest_framework import status

@api_view(['GET'])
def getTopics(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    ret = serializer.data
    # count number of rooms in each topic
    for i in range(len(ret)):
        ret[i]['room_count'] = Room.objects.filter(topics__name=ret[i]['name']).count()
    return Response(serializer.data, status = status.HTTP_200_OK)