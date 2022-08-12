"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from prototype.views import DeleteSongView, EditSongView,HomeView,SongDetailView,AddSongView


urlpatterns = [
    #path('admin/', admin.site.urls),
   # path('add/',add,name='add'),
   # path('home/',home,name='home'),
   # path('edit/',edit,name='edit'),
    path('',HomeView.as_view(),name='home'),
    path('song/<int:pk>',SongDetailView.as_view(),name='song_detail'),
    path('add/',AddSongView.as_view(),name='add'),
    path('song/edit/<int:pk>',EditSongView.as_view(),name='edit'),
    path('song/<int:pk>/delete',DeleteSongView.as_view(),name='delete'),
    
]
