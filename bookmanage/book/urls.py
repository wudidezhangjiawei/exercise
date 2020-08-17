from django.urls import path
from  book.views import index,goods,get,post,post_json
urlpatterns = [
    path('index/',index),
    path('<cat__id>/<goods__id>/',goods),
    path('get/',get),
    path('post/',post),
    path('post_json/',post_json)
]
