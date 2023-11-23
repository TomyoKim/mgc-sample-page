from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest
from django.contrib import auth

from .models import Account

class Login(View):
    """
    로그인을 위한 기능이 구현되어 있습니다.
    """
    def get(self, request: HttpRequest):
        """
        로그인 요청에 대해 관련 페이지를 제공합니다.
        """
        user = request.user
        
        if user.is_authenticated:
            return render(request, "user_auth/already_logined.html")
        
        return render(request, "user_auth/login.html")
    
    def post(self, request: HttpRequest):
        """
        로그인 요청에 대해 이메일 주소와 패스워드를 확인하여 거부/승낙 처리를 합니다.
        """
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = auth.authenticate(username=email, password=password)
        
        if user.is_authenticated:
            auth.login(request, user)
            return redirect("/")
        
        context = {
            "data": request.POST,
            "valid": "is-invalid",
            "message": "로그인 실패! 이메일 주소와 패스워드를 다시 확인하세요.",
        }
        
        return render(request, "user_auth/login.html", context=context)
    
class Logout(View):
    """
    로그아웃을 위한 기능이 구현되어 있습니다.
    """
    def get(self, request: HttpRequest):
        """
        로그아웃 요청에 대해 로그아웃 처리합니다.
        """
        user = request.user
        
        if user.is_authenticated:
            auth.logout(request)
            return redirect("/")
    
class SignUp(View):
    """
    회원 가입을 위한 기능이 구현되어 있습니다.
    """
    def get(self, request: HttpRequest):
        """
        회원 가입 요청에 대해 관련 페이지를 제공합니다.
        """
        user = request.user
        
        if user.is_authenticated:
            return render(request, "user_auth/already_logined.html")
        
        return render(request, "user_auth/signup.html")
    
    def post(self, request: HttpRequest):
        """
        회원 가입 요청에 대해 이메일 주소와 패스워드 등의 정보를 검증 후 거부/승낙 처리를 합니다.
        """
        email = request.POST.get("email")
        password = request.POST.getlist("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        
        user = Account.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        
        if not user:
            context = {
                "data": request.POST,
                "valid": "is-invalid",
                "message": "회원 가입 실패! 이메일 주소와 패스워드를 다시 확인하세요.",
            }
            return render(request, "user_auth/signup.html", context=context)
        
        return redirect("/")
            
    
class ChangePassword(View):
    def get(self, request: HttpRequest):
        pass
    
    def post(self, request: HttpRequest):
        pass
    
    