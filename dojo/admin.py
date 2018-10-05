from django.contrib import admin
from .models import Dojo, Deshi


@admin.register(Deshi)
class DeshiAdmin(admin.ModelAdmin):
    pass


class DeshiInline(admin.TabularInline):
    model = Deshi


@admin.register(Dojo)
class DojoAdmin(admin.ModelAdmin):

    inlines = [
        DeshiInline
    ]


