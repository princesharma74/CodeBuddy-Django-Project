from django.urls import path
from . import views, users, rooms, submissions, problems, topics, contests, rating_change, messages


urlpatterns = [
    path('', views.getRoutes),
    path('rooms', rooms.getRooms),
    path('room/<str:pk>/messages', messages.getMessages),
    path('room/<str:pk>', rooms.getRoom),
    path('users/', users.getUsers),
    path('user/<str:pk>', users.getUser),
    path('user/<str:pk>/create', users.createUser),
    path('user/<str:pk>/room/create', rooms.createRoom),
    path('user/<str:pk>/rooms/create', rooms.createRooms),
    path('user/<str:pk>/update', users.updateUser),
    path('user/<str:pk>/updatesubmissions', submissions.updateSubmissions),
    path('user/<str:pk>/submissions', submissions.getSubmissions),
    path('problems', problems.getProblems),
    path('user/<str:pk>/problems', problems.getProblemsByUser),
    path('user/<str:pk>/authenticate', users.authUser),
    path('user/<str:pk>/get-rating-changes', rating_change.getRatingChanges),
    path('user/<str:pk>/create-rating-changes', rating_change.createRatingChanges),
    path('topics', topics.getTopics),
    path('room/<str:pk>/add-participant', rooms.addParticipant),
    path('room/<str:pk>/send-message', rooms.sendMessage),
    path('room/<str:pk>/update', rooms.updateRoom),
    path('room/<str:pk>/delete', rooms.deleteRoom),
    path('contests/create', contests.createContest),
    path('get-contest', contests.getContest),
]