from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("hello world")
    return render(request,'website/index.html')


def about(request):
    return HttpResponse("About me")

def contact(request):
    return HttpResponse("contact me")