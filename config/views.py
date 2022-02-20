
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from start.models import *

def home(request):
    print(request.user)
    return render(request, "main/index.html", {})
