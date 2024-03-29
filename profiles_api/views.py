from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """TEST API VIEW"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of API Features"""
        an_apiview = [
            'uses http methods as function (get, post, patch, put, delete)',
            'It is simillar to a traditional Django View',
            'Gives you the most control over your application logic',
            'It is mapped manually to URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

class HelloViewset(viewsets.ViewSet):
    """Test Api viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial update)',
            'Automatically maps to URLS using Routers', 
            'Provides more functionality with less code'
        ]
        
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    def create(self, request):
        """Creates a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else: 
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST

            )
    def retrieve(self, request, pk=None):
        """Handle geting an object by its id"""
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """For removing an object"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewset(viewsets.ModelViewSet):
    """Handle updating and creating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes= (permissions.UpdateOwnStatus,IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile = self.request.user)

class BotViewSet(viewsets.ViewSet):
    serializer_class = serializers.BotSerializer
    def list(self, request):
        """Manages the functions of the bot"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial update)',
            'Automatically maps to URLS using Routers', 
            'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    def create(self, request):
        """Creates a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('firstName')
            message = f'Hello {name}!'
            print(request.data)
            print(message)
            return Response({'message': message})
        else: 
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )