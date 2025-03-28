"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from myapp.views import login, home
from django.urls import include, path ,URLPattern
from myapp import views
from django.conf.urls.static import static


urlpatterns = [
    
    #主要
    path('admin/', admin.site.urls),#管理後台
    path('page/',views.page), #已經登入頁面
    path('login/',views.login),#未登入頁面
    path('',views.home),#初始頁面
    path('boss/',views.boss),#老闆頁面
    path('info/',views.info),#資料
    path('post/',views.post),#post傳送表單
    
] 
