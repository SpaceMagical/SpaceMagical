from django.contrib.auth.models import User
from django.db import models


class Connection(models.Model):

    user_a = models.ForeignKey(User)
    user_b = models.ForeignKey(User)
    distance = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
