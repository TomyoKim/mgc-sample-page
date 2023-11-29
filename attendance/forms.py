from django import forms
from .models import AttendanceModel

class AttendanceModelForm(forms.ModelForm):
    class Meta:
        model = AttendanceModel
        fields = ['name', 'context']
        widgets = {
            'context': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # rows와 cols는 원하는 크기에 맞게 조정
        }