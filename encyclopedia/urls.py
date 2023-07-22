from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.content, name="content"),
    path("addPage/", views.add, name="addPage"),
    path("random/", views.random, name="random"),
    path("search/", views.search, name="search"),
    path("<str:name>/edit", views.edit, name="edit"),
    path("random/<str:name>/edit", views.edit, name="edit"),
    path("search/<str:name>/edit", views.edit, name="edit"),
    path("addPage/<str:name>/edit", views.edit, name="edit")
]

