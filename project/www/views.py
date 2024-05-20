from django.shortcuts import render,redirect
from .forms import ClubsForm,PlayersForm,PositonsForm
from .models import Club,Player,Position



def index(request):
    clubs_list = Club.objects.all()
    players_list = Player.objects.all()
    positions_list = Position.objects.all()
    return render(request, 'www/index.html', {'clubs': clubs_list, 'players': players_list, 'positions': positions_list})




def clubs(request):
    if request.method == 'POST':
        form = ClubsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clubs')  # Redirect to the same page to display the updated list
    else:
        form = ClubsForm()
    
    clubs_list = Club.objects.all()
    return render(request, 'www/clubs.html', {'form': form, 'clubs': clubs_list})

def players(request):
    if request.method == 'POST':
        form = PlayersForm(request.POST, request.FILES)
        if form.is_valid():
            player = form.save()
            selected_club = form.club.all().values_list('name', flat=True)
            selected_position = form.club.all().values_list('name', flat=True)
            return render(request, 'www/index.html', {'player_form': PlayersForm(), 'player': player, 'selected_club': selected_club ,'selected_position':selected_position})    
    else:
        form = PlayersForm()
    return render(request, 'www/players.html', {'players_form': form})


def positions(request):
    if request.method == 'POST':
        form = PositonsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('positions')  # Redirect to the same page to display the updated list
    else:
        form = PositonsForm()
    return render(request, 'www/positions.html', {'form':form})