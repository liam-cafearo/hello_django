# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

"""
We would normally only have one or two functions in a view that reflects the purpose of the app.
For learning purposes I have left the other functions(views) in to compare and contrast the syntax and purpose of each
as they did in the lesson code.
"""


def say_hello(request):
    name = "Bootcamper"
    html = "<html><body><h1>Hello %s!</h1></body></html>" % name
    return HttpResponse(html)


def get_now(request):
    now = datetime.datetime.now()
    return render(request, "HelloWorld/base.html", {"current_date": now})


def inheritance_test(request):
    return render(request, "HelloWorld/home.html",
                  {"a_variable": "I've been rendered in the child template",
                   "another_variable": "me too!"})
