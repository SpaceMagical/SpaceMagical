from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    user    = models.OneToOneField(User)
    comment = models.CharField(max_length=300, blank=True, null=True)

# LATER SCALE
#  
# class UserThumbnail(modes.Model):
#
#     iamge = models.ImageField()
