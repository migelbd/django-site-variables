from django.contrib import admin
from django_site_settings.forms import SiteVariableForm, SiteVariableNumberForm, SiteVariableBooleanForm
from django.utils.translation import gettext_lazy as _
from django_site_settings.models import SiteVariable, SiteVariableText, SiteVariableBoolean, SiteVariableNumber


# @admin.register(SiteVariable)
class SiteVariableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'content',
    )
    list_display_links = (
        'id',
        'name',
    )
    fields = (
        'name',
        'content',
    )

    search_fields = ('name', 'content',)


@admin.register(SiteVariableText)
class SiteVariableTextAdmin(SiteVariableAdmin):
    pass


@admin.register(SiteVariableBoolean)
class SiteVariableBooleanAdmin(SiteVariableAdmin):
    form = SiteVariableBooleanForm
    list_display = (
        'id',
        'name',
        'content_value',
    )

    @admin.display(description=_('value'), boolean=True)
    def content_value(self, obj):
        return obj.content.lower() == 'true'


@admin.register(SiteVariableNumber)
class SiteVariableNumberAdmin(SiteVariableAdmin):
    form = SiteVariableNumberForm
    list_display = (
        'id',
        'name',
        'content',
    )


