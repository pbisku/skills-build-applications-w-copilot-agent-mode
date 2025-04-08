from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thunder God', age=25, team='Blue Team'),
            User(email='metalgeek@mhigh.edu', name='Metal Geek', age=22, team='Blue Team'),
            User(email='zerocool@mhigh.edu', name='Zero Cool', age=20, team='Gold Team'),
            User(email='crashoverride@mhigh.edu', name='Crash Override', age=23, team='Gold Team'),
            User(email='sleeptoken@mhigh.edu', name='Sleep Token', age=21, team='Blue Team'),
        ]
        # Ensure users are saved and retrieved as Django model instances
        User.objects.bulk_create(users)
        users = list(User.objects.all())  # Retrieve saved users as Django model instances

        # Create teams
        teams = [
            Team(name='Blue Team'),
            Team(name='Gold Team')
        ]
        # Save teams to the database and retrieve them
        Team.objects.bulk_create(teams)
        teams = list(Team.objects.all())  # Retrieve saved teams as Django model instances

        # Assign users to teams after saving teams
        teams[0].save()
        teams[0].members.set(users[:3])  # Assign first three users to Blue Team
        teams[1].save()
        teams[1].members.set(users[3:])  # Assign remaining users to Gold Team

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(user=users[1], activity_type='Crossfit', duration=timedelta(hours=2)),
            Activity(user=users[2], activity_type='Running', duration=timedelta(hours=1, minutes=30)),
            Activity(user=users[3], activity_type='Strength', duration=timedelta(minutes=30)),
            Activity(user=users[4], activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0], points=100),
            Leaderboard(user=users[1], points=90),
            Leaderboard(user=users[2], points=95),
            Leaderboard(user=users[3], points=85),
            Leaderboard(user=users[4], points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(name='Running Training', description='Training for a marathon', duration=90),
            Workout(name='Strength Training', description='Training for strength', duration=30),
            Workout(name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
