from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, filters
from .models import Session
from .serializers import SessionsSerializer

class SessionListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['Date']
    ordering = ['Date']

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        sessions = Session.objects.all()
        serializer = SessionsSerializer(sessions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)