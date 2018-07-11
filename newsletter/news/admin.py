from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Checkable)
class CheckableAdmin(admin.ModelAdmin):
    pass
@admin.register(models.ReadRecord)
class ReadRecordAdmin(admin.ModelAdmin):
    pass