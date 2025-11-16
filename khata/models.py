from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        
    # Creates and saves an user with the given email and password
       if not email:
           raise ValueError("user must have an valid email address")
       user = self.model(email=self.normalize_email(email))
       user.set_password(password)
       user.save(using=self._db)
       return user
   
    def create_superuser(self, email, password=None, **extra_fields):
       extra_fields.setdefault('is_staff', True) 
       extra_fields.setdefault('is_superuser', True)
       if extra_fields.get('is_staff') is not True:
           raise ValueError('Superuser must have is_staff=True.')
       if extra_fields.get('is_superuser') is not True:
           raise ValueError('Superuser must have is_superuser=True.')
       
#        # Creates and Saves a superuser according to the given password and email.
       user = self.create_user(email, password)
       self.is_staff = True
       self.is_superuser = True
       self.is_buyer = True
       self.is_seller = True
       user.save(using=self._db)
       return user
       

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the User have permissions to view the app"
        # Only Superuser have permission to access all data
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return self.is_superuser
    


