from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from base.models import User, Leetcode, Codechef, Codeforces
from django.core.exceptions import ObjectDoesNotExist
from .serializers import UserSerializer, BasicUserSerializer, LeetcodeSerializer, CodechefSerializer, CodeforcesSerializer


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
        data = request.data
        leetcode_data = data.pop('leetcode', None)
        codechef_data = data.pop('codechef', None)
        codeforces_data = data.pop('codeforces', None)
        data['username'] = pk
        if leetcode_data:
            if not Leetcode.objects.filter(user=user).exists():
                leetcode, _ = Leetcode.objects.get_or_create(
                    user=user,
                    id=leetcode_data.get('id', None),
                )
            else: 
                leetcode = Leetcode.objects.get(user=user)
            leetcode.rating = leetcode_data.get('rating', None)
            leetcode.global_rank = leetcode_data.get('global_rank', None)
            leetcode.number_of_contests = leetcode_data.get('number_of_contests', None)
            leetcode.number_of_questions = leetcode_data.get('number_of_questions', None)
            leetcode.save()
        if codechef_data:
            if not Codechef.objects.filter(user=user).exists():
                codechef, _ = Codechef.objects.get_or_create(
                    user=user,
                    id=codechef_data.get('id', None),
                )
            else:
                codechef = Codechef.objects.get(user=user)
            codechef.rating = codechef_data.get('rating', None)
            codechef.global_rank = codechef_data.get('global_rank', None)
            codechef.number_of_contests = codechef_data.get('number_of_contests', None)
            codechef.number_of_questions = codechef_data.get('number_of_questions', None)
            codechef.save()

        if codeforces_data:
            if not Codeforces.objects.filter(user=user).exists():
                codeforces, _ = Codeforces.objects.get_or_create(
                    user=user,
                    id=codeforces_data.get('id', None),
                )
            else:
                codeforces = Codeforces.objects.get(user=user)
            codeforces.rating = codeforces_data.get('rating', None)
            codeforces.global_rank = codeforces_data.get('global_rank', None)
            codeforces.number_of_contests = codeforces_data.get('number_of_contests', None)
            codeforces.number_of_questions = codeforces_data.get('number_of_questions', None)
            codeforces.save()

        user.leetcode = leetcode
        user.codechef = codechef
        user.codeforces = codeforces
        user.save()
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
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
    if User.objects.filter(username=pk).exists():
        return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
    data = request.data
    leetcode_data = data.pop('leetcode', None)
    codechef_data = data.pop('codechef', None)
    codeforces_data = data.pop('codeforces', None)
    data['username'] = pk
    serializer = BasicUserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    user = User.objects.get(username=pk)
    if leetcode_data:
        leetcode, _ = Leetcode.objects.get_or_create(
            user=user,
            id=leetcode_data.get('id', None),
        )
        leetcode.rating = leetcode_data.get('rating', None)
        leetcode.global_rank = leetcode_data.get('global_rank', None)
        leetcode.number_of_contests = leetcode_data.get('number_of_contests', None)
        leetcode.number_of_questions = leetcode_data.get('number_of_questions', None)
        leetcode.save()
    if codechef_data:
        codechef, _ = Codechef.objects.get_or_create(
            user=user,
            id=codechef_data.get('id', None),
        )
        codechef.rating = codechef_data.get('rating', None)
        codechef.global_rank = codechef_data.get('global_rank', None)
        codechef.number_of_contests = codechef_data.get('number_of_contests', None)
        codechef.number_of_questions = codechef_data.get('number_of_questions', None)
        codechef.save()

    if codeforces_data:
        codeforces, _ = Codeforces.objects.get_or_create(
            user=user,
            id=codeforces_data.get('id', None),
        )
        codeforces.rating = codeforces_data.get('rating', None)
        codeforces.global_rank = codeforces_data.get('global_rank', None)
        codeforces.number_of_contests = codeforces_data.get('number_of_contests', None)
        codeforces.number_of_questions = codeforces_data.get('number_of_questions', None)
        codeforces.save()

    user.leetcode = leetcode
    user.codechef = codechef
    user.codeforces = codeforces
    user.save()
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)