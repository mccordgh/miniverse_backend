from django.db import models
from django.contrib.auth.models import User

class Adventure(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    rating = models.IntegerField()
    published = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.title)

class Item(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

    def __str__(self):
        return '{}'.format(self.name)

class Interactive(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    action = models.CharField(max_length=32)
    activator = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='activator_item', null=True)
    reward = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='rewarded_item', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

class Room(models.Model):
    room_number = models.IntegerField()
    description = models.CharField(max_length=512)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    item = models.OneToOneField(Item, on_delete=models.CASCADE, blank=True, null=True)
    interactive = models.OneToOneField(Interactive, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return 'Room #{} from {}'.format(self.room_number, self.adventure)

