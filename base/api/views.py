# JSON - Javascript Object Notation
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from base.models import Room, User, Problem, Topic, Submission
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from .serializers import RoomSerializer, UserSerializer, ProblemSerializer, TopicSerializer, SubmissionSerializer, UserLoginSerializer

@api_view(['GET'])
def getRoutes(request): 
    routes = [
        'GET /api',
        # for rooms
        'GET /api/rooms',
        'GET /api/rooms/:id',
        # for users
        'GET /api/users',
        'GET /api/users/:username',
        'PATCH /api/users/:username',
        # for submissions
        'GET /api/users/:username/submissions',
        'POST /api/users/:username/submissions/update',
        'POST /api/users/:username/submissions/create',
        # for problems
        'GET /api/problems',
        # for topics
        'GET /api/topics',
    ]
    return Response(routes)

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

# ---------------------------------------------------

# for users - sill commend for checking workflow
# ---------------------------------------------------
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
            user.gender = data
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
        
        user.save()
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    except:
        return Response({'error': 'Something went wrong.'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def checkUserAuthentication(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return Response({'message': 'User is authenticated'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# for submissions
# ---------------------------------------------------
@api_view(['GET'])
def getSubmissions(request, pk):
    # check if the user exists
    if not User.objects.filter(username=pk).exists():
        return Response({'error': 'User does not exist'}, status = status.HTTP_404_NOT_FOUND)
    try: 
        submissions = Submission.objects.filter(submitted_by=pk)
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'User does not exist'}, status = status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def updateSubmissions(request, pk):
    data = request.data
    try: 
        user = User.objects.get(username=pk)
        retdata = []
        for sub in data:
            # check if platform, problem_title, problem_link, submission_id, submission_url, exists and is not empty
            if 'platform' not in sub or 'problem_title' not in sub or 'problem_link' not in sub or 'submission_id' not in sub or 'submission_url' not in sub:
                return Response({'error': 'Invalid submission data'}, status = status.HTTP_400_BAD_REQUEST)
            try:
                problem = Problem.objects.get(url=sub['problem_link'])
            except ObjectDoesNotExist:
                problem = Problem.objects.create(
                    title=sub['problem_title'],
                    url=sub['problem_link'],
                    platform=sub['platform'],
                )
            try: 
                submission = Submission.objects.get(submission_id=sub['submission_id'])
            except ObjectDoesNotExist:
                submission = Submission.objects.create(
                    submission_id=sub['submission_id'],
                    problem=problem,
                    submission_link=sub['submission_url'],
                    submitted_by=user,
                )
            retdata.append(submission)
        serializer = SubmissionSerializer(retdata, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'User does not exist'}, status = status.HTTP_404_NOT_FOUND)
        

@api_view(['POST'])
def createSubmission(request, pk):
    data = request.data
    user = User.objects.get(username=pk)
    try:
        problem = Problem.objects.get(url=data['problem_link'])
    except ObjectDoesNotExist:
        problem = Problem.objects.create(
            title=data['problem_title'],
            url=data['problem_link'],
            platform=data['platform'],
        )
    submission = Submission.objects.create(
        submission_id=data['submission_id'],
        problem=problem,
        submission_link=data['submission_url'],
        submitted_by=user,
    )
    serializer = SubmissionSerializer(submission, many=False)
    return Response(serializer.data)


# for problems
# ---------------------------------------------------
@api_view(['GET'])
def getProblems(request):
    problems = Problem.objects.all()
    serializer = ProblemSerializer(problems, many=True)
    return Response(serializer.data)
# ---------------------------------------------------

# for topics
# ---------------------------------------------------
@api_view(['GET'])
def getTopics(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)
# ---------------------------------------------------