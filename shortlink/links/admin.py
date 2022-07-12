from django.contrib import admin

from links.models import Links


class LinksAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'time_create')
    search_fields = ('user_name',)
    list_filter = ('time_create',)


admin.site.register(Links, LinksAdmin)
