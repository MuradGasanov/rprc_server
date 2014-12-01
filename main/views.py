# -*- coding: utf-8 -*-

import json
import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth import login, logout, authenticate


def log_in(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")

    try:
        data = json.loads(request.body)
    except (TypeError, ValueError):
        return render_to_response("login.html")

    username = data.get("login", "")
    password = data.get("password", "")

    user = authenticate(username=username, password=password)

    if user:
        login(request, user)
        request.session.set_expiry(datetime.timedelta(days=1).seconds)
        if user.is_active:
            return HttpResponse(json.dumps({"error": []}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"error": ["Пользователь заблокирован"]}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error": ["Неверный логин или пароль"]}), content_type="application/json")


def log_out(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required(redirect_field_name=None)
def index(request):
    return render_to_response("index.html")