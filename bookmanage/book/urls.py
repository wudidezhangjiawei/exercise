from django.urls import path
from  book.views import index,goods
urlpatterns = [
    path('index/',index),
    path('<cat__id>/<goods__id>/',goods)
]