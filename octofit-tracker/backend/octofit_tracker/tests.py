from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.workout = Workout.objects.create(name='Pushups', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, type='run', duration=30, team=self.team)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=50)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')

    def test_user_str(self):
        self.assertEqual(self.user.username, 'testuser')

    def test_activity_str(self):
        self.assertIn('testuser', str(self.activity))

    def test_leaderboard_str(self):
        self.assertIn('Test Team', str(self.leaderboard))

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Pushups')
