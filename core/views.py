from django.shortcuts import render, redirect
from .models import Player

def home(request):
    return render(request, 'home.html')

def player_list(request):
    players = Player.objects.all()
    return render(request, 'player_list.html', {'players': players})
def add_player(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        skill_level = request.POST.get('skill_level')

        Player.objects.create(
            name=name,
            email=email,
            skill_level=skill_level
        )

        return redirect('player_list')

    return render(request, 'add_player.html')
def delete_player(request, id):
    player = Player.objects.get(id=id)
    player.delete()
    return redirect('player_list')
def edit_player(request, id):
    player = Player.objects.get(id=id)

    if request.method == 'POST':
        player.name = request.POST.get('name')
        player.email = request.POST.get('email')
        player.skill_level = request.POST.get('skill_level')
        player.save()
        return redirect('player_list')

    return render(request, 'edit_player.html', {'player': player})