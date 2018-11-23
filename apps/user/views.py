from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponse

from user.models import User
from utils.fdfs.storage import FDFSStorage

# Create your views here.
from django.contrib.auth.hashers import check_password, make_password
import re


def img_upload(request):
    return render(request, 'img_upload.html')


def img_handle(request):
    f1 = request.FILES.get('img')
    fdfs = FDFSStorage()
    return HttpResponse(fdfs.save(f1.name, f1))

class RegisterView(View):

    def get(self, request):

        return render(request, 'register.html')

    def post(self, request):

        user_name = request.POST.get("user_name")
        password = request.POST.get("pwd")
        email = request.POST.get("email")

        if not all([user_name, password, email]):
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

        try:
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            user = None

        if user:
            return render(request, 'register.html', {'errmsg': '用户名已存在'})

        # 直接注册成功不发送验证邮件信息，后期有需求再做
        user = User.objects.create_user(user_name, password, email)
        user.password = make_password(password)
        user.is_active = 1
        user.save()

        return redirect(reverse('group:group'))


class LoginView(View):

    def get(self, request):

        return render(request, 'login.html')


class LogoutView(View):

    def get(self, request):
        pass