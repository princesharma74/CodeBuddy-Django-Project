from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import RatingChange, User, Contest
from rest_framework import status
from .serializers import RatingChangeSerializer, ContestSerializer, BasicRatingChangeSerializer

def createRatingChange(data, username):
    if 'user' not in data:
        return {"error": "User not provided"}
    user = User.objects.get(username=username)
    # check if contest exists
    if 'contest' not in data or 'title' not in data['contest']:
        return {"error": "Contest not provided"}
    if Contest.objects.filter(title=data['contest']['title']).exists():
        contest = Contest.objects.get(title=data['contest']['title'])
        contest_serializer = ContestSerializer(instance=contest, data=data['contest'])
        if contest_serializer.is_valid():
            contest = contest_serializer.save()        
        else:
            return {"error": contest_serializer.errors}
    else:
        contest_serializer = ContestSerializer(data=data['contest'])
        if contest_serializer.is_valid():
            contest = contest_serializer.save()
        else:
            return {"error": contest_serializer.errors}
    data.pop('contest')
    if RatingChange.objects.filter(contest=contest, user=user).exists():
        rating_change_obj = RatingChange.objects.get(contest=contest, user=user)
        rating_change_serializer = BasicRatingChangeSerializer(instance=rating_change_obj, data=data)
    else:
        rating_change_serializer = BasicRatingChangeSerializer(data=data)
    if rating_change_serializer.is_valid():
        rating_change = rating_change_serializer.save()
        rating_change.contest = contest
        rating_change.user = user
        rating_change.save()
    else:
        return {"error": rating_change_serializer.errors}
    rating_change_serializer = RatingChangeSerializer(rating_change)
    return rating_change_serializer.data
    

@api_view(['POST'])
def createRatingChanges(request, pk):
    ret = []
    for data in request.data: 
        ret.append(createRatingChange(data, pk))
    return Response(ret, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def getRatingChanges(request, pk):
    # get all rating changes of a user
    user = User.objects.get(username=pk)
    rating_changes = RatingChange.objects.filter(user=user)
    serializer = RatingChangeSerializer(rating_changes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)