from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from base.models import User
from django.core.exceptions import ObjectDoesNotExist
from .serializers import UserSerializer


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
        data = request.data
        user = User.objects.get(username=pk)
        if 'email' in data:
            user.email = data['email']
        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']
        if 'bio' in data:
            user.bio = data['bio']
        if 'gender' in data:
            user.gender = data['gender']
        if 'codechef_id' in data:
            user.codechef_id = data['codechef_id']
        if 'leetcode_id' in data:
            user.leetcode_id = data['leetcode_id']
        if 'codeforces_id' in data:
            user.codeforces_id = data['codeforces_id']
        if 'codechef_rating' in data:
            user.codechef_rating = data['codechef_rating']
        if 'leetcode_rating' in data:
            user.leetcode_rating = data['leetcode_rating']
        if 'codeforces_rating' in data:
            user.codeforces_rating = data['codeforces_rating']
        if 'number_of_codeforces_contests' in data:
            user.number_of_codeforces_contests = data['number_of_codeforces_contests']
        if 'number_of_leetcode_contests' in data:
            user.number_of_leetcode_contests = data['number_of_leetcode_contests']
        if 'number_of_codechef_contests' in data:
            user.number_of_codechef_contests = data['number_of_codechef_contests']
        if 'number_of_codeforces_questions' in data:
            user.number_of_codeforces_questions = data['number_of_codeforces_questions']
        if 'number_of_leetcode_questions' in data:
            user.number_of_leetcode_questions = data['number_of_leetcode_questions']
        if 'number_of_codechef_questions' in data:
            user.number_of_codechef_questions = data['number_of_codechef_questions']
        if 'global_rank_codeforces' in data:
            user.global_rank_codeforces = data['global_rank_codeforces']
        if 'global_rank_leetcode' in data:
            user.global_rank_leetcode = data['global_rank_leetcode']
        if 'global_rank_codechef' in data:
            user.global_rank_codechef = data['global_rank_codechef']
        if 'avatar' in data:
            user.avatar = data['avatar']

        user.save()
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status = status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'User does not exist'}, status = status.HTTP_404_NOT_FOUND)

'''
@api_view(['POST'])
def checkUserExists(request):
    data = request.data
    if 'username' not in data:
        return Response({'error': 'Invalid user data'}, status = status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(username=data['username']).exists():
        return Response({'message': 'User exists'}, status = status.HTTP_200_OK)
    return Response({'message': 'User does not exist'}, status = status.HTTP_404_NOT_FOUND)
'''


@api_view(['POST'])
def createUser(request, pk):
    # check if the user already exists
    if User.objects.filter(username=pk).exists():
        return Response({'message': 'User already exists'}, status = status.HTTP_200_OK)
    data = request.data
    # check if username, email, first_name, last_name exists and is not empty
    if 'email' not in data or 'first_name' not in data or 'last_name' not in data:
        return Response({'error': 'Invalid user data'}, status = status.HTTP_400_BAD_REQUEST)
    try: 
        user = User.objects.create(
            username=pk,
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
        )
        if 'bio' in data:
            user.bio = data['bio']
        if 'codechef_id' in data:
            user.codechef_id = data['codechef_id']
        if 'leetcode_id' in data:
            user.leetcode_id = data['leetcode_id']
        if 'codeforces_id' in data:
            user.codeforces_id = data['codeforces_id']
        if 'codechef_rating' in data:
            user.codechef_rating = data['codechef_rating']
        if 'leetcode_rating' in data:
            user.leetcode_rating = data['leetcode_rating']
        if 'codeforces_rating' in data:
            user.codeforces_rating = data['codeforces_rating']
        if 'number_of_codeforces_contests' in data:
            user.number_of_codeforces_contests = data['number_of_codeforces_contests']
        if 'number_of_leetcode_contests' in data:
            user.number_of_leetcode_contests = data['number_of_leetcode_contests']
        if 'number_of_codechef_contests' in data:
            user.number_of_codechef_contests = data['number_of_codechef_contests']
        if 'number_of_codeforces_questions' in data:
            user.number_of_codeforces_questions = data['number_of_codeforces_questions']
        if 'number_of_leetcode_questions' in data:
            user.number_of_leetcode_questions = data['number_of_leetcode_questions']
        if 'number_of_codechef_questions' in data:
            user.number_of_codechef_questions = data['number_of_codechef_questions']
        if 'global_rank_codeforces' in data:
            user.global_rank_codeforces = data['global_rank_codeforces']
        if 'global_rank_leetcode' in data:
            user.global_rank_leetcode = data['global_rank_leetcode']
        if 'global_rank_codechef' in data:
            user.global_rank_codechef = data['global_rank_codechef']
        
        user.save()
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    except:
        return Response({'error': 'Something went wrong.'}, status = status.HTTP_400_BAD_REQUEST)