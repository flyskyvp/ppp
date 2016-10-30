#coding=utf-8
from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from blog.models import User
from blog.models import BlogsPost


# Create your views here.
def index(request):
    blog_list = BlogsPost.objects.all()
    # for i in blog_list:
        # print i.title
        # print i.timestamp
    return render_to_response('index.html',{'blog_list':blog_list})

#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField( label='用户名 ',max_length=100)
    password = forms.CharField(label='密   码',widget=forms.PasswordInput())
    email = forms.EmailField(   label='电子邮件')

# Create your views here.
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            #将表单写入数据库
            user = User()
            user.username = username
            user.password = password
            user.email = email
            user.save()
            # print 'register info:',user.username,user.password,user.email

            #返回注册成功页面
            return render_to_response('success.html',{'username':username,'action':'注册'},context_instance=RequestContext(request))
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf})


#定义表单模型
class UserLoginForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())

#登录
def login(request):
    if request.method == 'POST':
        uf = UserLoginForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            # print username
            # print password
            #获取的表单数据与数据库进行比较
            # for i in User.objects.all():
            #     print 'hhhhh:',i.username,i.password
            user = User.objects.filter(username__exact = username,password__exact = password)
            # print user
            if user:
                
                response = render_to_response('success.html',{'username':username,'action':'登录'},context_instance=RequestContext(request))
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/blog/login/')
    else:
        uf = UserLoginForm()
    return render_to_response('login.html',{'uf':uf})

    #退出
def logout(request):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response