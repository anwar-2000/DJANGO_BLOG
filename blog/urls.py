

from django.urls import path
from . import views

urlpatterns = [
    path("", views.startingPage, name="startingPage"),
    path("posts", views.posts , name="postsPage"),
    path("posts/<slug:slug>", views.postDetails, name="postDetails-page")
]
