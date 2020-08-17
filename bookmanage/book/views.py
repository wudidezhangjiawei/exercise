from django.shortcuts import render
from  django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return HttpResponse('ok')
def goods(request,cat__id,goods__id):
    return JsonResponse({'cat__id':cat__id,'goods__id':goods__id})
