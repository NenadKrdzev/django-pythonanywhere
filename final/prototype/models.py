from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=254)
    last_name=models.CharField(max_length=254)
    username=models.CharField(max_length=254)

    def __str__(self):
        return self.first_name+' '+self.last_name+' '+self.username

class Song(models.Model):
    title=models.CharField(max_length=254)
    body=RichTextField(blank=True,null=True)
    #body=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    link=models.URLField()

    def __str__(self):
        return self.title+" "+str(self.author)

    def get_absolute_url(self):
        #return reverse('song_detail',args=(str(self.id)))
        return reverse('home')