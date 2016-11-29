from django.contrib.auth.models import User
from django.db import models


class Connection(models.Model):

    user_a    = models.ForeignKey(User, related_name='user_a')
    user_b    = models.ForeignKey(User, related_name='user_b')
    distance  = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
