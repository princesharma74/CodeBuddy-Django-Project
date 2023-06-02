from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser): 
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self): 
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # if the Topic were defined below all other models, it should be wrapped in single quotes.
    name = models.CharField(max_length=200)
    # setting null = true means it can be blank. null is for the databases, blank is for the form and saving
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True) # current active people
    updated = models.DateTimeField(auto_now=True) # we will be automatically sets to the time when last updated.
    # the only difference from auto_now is that it gets its value only once the first time when the table was created
    created = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['-updated', '-created'] # - is to set the ordering in descending order, without this, it is automatically set in ascending order

    def __str__(self): 
        return self.name # the only difference from auto_now is that it gets its value only once the first time when the table was created

class Message(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # in place of cascade, you could do SET_NULL to avoid deleting messages when Room is deleted. Cascade means it gets deleted when it is deleted.
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['-updated', '-created'] # - is to set the ordering in descending order, without this, it is automatically set in ascending order

    def __str__(self):
        return self.body[0:50]
    