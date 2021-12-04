from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import datetime

from diary.models import Diary



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
    login_user = request.user
    # print(login_user)
    diaries = Diary.objects.all()
    context = {
        "login_user": login_user,
        "diaries": diaries
    }
    return render(request, "diary/my_diary.html", context)
