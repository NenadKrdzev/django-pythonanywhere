from django.contrib import admin

from prototype.models import Author, Song

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display=('username',)

    def has_add_permission(self, request,obj=None):
        return request.user.is_superuser

admin.site.register(Author,AuthorAdmin)

class SongAdmin(admin.ModelAdmin):
    list_display=('title','author',)
    list_filter=('author',)

    def has_add_permission(self, request,obj=None):
        if obj and (request.user==obj.user):
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False
        

admin.site.register(Song,SongAdmin)