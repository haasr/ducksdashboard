from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SiteLook(models.Model):
    """Contains attributes that affect the appearance of the site."""
    navigation_img      = models.FileField()
    navigation_img_size = models.CharField(max_length=12, blank=True, null=True)


class UserProfile(models.Model):
    profile_img      = models.FileField(null=True, blank=True)
    profile_img_name = models.TextField(default='profile-default.gif')
    profile_role     = models.CharField(max_length=13, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)