from django.contrib import admin
from adventure_creator import models

@admin.register(models.Adventure, models.Exit, models.Item, models.Interactive, models.Room)

class AdventureAdmin(admin.ModelAdmin):
    pass

class ExitAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass

class InteractiveAdmin(admin.ModelAdmin):
    pass

class RoomAdmin(admin.ModelAdmin):
    pass

