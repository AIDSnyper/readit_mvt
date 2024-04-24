from django.urls import path
from .models import *
from .views import *

urlpatterns = [
    path('', ArticlesView.as_view(), name='articles'),
    path('singe-blog/<int:pk>', sblog, name='sblog')
]
