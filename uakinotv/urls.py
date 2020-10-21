from django.urls import path
from . import views

app_name = "uakinotv"

urlpatterns = [
    path('', views.FilmsView.as_view(), name='first_page'),
    path('<int:pk>/', views.FilmDetailView.as_view(), name='detail'),
    path('category/<int:pk>/', views.FilmCategory.as_view(), name='category'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='review'),
    path('vote/<int:pk>/', views.AddMark.as_view(), name='vote'),
    path('contacts/', views.Contacts, name='contacts')
]
