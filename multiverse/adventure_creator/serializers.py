from django.contrib.auth.models import User
from rest_framework import serializers
from adventure_creator import models


class UserSerializer(serializers.ModelSerializer):
    '''
    The User serializer returns a username, and the date joined
    '''

    class Meta:
        model = User
        fields = ('username', 'date_joined')

class AdventureSerializer(serializers.HyperlinkedModelSerializer):
    '''
    The Adventure model serializer returns all fields
    '''

    class Meta:
        model = models.Adventure
        fields = '__all__'

class InteractiveSerializer(serializers.HyperlinkedModelSerializer):
    '''
    The Interactive model serializer returns all fields
    '''

    class Meta:
        model = models.Interactive
        fields = '__all__'

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    '''
    The Item model serializer returns all fields
    '''

    class Meta:
        model = models.Item
        fields = '__all__'

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    '''
    The Room model serializer returns all fields
    '''

    class Meta:
        model = models.Room
        fields = '__all__'

class GetAdventureSerializer(serializers.ModelSerializer):
    '''
    The GetAdventure serializer returns all data needed for the front end logic to run an adventure
    '''

    class Meta:
        model = models.Adventure
        fields = '__all__'