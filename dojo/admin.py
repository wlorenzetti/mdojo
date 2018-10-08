from django.contrib import admin
from .models import Dojo, Deshi, Shiken, Levels


@admin.register(Levels)
class LevelsAdmin(admin.ModelAdmin):
    pass


@admin.register(Shiken)
class ShikenAdmin(admin.ModelAdmin):
    pass


class ShikenInline(admin.TabularInline):
    model = Shiken


@admin.register(Deshi)
class DeshiAdmin(admin.ModelAdmin):
    inlines = [
        ShikenInline
    ]


class DeshiInline(admin.TabularInline):
    model = Deshi


@admin.register(Dojo)
class DojoAdmin(admin.ModelAdmin):

    inlines = [
        DeshiInline
    ]





