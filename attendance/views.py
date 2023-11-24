from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View

# Create your views here.
class Attendance(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "attendance/index.html")
    
    def post(self, request: HttpRequest) -> HttpResponse:
        pass
