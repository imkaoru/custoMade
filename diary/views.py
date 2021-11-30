from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    return render(request, "diary/index.html", {
        "newyear": now.month == 11 and now.day ==29
    })
