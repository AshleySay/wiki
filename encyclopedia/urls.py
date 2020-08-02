from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("newpage.html", views.newpage, name="newpage"),
    path("edit", views.edit, name="edit"),
    path("randompage", views.randompage, name="randompage"),
    path("error", views.error, name="error")
]
