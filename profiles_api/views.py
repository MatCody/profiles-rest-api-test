from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of API View features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!','an_apiview': an_apiview})

    def post(self, request):
        '''Create a hello message with our name'''
        serializer = self.serializer_class(data=request.data)
    
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} !'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    # THE DJANGO REST FRAMEWORK serializers PROVIDES THE FUNCTIONALITY TO VALIDATE
    # THE INPUT, SO THAT'S INSURING THAT THE INPUT IS VALID AS PER SPECIFICATION OF OURS
    # SERIALIZERS FIELD, OUR CASE -> the name no longer than 10 characters 

    '''the pk take the ID of the object that we want to update on our request'''
    def put(self, request, pk=None):
        '''Handle updating an object'''
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        '''if we want to update but maintain the past information'''
        '''Handle a partial update of an object'''
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        '''Delete an object'''
        return Response({'method':'DELETE'})