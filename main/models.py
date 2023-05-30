from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class League(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="league", null=True)
    league_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    promoted_teams = models.IntegerField(default=1)
    relegated_teams = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    league_id = models.ForeignKey(League, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    shorthand = models.CharField(max_length=3)
    points = models.IntegerField(null=False, default=0)
    goals_scored = models.IntegerField(null=False, default=0)
    goals_lost = models.IntegerField(null=False, default=0)
    wins = models.IntegerField(null=False, default=0)
    draws = models.IntegerField(null=False, default=0)
    lost = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    position = models.CharField(max_length=20)
    goals = models.IntegerField(null=False, default=0)
    asists = models.IntegerField(null=False, default=0)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    match_day = models.IntegerField()
    home_team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="hometeam")
    away_team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="awayteam")
    home_team_result = models.IntegerField(null=True, validators=[MinValueValidator(0)])
    away_team_result = models.IntegerField(null=True, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"Match {self.match_id}"

class Scores(models.Model):
    score_id = models.AutoField(primary_key=True)
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="teamid")
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="playerid")

    def __str__(self):
        return f"Score {self.score_id}"
