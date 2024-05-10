from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AnonymousUser, BaseUserManager
from django.db import transaction

# Create your models here.
class UserManager(BaseUserManager):
  
  def _create_user(self, email, password, **extra_fields):
    if not email:
        raise ValueError('The given email must be set')
    try:
        with transaction.atomic():
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
    except:
        raise
      
  def create_user(self, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, password, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    return self._create_user(email, password, **extra_fields)
  

class User(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(unique=True)
  is_active = models.BooleanField(default=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  date_joined = models.DateTimeField(default=timezone.now)
  
  objects = UserManager()
  
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["name"]
  
  def has_perm(self, perm: str, obj: models.Model | AnonymousUser | None = ...) -> bool:
    # return super().has_perm(perm, obj)
    return True
  
  class Meta:
    db_table = "users"
  
  
 