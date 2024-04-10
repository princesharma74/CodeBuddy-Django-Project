# JSON - Javascript Object Notation
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from base.models import Room, User, Problem, Submission
from django.core.exceptions import ObjectDoesNotExist
from .serializers import SubmissionSerializer

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
                problem.submitted_by.add(user)
            problem.save()
            try: 
                submission = Submission.objects.get(submission_id=sub['submission_id'])
            except ObjectDoesNotExist:
                submission = Submission.objects.create(
                    submission_id=sub['submission_id'],
                    problem=problem,
                    submission_link=sub['submission_url'],
                )
                submission.submitted_by.add(user)
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

