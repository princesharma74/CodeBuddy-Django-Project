# JSON - Javascript Object Notation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room, User, Problem, Topic, Submission
from django.core.exceptions import ObjectDoesNotExist
from .serializers import RooomSerializer, UserSerializer, ProblemSerializer, TopicSerializer, SubmissionSerializer

@api_view(['GET'])
def getRoutes(request): 
    routes = [
        'GET /api',
        # for rooms
        'GET /api/rooms',
        'GET /api/rooms/:id'

    ]
    return Response(routes)

# for rooms
# ---------------------------------------------------
@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RooomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RooomSerializer(room, many=False)
    return Response(serializer.data)

# ---------------------------------------------------

# for users
# ---------------------------------------------------
@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
def updateUser(request, pk):
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
    return Response(serializer.data)

@api_view(['POST'])
def updateSubmissions(request, pk):
    data = request.data
    user = User.objects.get(username=pk)
    retdata = []
    for sub in data:
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
    return Response(retdata)
        

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

@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(username=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# ---------------------------------------------------

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