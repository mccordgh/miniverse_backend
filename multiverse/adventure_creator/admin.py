from django.contrib import admin
from adventure_creator import models


# This module registers the project models for the Django admin panel.

@admin.register(models.Adventure, models.Item, models.Interactive, models.Room)

class AdventureAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass

class InteractiveAdmin(admin.ModelAdmin):
    pass

class RoomAdmin(admin.ModelAdmin):
    pass

