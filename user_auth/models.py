from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core import exceptions

# Create your models here.
class AccountManager(UserManager):
    """
    사용자 정보를 관리하기 위한 기능을 커스텀 하기 위해 분리해 둠
    """
    def create_user(self, username: str, email: str | None = ..., password: list | None = ..., **extra_fields: Any) -> Any:
        try:
            password = self._validate_password(password)
        except:
            return None
        else:
            return super().create_user(username, email, password, **extra_fields)
    
    def _validate_password(self, password: list):
        if len(password) != 2:
            raise exceptions.FieldError("회원 가입에 사용 할 패스워드는 리스트에 담아주세요.: [password, check_password]")
        
        if password[0] != password[1]:
            raise exceptions.ValidationError("두 패스워드가 일치하지 않습니다.")
        
        return password[0]]

class Account(AbstractUser):
    """
    사용자 정보를 Django에서 제공하는 정보로 사용하지만 나중에 커스텀 할 수 있도록 분리해 둠
    """
    objects = AccountManager()
