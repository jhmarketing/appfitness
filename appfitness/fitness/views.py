from django.shortcuts import render, redirect, get_object_or_404
from .models import Playlist
from .forms import PlaylistForm
# Create your views here.
from .models import Categoria, Cancion

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {'categorias': categorias})

def lista_canciones(request, categoria_id):
    canciones = Cancion.objects.filter(categoria_id=categoria_id)
    return render(request, 'lista_canciones.html', {'canciones': canciones})
def agregar_playlist(request):
    if request.method == "POST":
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save()
            return redirect('playlist/{0}'.format(playlist.id))
        else:
            form = PlaylistForm()
        return render(request, 'crear_playlist.html', {'form': form})
def ver_playlist(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    return render(request, 'playlist.html', {'playlist':playlist})
