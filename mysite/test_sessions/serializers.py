from rest_framework import serializers
from .models import Session
class SessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ["Title", "Description", "Candidateid", "CandidateName", "Date", "LocationName", "Latitude", "Longitude"]