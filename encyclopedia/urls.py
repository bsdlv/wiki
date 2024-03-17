from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("entry/", views.entry, name="entry"),
    path("random/", views.random, name="random"),
    path("search/", views.search, name="search"),
    path("wiki/<str:q>", views.wiki, name="wiki")
]
