from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest
from django.contrib import auth

from .models import User

# Create your views here.
class Login(View):
    def get(self, request: HttpRequest):
        return render(request, "user_auth/login.html")
    
    def post(self, request: HttpRequest):
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = auth.authenticate(username=email, password=password)
        
        if user.is_authenticated:
            auth.login(request, user)
            return redirect("/")
        
        context = {
            "email": email,
            "valid": "is-invalid",
            "message": "로그인 실패! 이메일 주소와 패스워드를 다시 확인하세요.",
            "data": request.POST
        }
        
        return render(request, "user_auth/login.html", context=context)
    
class Logout(View):
    def get(self, request: HttpRequest):
        user = request.user
        
        if user.is_authenticated:
            auth.logout(request)
            return redirect("/")
    
class SignUp(View):
    def get(self, request: HttpRequest):
        pass
    
    def post(self, request: HttpRequest):
        pass
    
class ChangePassword(View):
    def get(self, request: HttpRequest):
        pass
    
    def post(self, request: HttpRequest):
        pass
    
    