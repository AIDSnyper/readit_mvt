from django.shortcuts import render

from articles.models import Articles
from .models import *


def team(request):
    model = User.objects.all()
    ctx = {'model': model,
           'footer': Articles.objects.all()[:2]
           }
    return render(request, 'about.html', ctx)
