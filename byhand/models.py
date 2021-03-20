from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# from byhandpro.social.models import Post


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True,null=True)
    username = models.CharField(max_length=150, unique=True,null=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    # about = models.TextField(_(
    #     'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return self.username

class UserExtend(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    company_name = models.CharField(max_length=100,null=True)
    created_by = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100,null=True)
    profession = models.CharField(max_length=100,null=True)
    institution_name = models.CharField(max_length=100,null=True)
    degree = models.CharField(max_length=100,null=True)
    specilisation = models.CharField(max_length=100,null=True)
    start_year = models.CharField(max_length=100,null=True)
    end_year = models.CharField(max_length=100,null=True)

class Follow(models.Model):
    following = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name="who_follows")
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,related_name="who_following")
    follow_time = models.DateTimeField(auto_now=True)


# class Post(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,blank=True, null=True)
#     caption = models.CharField(max_length=500,null=True)
#     like = models.IntegerField(null=True)
#     date = models.DateTimeField(auto_now=True)
#     image = models.ImageField(upload_to='media',null=True)

# class Stream(models.Model):
#     following = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, related_name='stream_following')
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
#     date = models.DateTimeField()