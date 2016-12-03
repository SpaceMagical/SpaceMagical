from django.contrib.auth.models import User
from django.db import models


class Space(models.Model):
    
    name        = models.CharField(max_length=120)
    capacity    = models.IntegerField(blank=False, null=False)
    description = models.TextField()
    zipcode     = models.CharField(max_length=20, blank=False, null=False)
    country     = models.CharField(max_length=60, default='japan')
    state       = models.CharField(max_length=60, blank=True, null=True)
    city        = models.CharField(max_length=120, blank=False, null=False)
    address     = models.CharField(max_length=120, blank=False, null=False)
    date_added  = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_active   = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_ours     = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
 
    # def get_absolute_url(self):
    #     pass

    
def space_image_upload_to(instance, filename):
    space_id = instance.space.id
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" % (space_id, instance.id, file_extension)
    return "spaces/%s/%s" % (space_id, new_filename)


class SpaceImages(models.Model):

    space    = models.ForeignKey(Space)
    image    = models.ImageField(upload_to=space_image_upload_to)
    is_shown = models.BooleanField(default=True)

    def __str__(self):
        return self.space.name


class Rating(models.Model):

    user      = models.ForeignKey(User)
    space     = models.ForeignKey(Space)
    star      = models.PositiveIntegerField(default=3, blank=False, null=False)
    content   = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Rating for %s by %s: %d stars" % (self.space.name,
                                                  self.user.username,
                                                  self.star)

    # def get_absolute_url(self):
    #     return url
