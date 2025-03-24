from django.contrib import auth
from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import datetime 
from myapp.models import staffs
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import qrcode ,PIL
import os
import random
import json
# Create your views here.
#def index(request):

def login(request):#登入頁面
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name,password=password)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                request.session['username'] = name
                username=str(name)
                count(username)

                if name == 'micheal':
                    return boss(request)
                else:
                    return redirect('/page/')

        else:
            message='帳號密碼錯誤'

    return render(request, 'login.html', locals())

def home(request):#主頁面（未登入）
    now = datetime.now()#時間
  
    return render(request,"home.html",locals())

def post(request):#目前沒用，可以做申辦帳號
    if request.method == "POST":
        cName = request.POST['username']
        
        mess = request.POST['username']

        unit = staffs.objects.create(cName=cName,)
        unit.save()
    
    else :
        mess = '表單未送出'
    return render (request, "home.html",locals() )

def page(request):#QR COde畫面
    now = datetime.now()      
    name=request.session['username']

    data = random.randint(10000,100000)
    img = qrcode.make(data)
    img.save('static/images/myphoto.jpg', 'JPEG')
    return render(request,"page.html",locals())

def boss(request):#老闆畫面
    now = datetime.now()
    name=request.session['username']
    return render(request,"boss.html",locals())

def count(username):
    with open('user_data.json', 'r+') as file:
        data = json.load(file)
        if username in data:
            data[username] += 1
        else:
            data[username] = 1
        file.seek(0)  # 將文件指針移動到文件開頭
        json.dump(data, file)


def info(request):#給老闆看的
    with open('user_data.json','r') as file:
        while True:
           text =file.read()
           return render(request,"info.html",locals())

