from django.shortcuts import render
from  django.http import HttpResponse,JsonResponse
import json

# Create your views here.
def index(request):
    return HttpResponse('ok')
def goods(request,cat__id,goods__id):
    return JsonResponse({'cat__id':cat__id,'goods__id':goods__id})
def get(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)
    print(b)
    print(alist)
    return  HttpResponse("ojbk")
def post(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')
    print(a)
    print(b)
    print(alist)
    return  HttpResponse("ojbk")
def post_json(request):
    json_str = request.body
    json_str = json_str.decode()
    req_data = json.loads(json_str)
    print(req_data['a'])
    print(req_data['b'])
    return  HttpResponse('ok')
