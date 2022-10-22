from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Rating, Category

# Create your views here.
def indexPageView(request):
    return render(request, 'MoviesApp/index.html',)

def showMoviePageView(request, title) :

    context = {
        'movie_title' : title.upper() 
    }
    return render(request, "MoviesApp/show_movie.html", context)

def showInfoPageView(request, title, year) :
    context = {
        'movie_title' : title.upper(),
        'year' : year,
    }
    return render(request, 'MoviesApp/show_info.html', context)

def displayPageView(request) :

    #raw sql statement 
    #sQuery =  'SELECT title, year, rating.description, category.description FROM movie INNER JOIN rating ON rating.id = movie.rating_id INNER JOIN category ON category.id = movie.category_id'

    #runs query and returns data
    #data = Movie.object.raw(sQuery) 

    data = Movie.objects.all()
    ratingLookUp = Rating.objects.all()
    categoryLookUp = Category.objects.all() 

    context = {
        'data' : data,
        'rating' : ratingLookUp,
        'category' : categoryLookUp,
    }
    return render(request, 'MoviesApp/display.html', context)

