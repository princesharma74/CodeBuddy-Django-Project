from django.urls import path
from . import views, users, rooms, submissions, problems, topics


urlpatterns = [
    path('', views.getRoutes),
    # for rooms
    path('rooms/', rooms.getRooms),
    path('room/<str:pk>', rooms.getRoom),
    
    # for users
    path('users/', users.getUsers),
    path('user/<str:pk>', users.getUser),
    path('user/<str:pk>/update', users.updateUser),
    path('user/create/<str:pk>', users.createUser),

    path('user/<str:pk>/updatesubmissions', submissions.updateSubmissions),
    path('user/<str:pk>/submissions', submissions.getSubmissions),
    path('user/<str:pk>/problems', problems.getProblemsByUser),

    # for problems
    path('problems/', problems.getProblems),

    # for topics
    path('topics/', topics.getTopics),
]