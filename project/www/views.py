from django.shortcuts import render,redirect,get_object_or_404
from .forms import ClubsForm,PlayersForm,PositionsForm
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
            return redirect('clubs') 
    else:
        form = ClubsForm()
    
    clubs_list = Club.objects.all()
    return render(request, 'www/clubs.html', {'form': form, 'clubs': clubs_list})

def players(request):
    if request.method == 'POST':
        form = PlayersForm(request.POST, request.FILES)
        if form.is_valid():
            player = form.save()
            selected_club = form.cleaned_data['club']
            selected_position = form.cleaned_data['position']
            return render(request, 'www/players.html', {'players_form': PlayersForm(), 'player': player, 'selected_club': selected_club ,'selected_position':selected_position})    
    else:
        form = PlayersForm()
    return render(request, 'www/players.html', {'players_form': form})



def positions(request):
    if request.method == 'POST':
        form = PositionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('positions')
    else:
        form = PositionsForm()

    return render(request, 'www/positions.html', {'form': form})


def club_detail(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    players = club.player_set.all()
    return render(request, 'www/club_detail.html', {'club': club, 'players': players})
