from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import DetailView, CreateView, ListView
from django.views.generic.base import View
from .forms import FormReview, FormVote
from .models import Film, Category, Reviews, Genre, Mark, Year


def Contacts(request):
    return render(request, 'uakinotv/contact.html')


class FilmsView(View):
    """Список фільмів"""

    def get(self, request):
        print(request.GET.get('sea'))
        if request.GET.get('sea'):
            films = Film.objects.filter(title__icontains=request.GET.get('sea'))
        else:
            films = Film.objects.all()
        if request.GET.getlist("year"):
            films = films.filter(year__year__in=self.request.GET.getlist("year"))
        if request.GET.getlist("genre"):
            films = films.filter(genres__name__in=self.request.GET.getlist("genre"))
        category = Category.objects.all()
        year = Year.objects.all()
        genre = Genre.objects.all()
        vote = Mark.objects.all()
        return render(request, 'uakinotv/film_first.html', {"film_list": films, "genres": genre, "votes": vote,
                                                            "categories": category, "years": year})


class FilmDetailView(View):
    """Перехід на повне описання фільму"""

    def get(self, request, pk):
        films = Film.objects.get(id=pk)
        views = Reviews.objects.filter(film_id=pk)
        vote = Mark.objects.all()
        return render(request, 'uakinotv/film_detail.html', {"film_desc": films, 'coment': views, "votes": vote})


class FilmCategory(generic.ListView):
    """Переділ по категоріям"""
    model = Film
    template_name = 'uakinotv/film_first.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film_category = Film.objects.filter(category_id=self.kwargs['pk'])
        category = Category.objects.all()
        genre = Genre.objects.all()
        year = Year.objects.all()
        context['categories'] = category
        context['film_list'] = film_category
        context['genres'] = genre
        context['years'] = year
        return context


class AddReview(View):
    """Відгуки"""

    def post(self, request, pk):
        form = FormReview(request.POST)
        film = Film.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.film = film
            form.save()
        return redirect(film.get_absolute_url())


class AddMark(View):

    def post(self,request, pk):
        form = FormVote(request.POST)
        film = Film.objects.get(id=pk)
        if form.is_valid():
            pass
        return redirect(film.get_absolute_url())






