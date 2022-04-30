from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def list_workers(request):
    return HttpResponse('Hallo world!!!')