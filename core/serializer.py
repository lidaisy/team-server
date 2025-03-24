from rest_framework import serializers
from . models import *

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['name']

class StandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standing
        fields = ['name']