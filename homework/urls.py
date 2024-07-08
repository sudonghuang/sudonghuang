"""
URL configuration for homework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
import works.views
from works import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 配置媒体文件的路由地址
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    # 跳转注册页面
    path('toRegister/', works.views.to_register, name='toRegister'),
    # 提交注册请求
    path('auth/register', works.views.register, name='register'),
    # 跳转登陆界面
    path('tologin/', works.views.tologin, name='tologin'),
    path('login/', works.views.login, name='login'),

    path('toupload/', works.views.toupload, name='toupload'),
    path('upload/', works.views.upload, name='upload'),

    path('tophoto/', works.views.tophotoload, name='tophoto'),
    path('loadphoto/', works.views.loadphoto, name='loadphoto'),

    path('uploadpic/', works.views.upload_image, name='image_upload'),
    path('view/', works.views.view_image, name='image_view'),
]
