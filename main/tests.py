from django.test import TestCase
from main.models import User, League
import views
class LeagueTestCase(TestCase):
    def setUpTestData(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        League.objects.create(name="TestLeague", user=self.user)
        test_league = League.objects.get(name="TestLeague")
        for i in range(16):
            test_league.team_set.create(name="testteam{}".format(i), shorthand="tst", league_id=test_league)
