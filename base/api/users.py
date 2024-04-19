from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from base.models import User
from django.core.exceptions import ObjectDoesNotExist
from .serializers import UserSerializer, CreateUserSerializer


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET'])
def getUser(request, pk):
    try: 
        user = User.objects.get(username=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status = status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'User does not exist'}, status = status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def updateUser(request, pk):
    try: 
        user = User.objects.get(username=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def authUser(request, pk): 
    data = request.data
    if 'password' not in data: 
        return Response({'error': 'Invalid user data'}, status = status.HTTP_400_BAD_REQUEST)
    try: 
        user = User.objects.get(username=pk)
        if user.check_password(data['password']):
            serializer = UserSerializer(user, many=False)
            return Response({'message': 'User authenticated', 'user': serializer.data}, status = status.HTTP_200_OK)
        else: 
            return Response({'error': 'Invalid credentials'}, status = status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response({'error': 'User does not exist'}, status = status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def createUser(request, pk):
    try:
        # Check if the user already exists
        if User.objects.filter(username=pk).exists():
            return Response({'message': 'User already exists'}, status=status.HTTP_200_OK)
        
        # Validate request data
        request.data["username"] = pk
        serializer = CreateUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Create user
        user = serializer.save(username=pk)
        
        return Response(user.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)