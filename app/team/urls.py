from django.urls import path
from .models import *
from .views import *

urlpatterns = [
    path('', team, name='team')
]
