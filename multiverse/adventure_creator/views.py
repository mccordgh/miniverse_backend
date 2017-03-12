from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, JsonResponse
from adventure_creator import serializers, models
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
import json

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class AdventureViewSet(viewsets.ModelViewSet):
    queryset = models.Adventure.objects.all()
    serializer_class = serializers.AdventureSerializer

class GetAdventureViewSet(viewsets.ModelViewSet):
    queryset = models.Adventure.objects.all() 
    serializer_class = serializers.AdventureSerializer

class InteractiveViewSet(viewsets.ModelViewSet):
    queryset = models.Interactive.objects.all()
    serializer_class = serializers.InteractiveSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer

class LoginView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)


    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended",
    }

    def _error_response(self, message_key):
        data = json.dumps({
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        })

    def post(self,request):
        req_body = json.loads(request.body.decode())
        username = req_body['username']
        password = req_body['password']
        user = authenticate(username=username, password=password)

        success = False
        if user is not None:
            if user.is_active:
                login(request, user)
                data = json.dumps({
                    'success': True,
                    'username': user.username,
                    'email': user.email,
                })
                return HttpResponse(data, content_type='application/json')

            return HttpResponse(self._error_response('disabled'), content_type='application/json')
        return HttpResponse(self._error_response('invalid'), content_type='application/json')

def get_adventure(request, pk):
    adventure = models.Adventure.objects.all().values()
    interactives = models.Interactive.objects.all().values()
    items = models.Item.objects.all().values()
    rooms = models.Room.objects.all().values()

    return JsonResponse({
        "adventure": list(adventure),
        "interactives": list(interactives),
        "items": list(items),
        "rooms": list(rooms)
    })
