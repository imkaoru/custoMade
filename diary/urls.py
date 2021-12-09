from django.urls import path
from . import views


app_name = "diary"
urlpatterns = [
    path("", views.index, name="index"),
    path("keep_title/", views.keep_title, name="keep_title"),
    path("keep_japanese_translation/", views.keep_japanese_translation, name="keep_japanese_translation"),
    path("keep_own_english_text/", views.keep_own_english_text, name="keep_own_english_text"),
    path("translate_to_english/", views.translate_to_english, name="translate_to_english"),
    path("keep_english_text/", views.keep_english_text, name="keep_english_text"),
    path("my_diary/", views.my_diary, name="my_diary"),
    path('update_check_status/<int:diary_id>/', views.update_check_status, name='update_check_status'),
]