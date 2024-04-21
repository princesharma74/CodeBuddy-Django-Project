# JSON - Javascript Object Notation
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from base.models import Room, User, Topic, Message
from django.core.exceptions import ObjectDoesNotExist
from .serializers import RoomSerializer, MessageSerializer

# for rooms
# ---------------------------------------------------
@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET'])
def getRoom(request, pk):
    try: 
        room = Room.objects.get(id=pk)
        serializer = RoomSerializer(room, many=False)
        return Response(serializer.data, status = status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'Room does not exist'}, status = status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def createRoom(request, pk):
    if not User.objects.filter(username=pk).exists():
        return Response({'error': 'Host does not exist'}, status = status.HTTP_404_NOT_FOUND)
    user = User.objects.get(username=pk)
    room = Room.objects.create(
        host = user,
        name = request.data['name'],
        description = request.data['description'], 
    )
    if 'topic' in request.data:
        for topic in request.data['topic']:
            topic, created = Topic.objects.get_or_create(name=topic)
            room.topic.add(topic)
    room.participants.add(user)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['PATCH'])
def updateRoom(request, pk):
    if 'name' not in request.data or 'description' not in request.data:
        return Response({'error': 'Invalid data'}, status = status.HTTP_400_BAD_REQUEST)
    try:
        room = Room.objects.get(id=pk)
        room.name = request.data['name']
        room.description = request.data['description']
        if 'topic' in request.data:
            for topic in request.data['topic']:
                topic, created = Topic.objects.get_or_create(name=topic)
                room.topic.add(topic)
        room.save()
        serializer = RoomSerializer(room, many=False)
        return Response(serializer.data, status = status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'Room does not exist'}, status = status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteRoom(request, pk):
    try:
        room = Room.objects.get(id=pk)
        room.delete()
        return Response({'message': 'Room deleted successfully'}, status = status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'Room does not exist'}, status = status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def addParticipant(request, pk):
    try:
        room = Room.objects.get(id=pk)
        try:
            user = User.objects.get(username=request.data['participant'])
        except ObjectDoesNotExist:
            return Response({'error': 'Participant does not exist'}, status = status.HTTP_404_NOT_FOUND)
        room.participants.add(user)
        serializer = RoomSerializer(room, many=False)
        return Response(serializer.data, status = status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'Room or User does not exist'}, status = status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def sendMessage(request, pk):
    if 'sender' not in request.data or 'message' not in request.data:
        return Response({'error': 'Invalid data'}, status = status.HTTP_400_BAD_REQUEST)
    try:
        try:
            room = Room.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response({'error': 'Room does not exist'}, status = status.HTTP_404_NOT_FOUND)
        try: 
            user = User.objects.get(username=request.data['sender'])
        except ObjectDoesNotExist:
            return Response({'error': 'User does not exist'}, status = status.HTTP_404_NOT_FOUND)
        try: 
            message = Message.objects.create(
                user = user,
                room = room,
                body = request.data['message'],
            )
            room.participants.add(user)
        except ObjectDoesNotExist:
            return Response({'error': 'Message could not be sent'}, status = status.HTTP_400_BAD_REQUEST)
        serializer = MessageSerializer(message, many=False)
        return Response(serializer.data, status = status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'Room does not exist'}, status = status.HTTP_404_NOT_FOUND)

@api_view( ['POST'] )
def createRooms(request, pk): 
    if not User.objects.filter(username=pk).exists():
        return Response({'error': 'Host does not exist'}, status = status.HTTP_404_NOT_FOUND)
    user = User.objects.get(username=pk)
    for room in request.data:
        room_data = room
        room = Room.objects.create(
            host = user,
            name = room['name'],
            description = room['description'], 
        )
        if 'topic' in room_data:
            for topic in room_data['topic']:
                topic_obj, created = Topic.objects.get_or_create(name=topic)
                room.topic.add(topic_obj)
        room.participants.add(user)
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data, status = status.HTTP_201_CREATED)