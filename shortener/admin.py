from django.contrib import admin

from .models import URL


class URLAdmin(admin.ModelAdmin):
    fields = ['short_url', 'long_url', 'clicks']
    readonly_fields = ['id', 'created_at']
    list_display = ('id', 'long_url', 'short_url', 'hash', 'clicks', 'created_at')


admin.site.register(URL, URLAdmin)

