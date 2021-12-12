from django.db import models
from django.contrib.auth.models import User


class BaseManager(models.Manager):
    def get_or_none(self, **kwargs):
        """
        検索にヒットすればそのモデルを、しなければNoneを返します。
        """
        try:
            return self.get_queryset().get(**kwargs)
        except self.model.DoesNotExist:
            return None


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
    # date = models.DateField(auto_now_add=True)
    date = models.DateField() #開発環境のみ使用 3/3
    title = models.CharField(max_length=255)
    origin_diary = models.TextField()
    japanese_translation = models.TextField()
    own_english_text = models.TextField()
    english_text = models.TextField()
    image = models.ImageField(upload_to='documents/', blank=True, null=True)
    # completed = models.BooleanField(default=False)
    is_completed = models.CharField(max_length=10, default='unchecked')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "date"],
                name="user_date_unique"
            )
        ]

    objects = BaseManager()

    # def __str__(self):
    #     return f"\n日記ID: {self.id}\nユーザーID: {self.user.id}\n日付: {self.date}\nタイトル: {self.title}\n和文: {self.japanese_translation}\n英文: {self.english_text}\n完了かどうか: {self.completed}\n"


class Count(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diaries = models.PositiveIntegerField(default=0)
    completed_diaries = models.PositiveIntegerField(default=0)