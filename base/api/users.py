from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from base.models import User, Leetcode, Codechef, Codeforces
from django.core.exceptions import ObjectDoesNotExist
from .serializers import UserSerializer, LeetcodeSerializer, CodechefSerializer, CodeforcesSerializer, BasicUserSerializer


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
    except ObjectDoesNotExist:
        return Response({'error': 'User does not exist'}, status = status.HTTP_404_NOT_FOUND)
    data = request.data
    leetcode_data = data.pop('leetcode', None)
    codeforces_data = data.pop('codeforces', None)
    codechef_data = data.pop('codechef', None)
    try: 
        data['username'] = pk
        serializer = BasicUserSerializer(instance=user, data=data, many=False)
        if serializer.is_valid(): 
            user = serializer.save()
        else:
            errors = serializer.errors
            print("Validation errors:", errors)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        if leetcode_data is not None:
            leetcode_serializer = LeetcodeSerializer(instance=user.leetcode, data=leetcode_data, many=False)
            if leetcode_serializer.is_valid():
                leetcode = leetcode_serializer.save()
                user.leetcode = leetcode
                user.save()
            else: 
                errors = leetcode_serializer.errors
                print("Validation errors:", errors)
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        if codeforces_data is not None:
            codeforces_serializer = CodeforcesSerializer(instance=user.codeforces, data=codeforces_data, many=False)
            if codeforces_serializer.is_valid():
                codeforces = codeforces_serializer.save()
                user.codeforces = codeforces
                user.save()
            else: 
                errors = codeforces_serializer.errors
                print("Validation errors:", errors)
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        if codechef_data is not None:
            codechef_serializer = CodechefSerializer(instance=user.codechef, data=codechef_data, many=False)
            if codechef_serializer.is_valid():
                codechef = codechef_serializer.save()
                user.codechef = codechef
                user.save()
            else: 
                errors = codechef_serializer.errors
                print("Validation errors:", errors)
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


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
    data = request.data
    leetcode_data = data.pop('leetcode', None)
    codeforces_data = data.pop('codeforces', None)
    codechef_data = data.pop('codechef', None)
    try: 
        data['username'] = pk
        serializer = BasicUserSerializer(data=data, many=False)
        if serializer.is_valid(): 
            user = serializer.save()
        else:
            errors = serializer.errors
            print("Validation errors:", errors)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        if leetcode_data is not None:
            leetcode_serializer = LeetcodeSerializer(data=leetcode_data, many=False)
            if leetcode_serializer.is_valid():
                leetcode = leetcode_serializer.save()
                user.leetcode = leetcode
                user.save()
            else: 
                errors = leetcode_serializer.errors
                print("Validation errors:", errors)
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        if codeforces_data is not None:
            codeforces_serializer = CodeforcesSerializer(data=codeforces_data, many=False)
            if codeforces_serializer.is_valid():
                codeforces = codeforces_serializer.save()
                user.codeforces = codeforces
                user.save()
            else: 
                errors = codeforces_serializer.errors
                print("Validation errors:", errors)
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        if codechef_data is not None:
            codechef_serializer = CodechefSerializer(data=codechef_data, many=False)
            if codechef_serializer.is_valid():
                codechef = codechef_serializer.save()
                user.codechef = codechef
                user.save()
            else: 
                errors = codechef_serializer.errors
                print("Validation errors:", errors)
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
