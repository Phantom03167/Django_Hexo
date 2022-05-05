from django.db import models
from django.contrib import admin
from blog import models as m_models
from django.forms import TextInput, Textarea
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin


# Register your models here.

# admin.site.register(m_models.Article)
@admin.register(m_models.Article)
class ArticleAdmin(ImportExportModelAdmin):
    list_display = ('title', 'cover_data', 'is_recommend', 'pub_time', 'update_time')
    search_fields = ('title', 'summary', 'content')
    list_filter = ('pub_time',)
    list_editable = ('is_recommend',)
    readonly_fields = ('cover_admin',)
    list_per_page = 15

    fieldsets = (
        ('编辑文章', {
            'fields': ('title', 'content')
        }),
        ('其他设置', {
            'classes': ('collapse',),
            'fields': ('cover', 'cover_admin', 'summary', 'is_recommend', 'read_count', 'pub_time'),
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '59'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 59})},
    }
