from django.contrib import admin

from .models import *

admin.site.register(Sensor)
admin.site.register(SensorType)
# admin.site.register(Log)
admin.site.register(Unit)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'sensor', 'logged_at', 'temp')
    search_fields = ('id', 'sensor')
    # list_filter = ('updated_at', 'created_at',)
    # ordering = ('-logged_at)')
    # autocomplete_fields = ('author',)

    # def created_at_view(self, obj):
    #     if obj.created_at:
    #         return jdatetime.date.fromgregorian(date=obj.created_at)
