from django.urls import path
from . import views

urlpatterns = [
    path('',views.Homemain,name='Home'),
    path('movies_by_genre/', views.movies_by_genre, name='movies_by_genre'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('movie/<str:movie_title>/', views.movie_detail, name='movie_detail'),
    path('signup_success', views.signup_success, name='signup_success'),
    path('discover',views.Discover, name="Discover"),
    path('movies/', views.view_movies, name='view_movies'),
    path('signed_in/', views.signed_in, name='signed_in'),
    path('filmbuzz/', views.filmbuzz_view, name='filmbuzz'),
    path('upcoming/', views.upcoming, name='upcoming'),
    path('Others/', views.others, name='Others'),
]
