from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class AccountManager(UserManager):
    '''
    사용자 정보를 관리하기 위한 기능을 커스텀 하기 위해 분리해 둠
    '''
    def create_user(self, username: str, email: str | None = ..., password: list | None = ..., **extra_fields: Any) -> Any:
        if len(password) != 2:
            return None
        
        if password[0] != password[1]:
            return None
        
        return super().create_user(username, email, password[0], **extra_fields)

class Account(AbstractUser):
    '''
    사용자 정보를 Django에서 제공하는 정보로 사용하지만 나중에 커스텀 할 수 있도록 분리해 둠
    '''
    objects = AccountManager()
