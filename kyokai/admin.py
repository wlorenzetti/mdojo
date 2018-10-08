from django.contrib import admin
from .models import Kyokai, Affiliation


@admin.register(Kyokai)
class KyokaiAdmin(admin.ModelAdmin):
    pass


@admin.register(Affiliation)
class AffilationAdmin(admin.ModelAdmin):
    pass