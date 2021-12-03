from django.urls import path
from . import views

app_name = "diary"
urlpatterns = [
    path("", views.index, name="index"),
    path("my_diary", views.myDiary, name="my_diary"),
]
