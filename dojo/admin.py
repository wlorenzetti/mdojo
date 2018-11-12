from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Dojo, Deshi, Shiken, Levels
from .ie.resources import DeshiResource


@admin.register(Levels)
class LevelsAdmin(admin.ModelAdmin):
    pass


@admin.register(Shiken)
class ShikenAdmin(admin.ModelAdmin):
    pass


class ShikenInline(admin.TabularInline):
    model = Shiken


@admin.register(Deshi)
class DeshiAdmin(ImportExportModelAdmin):
    resource_class = DeshiResource
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



