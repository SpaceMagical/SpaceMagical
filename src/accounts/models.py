from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    user = models.OneToOneField(User)


# LATER SCALE
#  
# class UserThumbnail(modes.Model):
#
#     iamge = models.ImageField()
