from django import forms
from adventure_creator import models


class CreateAdventureForm(forms.ModelForm):
    title = forms.CharField(max_length=64, help_text="Adventure Title:")

    class Meta:
        model = models.Adventure
        fields = ('title',)

class CreateRoomForm(forms.ModelForm):
    description = forms.CharField(max_length=500, help_text="Room Description:")

    class Meta:
        model = models.Room
        fields = ('description', 'adventure', 'item', 'interactive')

class CreateItemForm(forms.ModelForm):
    name = forms.CharField(max_length=64, help_text="Item Name:")
    description = forms.CharField(max_length=128, help_text="Item Description:")

    class Meta:
        model = models.Item
        fields = ('name', 'description')


class CreateInteractiveForm(forms.ModelForm):
    name = forms.CharField(max_length=64, help_text="Interactive Item Name:")
    description = forms.CharField(max_length=128, help_text="Interactive Item Description:")

    class Meta:
        model = models.Interactive
        fields = ('name', 'description', 'activator')