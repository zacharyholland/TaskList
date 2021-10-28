from django.urls import path
from .views import indexPageView, aboutPageView, seeTaskPageView, createTaskPageView, editTaskPageView, deleteTaskPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    path("list/", seeTaskPageView, name="list"),
    path("create/", createTaskPageView, name="create"),
    path("edit/", editTaskPageView, name="edit"),
    path("delete/", deleteTaskPageView, name="delete"),
]