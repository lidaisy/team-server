from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=30)
    season = models.IntegerField()
    points = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()

class Match(models.Model):
    is_live = models.BooleanField(default=False)
    match_datetime = models.DateTimeField()
    home_team = models.ForeignKey(Club)
    team_team = models.ForeignKey(Club)
    home_team_score = models.IntegerField()
    away_team_score = models.IntegerField()

    def winner(self):
        if self.home_team_score > self.away_team_score:
            return self.home_team
        elif self.home_team_score < self.away_team_score:
            return self.away_team
        else:
            return None


class MatchDay(models.Model):
    season = models.IntegerField()
    match_day = models.IntegerField()
    match = models.ForeignKey(Match)

    class Meta:
        ordering = ["match_day"]