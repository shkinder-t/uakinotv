from django.forms import ModelForm

from .models import Reviews, FilmVotes


class FormReview(ModelForm):
    """Форма для відгуків"""

    class Meta:
        model = Reviews
        fields = ("name", "email", "text")


class FormVote(ModelForm):
    """Форма для оцінки"""

    class Meta:
        model = FilmVotes
        fields = ("mark",)