from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not phone_number:
            raise ValueError('Users must have a phone number')

        user = self.model(
            phone_number=self.normalize_email(phone_number),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            phone_number,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='آدرس ایمیل',
        max_length=255,
        null=True,
        blank=True,
        unique=True,
    )
    fullname = models.CharField(max_length=50, null=True, blank=True, verbose_name='نام کامل')
    phone_number = models.CharField(max_length=12,null=True, blank=True, unique=True, verbose_name='شماره همراه')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_admin = models.BooleanField(default=False, verbose_name='ادمین')

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Otp(models.Model):
    token = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11)
    code = models.SmallIntegerField()
    expiration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone


class UserInformation(models.Model):
    user = models.ForeignKey(User, models.CASCADE, related_name="informations", verbose_name='مشتری')
    fullname = models.CharField(max_length=50, verbose_name='نام کامل')
    address = models.CharField(max_length=400, verbose_name='آدرس')
    email = models.EmailField(blank=True, null=True, verbose_name='آدرس ایمیل')
    phone = models.CharField(max_length=11, verbose_name='تلفن همراه')
    postal_code = models.CharField(max_length=10, verbose_name='کد پستی')

    def __str__(self):
        return self.user.phone_number

    class Meta:
        verbose_name = 'اطلاعات کاربر'
        verbose_name_plural = 'اطلاعات کاربرها'
