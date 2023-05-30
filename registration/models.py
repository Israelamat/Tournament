from django.db import models

class League(models.Model):
    league_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)
    league_id = models.ForeignKey(League, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    shorthand = models.CharField(max_length=3)
    points = models.IntegerField(null=False, default=0)

class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    position = models.CharField(max_length=20)