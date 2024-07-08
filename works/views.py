import os

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, request

from homework.settings import MEDIA_ROOT
from works.forms import *
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Image


# Create your views here.
def to_register(request):
    return render(request, 'auth/注册.html')


def register(request):
    username = request.POST.get('user_name')
    password = request.POST.get('password')
    result = User.objects.filter(username=username)
    context_value = {"error_Info": "用户名已存在", 'username': username, 'password': password}
    if result:
        return render(request, 'auth/注册.html', context=context_value)
    User.objects.create_user(username=username, password=password)
    return render(request, 'auth/login.html')


def tologin(request):
    """
    跳转登陆界面
    """
    return render(request, 'auth/login.html')


def login(request):
    """登录处理"""
    username = request.POST.get('user_name')
    password = request.POST.get('password')
    context_value = {"error_Info": "用户或密码名错误", 'username': username, 'password': password}
    resUser: User = auth.authenticate(request, username=username, password=password)
    print(resUser, type(resUser))
    if resUser and resUser.is_active:
        # 用户登录成功后（返回给客户端的凭证或者说是令牌，随机字符串
        auth.login(request, resUser)
        form = fileInfoForm()

        context_value = {'title': "文件上传", "form": form}
        return render(request, 'auth/load.html',context=context_value)
    else:
        return render(request, 'auth/login.html', context=context_value)



def upload(request):
        """
        文件上传处理
        """
        # 获取上传文件，如果没有，默认值为None
        # myFile = request.FILES.get('myfile')
        # print(myFile)
        # if myFile:
        #     # 打开特定的文件进行二进制写操作
        #     f = open(os.path.join("E:\\myfile", myFile.name), 'wb+')
        #     # 分块写入文件
        #     for chunk in myFile.chunks():
        #         f.write(chunk)
        #     f.close()
        #     return HttpResponse("文件上传成功")
        # else:
        #     return HttpResponse("没发现文件")

        filename = request.POST.get('filename')
        print(filename)
        file = request.POST.get('file')
        print(request.POST.get("file"))

        form = fileInfoForm()
        if filename and file:
            return render(request,'auth/tophoto.html')
        else:
            return render(request, 'auth/load.html',
                          context={'error_info': "上传失败！不能没有文章名或文章内容", 'form': form})


def toupload(request):
    """跳转文章页面"""
    form = fileInfoForm()

    context_value = {'title': "文件上传", "form": form}
    return render(request, 'auth/load.html', context_value)


def tophotoload(request):
    return render(request,'photoupoload.html')


def loadphoto(request):
    myFile = request.FILES.get('img')
    print(settings.BASE_DIR)
    print(myFile)
    if myFile:
        a=os.path.abspath(__file__)
        print(a)
        file_path=os.path.dirname(a)
        file_path=os.path.join(file_path,'media')
        print(file_path)
        c=os.path.join(file_path,myFile.name)
        d=os.path.join(settings.BASE_DIR/"works/static")
        e=os.path.join(d,myFile.name)
        print(e)
        # 打开特定的文件进行二进制写操作
        f = open(c, 'wb+')
        # 分块写入文件
        for chunk in myFile.chunks():
            f.write(chunk)
        f.close()
        # f = open(d, 'wb+')
        # # 分块写入文件
        # for chunk in myFile.chunks():
        #     f.write(chunk)
        # f.close()
    return render(request, 'view_image.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_view')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def view_image(request):
    images = Image.objects.all()
    return render(request, 'view_image.html', {'images': images})
