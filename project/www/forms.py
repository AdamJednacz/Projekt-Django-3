from django import forms

from .models import Club,Player,Position

class ClubsForm(forms.ModelForm):
    name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Date'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'Choose a photo'}))

    class Meta:
        model = Club
        fields = '__all__'


class PlayersForm(forms.ModelForm):
    name =  forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    surname =  forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    age = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Age'}))
    club = forms.ModelMultipleChoiceField(queryset=Club.objects.all())
    position = forms.ModelMultipleChoiceField(queryset=Position.objects.all())
    photo = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'Choose a photo'}))

    class Meta:
        model = Player
        fields = '__all__'        



class PositonsForm(forms.ModelForm):
    name =  forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    class Meta:
        model = Position
        fields = '__all__'        