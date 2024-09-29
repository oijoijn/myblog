from django.shortcuts import render
from django.http import HttpResponse


def self_introduction(request):
    return HttpResponse("Hello, world. You're at the polls index.")