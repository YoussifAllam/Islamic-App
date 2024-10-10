from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Azkar_categories, Zikr
from image_uploader_widget.widgets import ImageUploaderWidget
from django.db import models


@admin.register(Azkar_categories)
class AzkarCategoriesAdminClass(ModelAdmin):
    list_display = ("name",)
    formfield_overrides = {
        models.ImageField: {'widget': ImageUploaderWidget},
    }


@admin.register(Zikr)
class AzkarAdminClass(ModelAdmin):
    list_display = ('zikr_category', 'zikr_content', 'zikr_repetitions', 'binifit', )
