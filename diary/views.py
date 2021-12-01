from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

import datetime


# def index(request):
#     now = datetime.datetime.now()
#     return render(request, "diary/index.html", {
#         "newyear": now.month == 1 and now.day == 1
#     })

def index(request):
    return render(request, "diary/index.html")
