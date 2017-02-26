from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Adventure(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)

    def __str__(self):
        return '{}'.format(self.title)

class Exit(models.Model):
    direction = models.CharField(max_length=1)

    def __str__(self):
        return '{}'.format(self.direction)

class Item(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)

    def __str__(self):
        return '{}'.format(self.name)


class Interactive(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    action = models.CharField(max_length=32)
    activator = models.OneToOneField(Item, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

class Room(models.Model):
    description = models.CharField(max_length=500)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    interactive = models.OneToOneField(Interactive, on_delete=models.CASCADE)
    exit = models.ManyToManyField(Exit)

    def __str__(self):
        return 'ROOM __str__'


