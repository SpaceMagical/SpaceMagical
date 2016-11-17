from django.contrib.auth.models import User
from django.db import models
from spaces.models import Space


class Help(models.Model):

    user = models.ForeignKey(User)
    content = models.TextField()
    space = models.ForeignKey(Space)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    num_viewed = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    
    
