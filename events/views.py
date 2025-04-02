from .models import Event
from .serializers import EventSerializer
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.permissions import IsEventOrganizer




class EventView(APIView):
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsEventOrganizer()]
        return [permissions.AllowAny()]
    
    def get(self, request, pk=None):
        """
        Retrieves one or all events
        """
        if pk:
            try:
                event = Event.objects.get(pk=pk)
                serializer = EventSerializer(event)
                return Response(serializer.data)
            except Event.DoesNotExist:
                return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data)

    def post(self, request):
        """
        Create an event
        """
        serializer = EventSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Update specific event
        """
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EventSerializer(event, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """
        Delete a specific event
        """
        try:
            event = Event.objects.get(pk=pk)
            event.delete()
            return Response({'message': 'Event deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
