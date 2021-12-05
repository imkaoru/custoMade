from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
#     nickname = models.CharField(max_length=64, unique=True)
#     password = models.SlugField()
#     diaries = models.PositiveIntegerField(default=0)
#     completed_diaries = models.PositiveIntegerField(default=0)

    # def __str__(self):
    #     return f"\nユーザーID: {self.id}\nニックネーム: {self.nickname}\n日記数: {self.diaries}\n学習済みの日記数: {self.completed_diaries}\n"


class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    japanese_translation = models.TextField()
    english_text = models.TextField()
    image = models.ImageField(blank=True, upload_to='documents/')
    # completed = models.BooleanField(default=False)
    is_completed = models.CharField(max_length=10, default='unchecked')

    # def __str__(self):
    #     return f"\n日記ID: {self.id}\nユーザーID: {self.user.id}\n日付: {self.date}\nタイトル: {self.title}\n和文: {self.japanese_translation}\n英文: {self.english_text}\n完了かどうか: {self.completed}\n"


class Count(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diaries = models.PositiveIntegerField(default=0)
    completed_diaries = models.PositiveIntegerField(default=0)


# class Document(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     photo = models.ImageField(upload_to='documents/', default='defo')
