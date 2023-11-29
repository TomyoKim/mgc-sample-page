from django.db import models

# Create your models here.
class AttendanceManager(models.Manager):
    def add(self, name: str, context: str):
        model = self.model(name=name, context=context)
        model.save()
        return model
    
    def get(self, name: str):
        return super().get(name=name)
    
    def create(self, name: str, context: str):
        return super().create(name=name, context=context)
    
class AttendanceModel(models.Model):
    name = models.CharField(max_length=50)   # 'name' 필드, 최대 길이 100자
    context = models.CharField(max_length=500) # 'context' 필드, 최대 길이 500자
    
    objects = AttendanceManager()

    def __str__(self):
        return f"({self.name}, {self.context})"

    class Meta:
        verbose_name = "출석"
        verbose_name_plural = "출석(들)"