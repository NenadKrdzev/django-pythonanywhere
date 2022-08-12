from dataclasses import field
from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model=Song
        fields=('title','user','link','body',)

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'}),
            'link':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Song
        fields=('title','link','body',)

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            #'author':forms.Select(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'}),
            'link':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }