from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    # test api view
    def get(self, request, format=None):
        # returns list of api features
        an_apiview = [
            'User HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URL\'s',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})