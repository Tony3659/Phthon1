from django.shortcuts import render
from django.http import HttpResponse  #我印到網頁的程序 將它import進來



def index(request):                             #()中是變數                         
    return HttpResponse("~~")         #每當有人呼叫index就讓它回應("")中的東西