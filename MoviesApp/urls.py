from django.urls import path
from .views import indexPageView, showMoviePageView, showInfoPageView, displayPageView

urlpatterns = [
    path("movie/<str:title>/", showMoviePageView, name = "show_movie"),
    #path("movie/", showMoviePageView, name = "show_movie"),
    path("info/<str:title>/<int:year>", showInfoPageView, name="show_info"),
    path("display/", displayPageView, name="display"),
    path("", indexPageView, name="index"),
]
