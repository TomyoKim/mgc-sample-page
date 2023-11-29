from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import View
from .models import AttendanceModel

# Create your views here.
class Attendance(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        data = AttendanceModel.objects.all()
        
        context = {
            "data": data
        }
        
        return render(request, "attendance/index.html", context=context)
    
    def post(self, request: HttpRequest) -> HttpResponse:
        name = request.POST.get("name")
        context = request.POST.get("context")
        
        AttendanceModel.objects.create(name, context)
        
        return redirect("attendance:index")
