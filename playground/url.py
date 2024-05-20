from django.urls import path
from . import views
from .views import show_popup_form


urlpatterns = [
    path("Home/", views.Home),
    path("Motiv/", views.motivational),
    path("Inspir/", views.inspire),
    path("Funny/", views.funny),
    path("Love/", views.love),
    path('suggest/', show_popup_form, name='show_popup_form'),
    path('movies_list/', views.movie_list, name='movie_list')
]