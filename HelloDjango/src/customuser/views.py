from django.shortcuts import render
from customuser.forms import CustomUserRegisterForm, CustomUserLoginForm,\
    SignForm
#OR from .forms import CustomUserRegisterForm
from .models import CustomUser
#OR from customuser.models import CustomUser
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.views import password_change
from django.template.context_processors import request
# Create your views here.
# 회원가입
def sign(request):
    if request.method == "POST":
        form = SignForm(request.POST)
        if form.is_valid():
            # **사전변수 : 사전에 들어있는 모든 키:값을 매개변수로 넘겨줌
            # User.objects.create_user() : dJango의 User 모델클래스에서 자동으로 회원을 생성함
            new_user = User.objects.create_user(**form.cleaned_data)
            return HttpResponseRedirect(reverse('polls:index'))
    elif request.method == "GET":
        form = SignForm()
        return render(request, 'customuser/sign.html', {'form':form})
'''
def sign(request):
    if request.method=="POST":
        obj = CustomUserRegisterForm(request.POST)
        if obj.is_valid():
            #obj.cleaned_data['변수명']
            id = obj.cleaned_data['id']
            password = obj.cleaned_data['password']
            passwordCheck = obj.cleaned_data['passwordCheck']
            if password == passwordCheck:
                #객체를 찾다가 없는 경우 객체를 자동으로 생성
                #CustomUser.object.get_or_creat()
                makeUser, find = CustomUser.objects.get_or_create(id=id)
                if find: #새로 생성된 객체인가?
                    makeUser.password=password
                    makeUser.save()
                    return HttpResponseRedirect(reverse('polls:index'))
                else: #기조ㅗㄴ에 생성된 객체인가?
                    error = "이미 사용중인 아이디입니다."
                    
#                 #try ~ except 문장
#                 try:
#                     user = CustomUser.objects.get(id=id) #CustomUser에서 객체를 찾음
#                     error = "이미 사용중인 아이디입니다."
#                 except CustomUser.DoesNotExist: #객체를 모소찾아서 에러가 발생
#                 #if user is None: #반환된 객체가 없는 경우
#                     makeUser = CustomUser() #빈 모델클래스의 객체 생성
#                     makeUser.id = id
#                     makeUser.password = password
#                     makeUser.save()
#                     return HttpResponseRedirect(reverse('polls:index'))
#                 #else: #반환된 객체가 있는 경우 (같은 아이디가 존재)
#                     #error = "이미 사용중인 아이디입니다."

            else:
                error = "비밀번호가 맞지 않습니다."
            return render(request, 'customuser/sign.html', {'form':obj, 'error':error})
    elif request.method=="GET":
        obj = CustomUserRegisterForm()
        return render(request, 'customuser/sign.html', {'form':obj})
'''
#로그인
def login(request):
    if request.method=="POST":
        obj = CustomUserLoginForm(request.POST)
        if obj.is_valid():
            id = obj.cleaned_data['id']
            password = obj.cleaned_data['password']
            user = CustomUser.objects.filter(id=id).filter(password=password)
            if user.exists(): #로그인 성공 (id, password가 일치하는 객체를 찾음)
                #로그인 상태로 처리
                request.session['LoginState']=True
                request.session['username']=user[0].id
                return HttpResponseRedirect(reverse('polls:index')) #index페이지로 이동
            else:
                pass
        else:
            pass
    elif request.method=="GET":
        obj = CustomUserLoginForm()
        return render(request, 'customuser/Login.html', {'form':obj})
#로그아웃
def logout(request):
    #특정 세션값만 제거
    #del request.session['username']
    #del request.session['LoginState']
    #존재하지 않는 세션값을 제거할 때 KeyError가 발생
    
    #세션
    request.session.flush() #세션에 저장된 값들을 전부 삭제
    return HttpResponseRedirect(reverse('polls:index'))