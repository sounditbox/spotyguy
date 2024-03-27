from django.contrib import admin, messages
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Artist, Release, Song


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'monthly_listeners', 'verified', 'earnings', 'slug')
    list_editable = ('monthly_listeners', 'verified')
    list_display_links = ('name', 'slug')

    def earnings(self, artist: Artist):
        return f'{artist.monthly_listeners * 0.00001:.2f}$ last month'

    @admin.action(description='Verify selected artists')
    def verify(self, request: HttpRequest, qs: QuerySet):
        changed = qs.update(verified=Artist.Status.VERIFIED)
        self.message_user(request, f'{changed} artists verified',
                          level=messages.SUCCESS)

    @admin.action(description='Unverify selected artists')
    def unverify(self, request: HttpRequest, qs: QuerySet):
        changed = qs.update(verified=Artist.Status.UNVERIFIED)
        self.message_user(request, f'{changed} artists unverified',
                          level=messages.SUCCESS)

    actions = [verify, unverify]


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    pass


@admin.register(Song)
class Song(admin.ModelAdmin):
    pass
