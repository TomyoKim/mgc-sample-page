from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class AccountManager(UserManager):
    '''
    사용자 정보를 관리하기 위한 기능을 커스텀 하기 위해 분리해 둠
    '''
    pass

class Account(AbstractUser):
    '''
    사용자 정보를 Django에서 제공하는 정보로 사용하지만 나중에 커스텀 할 수 있도록 분리해 둠
    '''
    pass
