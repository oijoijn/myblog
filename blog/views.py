from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView 

class IndexView(TemplateView):
    """
    動作:home
    """
    template_name = "index.html"

def self_introduction(request):
    return HttpResponse("Hello, world. You're at the polls index.")