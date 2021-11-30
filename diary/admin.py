from django.contrib import admin
from .models import User, Diary

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "nickname", "password", "diaries", "completed_diaries")

class DiaryAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "date", "title", "japanese_translation", "english_text", "image", "completed")

admin.site.register(User, UserAdmin)
admin.site.register(Diary, DiaryAdmin)