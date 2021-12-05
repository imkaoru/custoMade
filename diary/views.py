from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import datetime

from diary.models import Diary, Count



# def index(request):
#     now = datetime.datetime.now()
#     return render(request, "diary/index.html", {
#         "newyear": now.month == 1 and now.day == 1
#     })


# @login_required
# def testview(request):
#     user = request.user


@login_required
def index(request):
    return render(request, "diary/index.html")


@login_required
def myDiary(request):
    # print(request.user.id)
    # login_user = request.user
    # print(login_user)

    # 以下、新規登録機能これからなので未確認
    if not Count.objects.filter(user=request.user).exists():
        new = Count(user=request.user)
        new.save()

    diaries = Diary.objects.filter(user=request.user)
    count = Count.objects.filter(user=request.user).first()
    count.diaries = diaries.count()
    count.save()

    context = {
        "login_user": request.user,
        "diaries": diaries,
        "count": count
    }
    return render(request, "diary/my_diary.html", context)


def update_check_status(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    count = Count.objects.filter(user=request.user).first()
    total = Diary.objects.filter(
            user=request.user,
            is_completed="checked"
            ).count()

    if diary.is_completed == "unchecked":
        diary.is_completed = "checked"
        count.completed_diaries = total+1
    else:
        diary.is_completed = "unchecked"
        count.completed_diaries = total+1
    diary.save()
    count.save()

    return redirect('diary:my_diary')