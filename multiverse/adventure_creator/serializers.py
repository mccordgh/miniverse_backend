from django.contrib.auth.models import User
from rest_framework import serializers
from adventure_creator import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'date_joined')

class AdventureSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Adventure
        fields = '__all__'

class InteractiveSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Interactive
        fields = '__all__'

class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Item
        fields = '__all__'

class RoomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Room
        fields = '__all__'

class GetAdventureSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Adventure
        fields = '__all__'