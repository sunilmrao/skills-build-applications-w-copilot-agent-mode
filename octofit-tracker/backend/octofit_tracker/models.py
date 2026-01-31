

from djongo import models
from bson import ObjectId

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False, default=ObjectId)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False, default=ObjectId)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')
    def __str__(self):
        return self.email

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False, default=ObjectId)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False, default=ObjectId)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    def __str__(self):
        return f"{self.user.email} - {self.workout.name} on {self.date}"

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False, default=ObjectId)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.team.name}: {self.points} pts"
