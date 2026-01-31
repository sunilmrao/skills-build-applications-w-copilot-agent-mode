from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.assertEqual(team.name, 'Marvel')

    def test_create_user(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(email='batman@dc.com', name='Batman', team=team)
        self.assertEqual(user.team.name, 'DC')

    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body')
        self.assertEqual(workout.name, 'Pushups')

    def test_create_activity(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(email='spiderman@marvel.com', name='Spiderman', team=team)
        workout = Workout.objects.create(name='Running', description='Cardio')
        activity = Activity.objects.create(user=user, workout=workout, date='2023-01-01', duration=30)
        self.assertEqual(activity.user.email, 'spiderman@marvel.com')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
