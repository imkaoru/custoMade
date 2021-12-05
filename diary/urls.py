from django.urls import path
from . import views


app_name = "diary"
urlpatterns = [
    path("", views.index, name="index"),
    path("my_diary", views.myDiary, name="my_diary"),
    path('update_check_status/<int:diary_id>/', views.update_check_status, name='update_check_status'),
]