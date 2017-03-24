from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, JsonResponse
from adventure_creator import serializers, models
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
import json

class UserViewSet(viewsets.ModelViewSet):
    '''
    The user view shows all users
    '''
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class AdventureViewSet(viewsets.ModelViewSet):
    '''
    The adventure view shows all adventures
    '''
    queryset = models.Adventure.objects.all()
    serializer_class = serializers.AdventureSerializer

class InteractiveViewSet(viewsets.ModelViewSet):
    '''
    The interactive view shows all interactives for an adventure
    '''
    queryset = models.Interactive.objects.all()
    serializer_class = serializers.InteractiveSerializer

class ItemViewSet(viewsets.ModelViewSet):
    '''
    The Item view shows all items for an adventure
    '''
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

class RoomViewSet(viewsets.ModelViewSet):
    '''
    The Room view shows all rooms for an adventure
    '''
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer

def get_adventure(request, pk):
    '''
    The get_adventure view returns all necessary information for an adventure, given the primary key of that adventure
    '''
    adventure = models.Adventure.objects.all().filter(pk=pk).values()
    rooms = models.Room.objects.all().filter(adventure_id=pk).values()
    interactives = models.Interactive.objects.all().values()
    items = models.Item.objects.all().values()
    
    interactives_list = []
    for room in rooms:
        for interactive in interactives:
            if interactive['id'] == room['interactive_id']:
                interactives_list.append(interactive)
            
    items_list = []
    for room in rooms:
        for item in items:
            if item['id'] == room['item_id']:
                items_list.append(item)

    for interactive in interactives_list:
        for item in items:
            if item['id'] == interactive['reward_id']:
                items_list.append(item)
            

    return JsonResponse({
        "adventure": list(adventure),
        "interactives": interactives_list,
        "items": items_list,
        "rooms": list(rooms)
    })

def get_all_adventures(request):
    
    return JsonResponse({
        "adventures": list(models.Adventure.objects.all().values())
        })