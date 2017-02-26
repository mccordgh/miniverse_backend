from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from adventure_creator import forms

# Base view for /
def index_view(request):
    # Auto logging in my superuser for coding purposes!!
    user = authenticate(
        username='matthew',
        password='pass1234'
    )

    # Check if user authenticated
    if user is not None:
        login(request=request, user=user)
        return render(request, 'adventure_creator/home.html', {'username': user})
    else:
        return HttpResponse('invalid user')

# view for creating an adventure using create_adventure.html template
def create_adventure_view(request):
    form = forms.CreateAdventureForm()

    if request.method == 'POST':
        form = forms.CreateAdventureForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            form = forms.CreateRoomForm()
            return render(request, 'adventure_creator/create_room.html', {
                'username': request.user,
                'form': form
                })
        else:
            print(form.errors)
    return render(request, 'adventure_creator/create_adventure.html', {
        'username': request.user,
        'form': form
        })

# view for creating all the rooms in an adventure
def create_room_view(request):
    form = forms.CreateRoomForm()

    if request.method == 'POST':
        form = forms.CreateRoomForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            info = "Room saved to Adventure"
            form = forms.CreateRoomForm()
            return render(request, 'adventure_creator/create_room.html', {
                'username': request.user,
                'form': form,
                'info': info
                })
        else:
            print(form.errors)
    return render(request, 'adventure_creator/create_room.html', {'username': request.user})

# view for creating items to use in your rooms
def create_item_view(request):
    form = forms.CreateItemForm()

    if request.method == 'POST':
        form = forms.CreateItemForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            info = "Item saved to database"
            form = forms.CreateItemForm()
            return render(request, 'adventure_creator/create_item.html', {
                'username': request.user,
                'form': form,
                'info': info
                })
        else:
            print(form.errors)
    return render(request, 'adventure_creator/create_item.html', {
                'username': request.user,
                'form': form
                })

# view for creating interactives to use in your rooms
def create_interactive_view(request):
    form = forms.CreateInteractiveForm()

    if request.method == 'POST':
        form = forms.CreateInteractiveForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            info = "interactive saved to database"
            form = forms.CreateInteractiveForm()
            return render(request, 'adventure_creator/create_interactive.html', {
                'username': request.user,
                'form': form,
                'info': info
                })
        else:
            print(form.errors)
    return render(request, 'adventure_creator/create_interactive.html', {
                'username': request.user,
                'form': form
                })

# view for listing all adventures of current user
def adventures_view(request):
    return render(request, 'adventure_creator/view_my_adventures.html', {'username': request.user})

