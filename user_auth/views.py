from django.shortcuts import render
from django.views import View

# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "user_auth/login.html")
    
    def post(self, request):
        pass
    
class Logout(View):
    def get(self, request):
        pass
    
class SignUp(View):
    def get(self, request):
        pass
    
    def post(self, request):
        pass
    
class ChangePassword(View):
    def get(self, request):
        pass
    
    def post(self, request):
        pass
    
    