from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from datetime import date, datetime
import requests

from .models import Diary, Count, BaseManager
from .forms import DiaryForm


#################### index.html
# date = date.today()
date = "2021-12-07" #開発環境のみ使用 1/3
diary_step = 1
translate = False


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
    global diary_step
    global translate
    diary = Diary.objects.filter(user=request.user, date=date).first()

    if diary_step > 3 and translate == True:

        # 後ほどユーザーによってAPIキーを分ける処理に変更する
        YOUR_API_KEY = '5ff525e1-0d5f-8846-3081-f374d323b988:fx'

        TEXT = diary.japanese_translation
        params = {
            "auth_key": YOUR_API_KEY,
            "text": TEXT,
            "source_lang": 'JA', # 入力テキストの言語を日本語に設定
            "target_lang": 'EN'  # 出力テキストの言語を英語に設定
        }
        req = requests.post("https://api-free.deepl.com/v2/translate", data=params)
        result = req.json()
        english_text = result["translations"][0]["text"]
        diary.english_text = english_text
        diary.save()

        translate = False

    context = {
        "diary": diary,
        "diary_step": diary_step
    }
    return render(request, "diary/index.html", context)


@login_required
def keep_title(request):
    if (request.method == "POST"):
        global diary_step
        diary_step = 2
        user=request.user

        diary = Diary.objects.get_or_none(user=user, date=date)
        if (not diary == None):
            return redirect('diary:index')

        Diary.objects.create(
            user=user,
            date=date, #開発環境のみ使用 2/3
            title=request.POST.get('title'),
            origin_diary=request.POST.get('origin_diary'),
        )
    return redirect('diary:index')


@login_required
def keep_japanese_translation(request):
    if (request.method == "POST"):
        global diary_step
        diary_step = 3

        Diary.objects.filter(user=request.user, date=date).update(
            title=request.POST.get('title'),
            origin_diary=request.POST.get('origin_diary'),
            japanese_translation=request.POST.get('japanese_translation'),
        )
    return redirect('diary:index')


@login_required
def keep_own_english_text(request):
    if (request.method == "POST"):
        global diary_step
        diary_step = 4

        Diary.objects.filter(user=request.user, date=date).update(
            title=request.POST.get('title'),
            origin_diary=request.POST.get('origin_diary'),
            japanese_translation=request.POST.get('japanese_translation'),
            own_english_text=request.POST.get('own_english_text'),
        )
    return redirect('diary:index')


@login_required
def translate_to_english(request):
    if (request.method == "POST"):
        if 'translate-btn' in request.POST:
            global translate
            translate = True
        else:
            global diary_step
            diary_step = 5

        Diary.objects.filter(user=request.user, date=date).update(
            title=request.POST.get('title'),
            origin_diary=request.POST.get('origin_diary'),
            japanese_translation=request.POST.get('japanese_translation'),
            own_english_text=request.POST.get('own_english_text'),
            english_text=request.POST.get('english_text'),
        )
    return redirect('diary:index')


@login_required
def keep_english_text(request):
    if (request.method == "POST"):
        if 'translate-btn' in request.POST:
            global translate
            translate = True
        else:
            global diary_step
            diary_step = 1

        user=request.user

        diary = Diary.objects.filter(user=user, date=date).first()
        form = DiaryForm(request.POST, request.FILES, instance=diary)
        if form.is_valid():
            form.save()

        Diary.objects.filter(user=user, date=date).update(
            title=request.POST.get('title'),
            origin_diary=request.POST.get('origin_diary'),
            japanese_translation=request.POST.get('japanese_translation'),
            own_english_text=request.POST.get('own_english_text'),
            english_text=request.POST.get('english_text'),
            # image=request.FILES.get('image'),
            # image=request.FILES['image'],
        )

        if not 'translate-btn' in request.POST:
            return redirect('diary:my_diary')
    return redirect('diary:index')
#################### index.html


#################### my_diary.html
sort_state = 0
filter_state = 0


@login_required
def my_diary(request):
    # print(request.user.id)

    # 新規ユーザーのカウントクエリを自動で生成
    if not Count.objects.filter(user=request.user).exists():
        new = Count(user=request.user)
        new.save()

    global sort_state
    global filter_state
    if sort_state == 0 and filter_state == 0:
        diaries = Diary.objects.filter(
            user=request.user,
        ).order_by('date').reverse()
    elif sort_state == 0 and filter_state == 1:
        diaries = Diary.objects.filter(
            user=request.user,
            is_completed="unchecked",
        ).order_by('date').reverse()
    elif sort_state == 1 and filter_state == 0:
        diaries = Diary.objects.filter(
            user=request.user,
        ).order_by('date')
    else:
        diaries = Diary.objects.filter(
            user=request.user,
            is_completed="unchecked",
        ).order_by('date')

    # diaries = Diary.objects.filter(user=request.user)
    count = Count.objects.filter(user=request.user).first()
    count.diaries = Diary.objects.filter(user=request.user).count()
    count.save()

    context = {
        "diaries": diaries,
        "count": count,
        "sort_state": sort_state,
        "filter_state": filter_state,
    }
    return render(request, "diary/my_diary.html", context)


@login_required
def sort_diaries(request):
    global sort_state
    if sort_state == 0:
        sort_state = 1
    else:
        sort_state = 0
    return redirect('diary:my_diary')


@login_required
def filter_diaries(request):
    global filter_state
    if filter_state == 0:
        filter_state = 1
    else:
        filter_state = 0
    return redirect('diary:my_diary')


@login_required
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
        count.completed_diaries = total-1
    diary.save()
    count.save()

    return redirect('diary:my_diary')


# 現状いくつかの問題がある(詳細はGoogleDocument)
@login_required
def diary_edit(request):
    if (request.method == "POST"):
        user=request.user
        # target_date=request.POST.get('date')
        target_date=datetime.strptime(request.POST.get('date'), '%b. %d, %Y') #'Dec. 7, 2021'
        diary = Diary.objects.filter(user=user, date=target_date).first()

        if 'update-btn' in request.POST:
            form = DiaryForm(request.POST, request.FILES, instance=diary)
            if form.is_valid():
                form.save()

            Diary.objects.filter(user=user, date=target_date).update(
                title=request.POST.get('title'),
                english_text=request.POST.get('english_text'),
                japanese_translation=request.POST.get('japanese_translation'),
            )
        else:
            diary.delete()
    return redirect('diary:my_diary')
#################### my_diary.html