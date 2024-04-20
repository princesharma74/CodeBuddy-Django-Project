from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from base.models import Message, Room
from .serializers import MessageSerializer
from rest_framework import status

@api_view(['GET'])
def getMessages(request, pk):
    try: 
        room = Room.objects.get(id=pk)
        messages = Message.objects.filter(room=room)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'Room does not exist'}, status = status.HTTP_404_NOT_FOUND)