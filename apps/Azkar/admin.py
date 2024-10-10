from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Azkar_categories, Zikr


@admin.register(Azkar_categories)
class AzkarCategoriesAdminClass(ModelAdmin):
    list_display = ("name",)


@admin.register(Zikr)
class AzkarAdminClass(ModelAdmin):
    list_display = ('zikr_category', 'zikr_content', 'zikr_repetitions', 'binifit', )
