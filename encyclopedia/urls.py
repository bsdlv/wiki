from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("new_page/", views.new_page, name="new_page"),
    path("random_page/", views.random_page, name="random_page"),
    path("search/", views.search, name="search"),
    path("wiki/<str:q>", views.wiki, name="wiki")
]
