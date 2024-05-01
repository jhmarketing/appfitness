from django import forms
from .models import Playlist

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['nombre', 'q1', 'q2', 'q3', 'q4', 'recharge']