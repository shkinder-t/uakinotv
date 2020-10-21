from django.contrib import admin
from .models import Genre, ActorPR, Film, Reviews, Category, Mark, FilmVotes, Year
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class FilmAdminForm(forms.ModelForm):
    description = forms.CharField(label='Опис', widget=CKEditorUploadingWidget())

    class Meta:
        model = Film
        fields = '__all__'


class GengeAd(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "description")
    list_display_links = ("name",)


@admin.register(Film)
class FilmAd(admin.ModelAdmin):
    list_display = ("id", "title", "category","slug")
    list_display_links = ("title",)
    search_fields = ("category__name", "title",)
    list_filter = ("year",)
    form = FilmAdminForm


admin.site.register(Genre, GengeAd)
admin.site.register(ActorPR)
admin.site.register(Reviews)
admin.site.register(Category)
admin.site.register(Mark)
admin.site.register(FilmVotes)
admin.site.register(Year)