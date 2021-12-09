from django.contrib import admin
from .models import User, Diary, Count


# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display = ("id", "nickname", "password", "diaries", "completed_diaries")


class DiaryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date", "title", "origin_diary", "japanese_translation", "own_english_text", "english_text", "image", "is_completed")


class CountAdmin(admin.ModelAdmin):
    list_display = ("id", "diaries", "completed_diaries")


# admin.site.register(User, UserAdmin)
admin.site.register(Diary, DiaryAdmin)
admin.site.register(Count, CountAdmin)