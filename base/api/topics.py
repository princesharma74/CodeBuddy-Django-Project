from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Topic
from .serializers import TopicSerializer
from rest_framework import status

@api_view(['GET'])
def getTopics(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)