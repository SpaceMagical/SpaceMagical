from django.contrib.auth.models import User
from django.db import models
from spaces.models import Space


class MonjuNoChie(models.Model):

    user        = models.ForeignKey(User)
    content     = models.TextField()
    space       = models.ForeignKey(Space)
    timestamp   = models.DateTimeField(auto_now_add=True, auto_now=False)
    num_viewed  = models.PositiveIntegerField()
    is_active   = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return "Request from %s" % self.user.username
    
    
class Caregory(models.Model):

    CATEGORIES = (
        ('programming', 'Programming'),
        ('life', 'Life'),               
    )
    
    name = models.CharField(max_length=120, choices=CATEGORIES, blank=True, null=False)
    monju = models.ForeignKey(MonjuNoChie, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
