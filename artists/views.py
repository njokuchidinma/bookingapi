from .models import ArtistProfile
from .serializers import ArtistProfileSerializer
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.permissions import IsArtist



class ArtistProfileView(APIView):
    
    def get_permissions(self):
        """
        INVOKED CUSTOM PERMISSIONS
        """
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsArtist()]
        return [permissions.AllowAny()]
    
    def get(self, request, pk=None):
        """
        Retrieve one or all artist profiles
        """
        if pk:
            try:
                artist = ArtistProfile.objects.get(pk=pk)
                serializer = ArtistProfileSerializer(artist)
                return Response(serializer.data)
            except ArtistProfile.DoesNotExist:
                return Response({'error': 'Artist Profile was not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            artists = ArtistProfile.objects.all()
            serializer = ArtistProfileSerializer(artists, many=True)
            return Response(serializer.data)

    def post(self, request):
        """
        Create a new artist profile
        """
        serializer = ArtistProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Update an existing artist profile, partial updates allowed too
        """
        try:
            artist = ArtistProfile.objects.get(pk=pk)
        except ArtistProfile.DoesNotExist:
            return Response({'error': 'Artist Profile not found'}, status==status.HTTP_404_NOT_FOUND)

        serializer = ArtistProfileSerializer(artist, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete an artist profile
        """
        try:
            artist = ArtistProfile.objects.get(pk=pk)
            artist.delete()
            return Response({'message': 'Artist Profile deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except ArtistProfile.DoesNotExist:
            return Response({'error': 'Artist Profile not found'}, status=status.HTTP_404_NOT_FOUND)