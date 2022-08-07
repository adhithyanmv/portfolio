from . import views
from django.urls import path


urlpatterns = [
    path("", views.index),
    path("index.html", views.index),
    path("project1", views.project1),
    path("project2", views.project2),
    path("project3", views.project3),
    path("project4", views.project4),
    path("project5", views.project5),
    path("project6", views.project6),
    path("project7", views.project7),
    path("project8", views.project8),
    path("project9", views.project9),
    path("project10", views.project10),
]
