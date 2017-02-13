from django.shortcuts import render
from django.utils import timezone
from datetime import datetime, timedelta
import django.contrib.auth as auth #用户登录认证
from app.models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse,JsonResponse,HttpResponseBadRequest,HttpResponseForbidden
import json
from django.conf import settings
import random,string
import  urllib.request,urllib.parse
# import hashlib
from bs4 import BeautifulSoup


# Create your views here.
def repo_list(request):
    res=[]
    repos=Repo.objects.all()
    for repo in repos:
        res.append({
            'id':repo.id,
            'name':repo.name,
            'amount':repo.amount
        })
    return JsonResponse(res,safe=False)



def repo(request,repo_id):
    repo=Repo.objects.get(id=repo_id)
    res={
        'id':repo.id,
        'name':repo.name,
        'amount':repo.amount,
        'words':repo.get_words()
    }
    return JsonResponse(res)


def entry(request,word):
    e=Entry.objects.get(word=word)
    res={
        'word':e.word,
        'level':e.level,
        'definitions':e.get_definitions(),
        'phonetic':e.get_phonetic(),
        'sentences':e.get_sentences()
    }
    return JsonResponse(res)



@require_http_methods(["POST"])
def login(request):
    data = json.loads(request.body.decode())
    user = auth.authenticate(username=data['phone'], password=data['password']) #电话号码当做username来用
    if user is not None:
        # the password verified for the user
        if user.is_active:
            # User is valid, active and authenticated
            auth.login(request, user)
            res = HttpResponse('success')
        else:
            # The password is valid, but the account has been disabled!
            res = HttpResponse('您的账号已被锁定')
    else:
        # the authentication system was unable to verify the username and password
        # The username and password were incorrect.
        res = HttpResponse('用户名或密码错误')
    return res




def logout(request):
    auth.logout(request)
    return HttpResponse('success')


@login_required
def is_logged_in(request):
    # logger.info(request.user.user_info.get())
    return HttpResponse('success')