from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """TEST API VIEW"""
    def get(self, request, format=None):
        """Returns a list of API Features"""
        an_apiview = [
            'uses http methods as function (get, post, patch, put, delete)',
            'It is simillar to a traditional Django View',
            'Gives you the most control over your application logic',
            'It is mapped manually to URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})