from django.contrib import admin

from .models import Artist, Release, Song


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'monthly_listeners', 'slug')
    list_editable = ('monthly_listeners',)
    list_display_links = ('name', 'slug')

@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    pass


@admin.register(Song)
class Song(admin.ModelAdmin):
    pass
