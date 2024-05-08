from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', verbose_name="аватар", null=True, blank=True)
    bio = models.TextField(verbose_name='о себе', null=True, blank=True)
    location = models.CharField(max_length=20, verbose_name="местоположение", null=True, blank=True)

    def __str__(self):
        return self.user.username
