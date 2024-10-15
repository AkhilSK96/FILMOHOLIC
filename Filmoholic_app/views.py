from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from Filmoholic_app.models import Movies, Others 
from Filmoholic_app.models import filmbuzz
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from .forms import UserForm
from .forms import MovieForm


def Homemain(request):
    return render(request,"Home1.html")

def Discover(request):
    movies = Movies.objects.all()
    return render(request, 'discover.html', {'movies': movies})

def movies_by_genre(request):
    genre = request.GET.get('genre', None)
    if genre:
        # Filter movies by the selected genre
        movies = Movie.objects.filter(genre=genre)
    else:
        # No genre selected, return all movies
        movies = Movie.objects.all()
    
    return render(request, 'index.html', {'movies': movies})

def add_movies(request):
    return render(request, 'add_movies.html')

def favorites(request):
    return render(request, 'favorites.html')

def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('signup_success')  
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})



def movie_detail(request, movie_title):
    # Logic to fetch movie details based on 'movie_title'
    # Example: Fetch movie details from a database or use hardcoded data
    movie_details = {
        'title': movie_title,
        'description': 'Movie description goes here...',
        'cast': ['Actor 1', 'Actor 2', 'Actor 3'],
        # Other movie details...
    }
    return render(request, 'movie_detail.html', {'movie': movie_details})

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('signup_success')  
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

def signup_success(request):
    return render(request, 'signup_success.html')


def view_movies(request):
    movies = Movies.objects.all()
    return render(request, 'discover.html', {'movies': movies})
def signed_in(request):
    user = User.objects.all()
    return render(request, 'signed_in.html',{'user':user})

def filmbuzz_view(request):
    filmbuzz_items = filmbuzz.objects.all()
    return render(request, 'filmbuzz.html', {'filmbuzz_items': filmbuzz_items})

def upcoming(request):
    return render(request, 'upcoming.html')

def others(request):
    others = Others.objects.all()
    return render(request, 'Others.html', {'others': others})