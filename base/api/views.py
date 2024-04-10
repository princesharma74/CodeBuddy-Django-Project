# JSON - Javascript Object Notation
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


