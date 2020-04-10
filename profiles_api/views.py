from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    # test api view
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        # returns list of api features
        an_apiview = [
            'User HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URL\'s',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})


    def post(self,request):
        """create a hello message with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})
        

    def patch(self,request,pk=None):
        # handles partial updating an object
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        # to delete objects
        return Response({'method': 'DELETE'})