from django.contrib import admin
from .models import Rating, Space


class RatingAdmin(admin.ModelAdmin):

    class Meta:
        model = Rating


class SpaceAdmin(admin.ModelAdmin):

    class Meta:
        model = Space


admin.site.register(Rating, RatingAdmin)
admin.site.register(Space, SpaceAdmin)
