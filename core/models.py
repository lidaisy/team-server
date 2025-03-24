from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

class Standing(models.Model):
    number = models.IntegerField()
    team = models.ForeignKey(Club)
    
    class Meta:
        ordering = ["number"]

class Match(models.Model):
    season = models.IntegerField()
    match_datetime = models.DateTimeField()
    match_day = models.IntegerField()
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
        
    class Meta:
        ordering = ["match_day"]
