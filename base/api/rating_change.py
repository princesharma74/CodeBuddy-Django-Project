from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import RatingChange, User, Contest
from rest_framework import status
from .serializers import RatingChangeSerializer, ContestSerializer

@api_view(['POST'])
def createRatingChange(request, pk):
    if 'contest' not in request.data or 'rating_change' not in request.data or 'rank' not in request.data or 'final_rating' not in request.data or 'number_of_problems_solved' not in request.data:
        return Response({'detail': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    data = request.data
    user = User.objects.get(username=pk)

    constest_data = data['contest']
    if 'title' not in constest_data: 
        return Response({'error': 'Invalid contest data'}, status=status.HTTP_400_BAD_REQUEST)

    if not Contest.objects.filter(title=constest_data['title']).exists():
        try: 
            serializer.save()
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else: 
        contest = Contest.objects.get(title=constest_data['title'])

    rating_changes = RatingChange.objects.filter(user=user, contest=contest)

    if not rating_changes.exists():
        RatingChange.objects.create(
            user=user, 
            contest=contest,
            rating_change=data['rating_change'], 
            rank=data['rank'], 
            final_rating=data['final_rating'], 
            number_of_problems_solved=data['number_of_problems_solved']
        )
    else:
        rating_change = rating_changes.first()
        rating_change.rating_change = data['rating_change']
        rating_change.rank = data['rank']
        rating_change.final_rating = data['final_rating']
        rating_change.number_of_problems_solved = data['number_of_problems_solved']
        rating_change.save()

    ratingchange = RatingChange.objects.filter(user=user, contest=contest).first()
    serializer = RatingChangeSerializer(ratingchange, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def getRatingChanges(request, pk):
    # get all rating changes of a user
    user = User.objects.get(username=pk)
    rating_changes = RatingChange.objects.filter(user=user)
    serializer = RatingChangeSerializer(rating_changes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)