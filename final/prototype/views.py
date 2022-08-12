import imp
from typing import List
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Song
from .forms import SongForm,EditForm
from django.urls import reverse_lazy

# Create your views here.
#def home(request):
#    queryset=Song.objects.all()
 #   context={"songs":queryset,}
 #  return render(request,'home.html',context=context)

class HomeView(ListView):
    model=Song
    template_name='home.html'
    ordering=['-id']

class SongDetailView(DetailView):
    model=Song
    template_name='song_details.html'

class AddSongView(CreateView):
    model=Song
    form_class=SongForm
    template_name='add.html'
    #fields='__all__'
    #fields=('title','body','author','link',)


class EditSongView(UpdateView):
    model=Song
    form_class=EditForm
    template_name='edit.html'
   # fields=['title','body','link']

class DeleteSongView(DeleteView):
    model=Song
    template_name='delete.html'
    success_url=reverse_lazy('home')