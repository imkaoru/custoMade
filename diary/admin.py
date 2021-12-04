from django.contrib import admin
from .models import User, Diary, Count


# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display = ("id", "nickname", "password", "diaries", "completed_diaries")


class DiaryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date", "title", "japanese_translation", "english_text", "image", "completed")

class CountAdmin(admin.ModelAdmin):
    list_display = ("id", "diaries", "completed_diaries")



# admin.site.register(User, UserAdmin)
admin.site.register(Diary, DiaryAdmin)
admin.site.register(Count, CountAdmin)