

from django.urls import path
from . import views

urlpatterns = [
    path("", views.startingPage.as_view(), name="startingPage"),
    path("posts", views.posts.as_view() , name="postsPage"),
    path("posts/<slug:slug>", views.postDetails.as_view(), name="postDetails-page")
]
