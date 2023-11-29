from django.contrib import admin
from .models import AttendanceModel
from .forms import AttendanceModelForm

# Register your models here.

class AttendanceModelAdmin(admin.ModelAdmin):
    # 관리자 페이지에서 사용할 폼
    form = AttendanceModelForm
    
    # 관리자 리스트 뷰에서 표시할 필드
    list_display = ('name', 'context')

    # 리스트 뷰에서 필터 옵션으로 사용할 필드
    list_filter = ('name',)

    # 검색 기능에서 사용할 필드
    search_fields = ['name', 'context']

    # 필드 세트를 정의하여 입력 양식의 레이아웃을 커스터마이징할 수 있습니다.
    fieldsets = (
        (None, {
            'fields': ('name', 'context')
        }),
    )

# MyModel과 MyModelAdmin을 Django 관리자에 등록합니다.
admin.site.register(AttendanceModel, AttendanceModelAdmin)
