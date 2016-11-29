from django.contrib import admin
from .models import MonjuNoChie


class MonjuNoChieAdmin(admin.ModelAdmin):

    class Meta:
        model = MonjuNoChie


admin.site.register(MonjuNoChie, MonjuNoChieAdmin)
