from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, filters
from .models import Session
from .serializers import SessionsSerializer

class SessionListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ['CandidateName']

    # 1. List all sessions
    def get(self, request, *args, **kwargs):
        '''
        List all the session items for given requested user
        '''
        
        sessions = Session.objects.all().order_by('Date')
        serializer = SessionsSerializer(sessions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)