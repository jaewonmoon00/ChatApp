from django.shortcuts import render
from rest_framework.views import APIView
from .index import pusher_client
from rest_framework.response import Response


# Create your views here.
class MessageAPIView(APIView):
    def post(self, request):
        #pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
        pusher_client.trigger('chat', 'message', {
            'username': request.data['username'],
            'message': request.data['message'],
        })
        return Response([])