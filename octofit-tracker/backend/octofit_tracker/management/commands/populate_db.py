
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear collections using pymongo
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.user.delete_many({})
        db.team.delete_many({})
        db.workout.delete_many({})

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Team')
        dc = Team.objects.create(name='DC', description='DC Team')

        # Create Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel),
            User.objects.create(email='spiderman@marvel.com', name='Spiderman', team=marvel),
            User.objects.create(email='captainamerica@marvel.com', name='Captain America', team=marvel),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc),
            User.objects.create(email='superman@dc.com', name='Superman', team=dc),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team=dc),
        ]

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body strength')
        running = Workout.objects.create(name='Running', description='Cardio')
        yoga = Workout.objects.create(name='Yoga', description='Flexibility')

        # Create Activities
        Activity.objects.create(user=users[0], workout=pushups, date='2023-01-01', duration=30)
        Activity.objects.create(user=users[1], workout=running, date='2023-01-02', duration=45)
        Activity.objects.create(user=users[2], workout=yoga, date='2023-01-03', duration=60)
        Activity.objects.create(user=users[3], workout=pushups, date='2023-01-01', duration=25)
        Activity.objects.create(user=users[4], workout=running, date='2023-01-02', duration=50)
        Activity.objects.create(user=users[5], workout=yoga, date='2023-01-03', duration=55)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=135)
        Leaderboard.objects.create(team=dc, points=130)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
