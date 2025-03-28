from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *

class ReactView(APIView):
  
    def get_standings(self, request):
        query = Club.objects.all().filter(season = request.season).order_by("points")
        detail = [ {"team": team.name} for team in query ]
        return Response(detail)
  
    def get_matches_for_team(self, request):
        current_season = MatchDay.objects.all().filter(season = request.season)
        query = current_season.filter(match__home_team__icontains = request.club) | current_season.filter(match__away_team__icontains = request.club)
        detail = [ {"home_team": match.home_team, "away_team": match.away_team, "datetime": match.match_datetime, "home_team_score": match.home_team_score, "away_team_score": match.away_team_score, "is_live": match.is_live} for match in query ]
        return Response(detail)
  
    def get_matches(self, request):
        current_season = MatchDay.objects.all().filter(season = request.season)
        query = current_season.order_by("match_day")
        detail = [ {"home_team": match.home_team, "away_team": match.away_team, "datetime": match.match_datetime, "home_team_score": match.home_team_score, "away_team_score": match.away_team_score, "is_live": match.is_live} for match in query ]
        return Response(detail)
