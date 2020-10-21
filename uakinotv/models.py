from django.db import models
from datetime import date

from django.urls import reverse


class Genre(models.Model):
    """Жанри фільмів"""
    name = models.CharField("Жанр", max_length=100)
    description = models.TextField("Опис")
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"


class Category(models.Model):
    """Категорії"""
    name = models.CharField("Категорія", max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class ActorPR(models.Model):
    """Актори та режисери"""
    name = models.CharField("Імя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актори і режисери"
        verbose_name_plural = "Актори та режисери"


class Year(models.Model):
    year = models.PositiveSmallIntegerField("Дата виходу", default=date.today)

    def __str__(self):
        return f"{self.year}"


class Film(models.Model):
    """Фільм"""
    title = models.CharField("Назва", max_length=100)
    description = models.TextField("Опис")
    picture = models.ImageField("Картинка", upload_to="films/")
    year = models.ForeignKey(Year, verbose_name="Дата виходу", on_delete=models.CASCADE, default=date.today)
    producer = models.ManyToManyField(ActorPR, verbose_name="Режисер", related_name="film_producer")
    actors = models.ManyToManyField(ActorPR, verbose_name="Актори", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Жанр")
    category = models.ForeignKey(Category, verbose_name="Категорія", on_delete=models.SET_NULL, null=True)
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="Вказати суму у гривнях")
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"

    def get_absolute_url(self):
        return reverse('uakinotv:detail', args=[str(self.id)])


class Reviews(models.Model):
    """Відгуки"""
    email = models.EmailField()
    name = models.CharField("Імя", max_length=100)
    text = models.TextField("Відгук", max_length=100000)
    film = models.ForeignKey(Film, verbose_name="фільм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.film}"

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"


class Mark(models.Model):
    """ Кількість голосів від 1 до 5"""
    mark = models.SmallIntegerField("Оцінка", default=0)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.mark}"

    class Meta:
        verbose_name = "Голос"
        verbose_name_plural = "Голосування"


class FilmVotes(models.Model):
    """Таблиця для кількості голосів"""
    film = models.ForeignKey(Film, verbose_name="фільм", on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark, verbose_name="Оцінка", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.film} - {self.mark}"

    class Meta:
        verbose_name = "Оцінювання"
        verbose_name_plural = "Оцінювання"

