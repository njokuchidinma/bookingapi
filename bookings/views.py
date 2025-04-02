from .models import Booking
from .serializers import BookingSerializer
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.tasks import payment_processing





class BookingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk=None):
        """
        Retrieve a specific booking or list all bookings for the user
        """
        if pk:
            try:
                booking = Booking.objects.get(pk=pk, user=request.user)
                serializers = BookingSerializer(booking)
                return Response(serializers.data)
            except Booking.DoesNotExist:
                return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            bookings = Booking.objects.filter(user=request.user)
            serializers = BookingSerializer(bookings, many=True)
            return Response(serializers.data)

    def post(self, request):
        """
        Creates a new booking and trigger background payment processing
        """
        serializers = BookingSerializer(data=request.data, context={'request': request})
        if serializers.is_valid():
            booking = serializers.save()
            payment_processing.delay(booking.id)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Updates bookings fully and partially
        """
        try:
            booking = Booking.objects.get(pk=pk, user=request.user)
        except Booking.DoesNotExist:
            return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializers = BookingSerializer(booking, data=request.data, partial=True, context={'request': request})
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Cancel a specific booking
        """
        try: 
            booking = Booking.objects.get(pk=pk, user=request.user)
            booking.delete()
            return Response({'message': 'Booking cancelled successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Booking.DoesNotExist:
            return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)

        

