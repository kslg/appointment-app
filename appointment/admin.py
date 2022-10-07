from django.contrib import admin
from .models import Teacher, Appointment
# Register your models here.

admin.site.register(Teacher)


@admin.register(Appointment)
class Admin (admin.ModelAdmin):

    list_display = (
        'date',
        'time',
        'parent_name',
        'teacher',
        'child_name',
        'accepted'
    )
    search_fields = ['teacher', 'child_name']
    actions = ['accepted']
    list_filter = ('date', 'time', 'accepted')

    def approved(self, request, queryset):
        queryset.update(approved=True)
