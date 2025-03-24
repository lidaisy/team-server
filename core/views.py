from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *

class ReactView(APIView):
  
    def get_standings(self, request):
        detail = [ {"team": team.name} for team in Standing.objects.all() ]
        return Response(detail)
  
    def get_matches_for_team(self, request):
        current_season = Match.objects.all().filter(season = request.season)
        query = current_season.filter(home_team__icontains = request.club) | current_season.filter(away_team__icontains = request.club)
        detail = [ {"home_team": match.home_team, "away_team": match.away_team, "day": match.match_day, "datetime": match.match_datetime, "home_team_score": match.home_team_score, "away_team_score": match.away_team_score} for match in query ]
        return Response(detail)

