from django.db import models

# Create your models here.
class AttendanceModel(models.Model):
    name = models.CharField(max_length=50)   # 'name' 필드, 최대 길이 100자
    context = models.CharField(max_length=500) # 'context' 필드, 최대 길이 500자

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "출석"
        verbose_name_plural = "출석(들)"