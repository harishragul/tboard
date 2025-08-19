from django.contrib import admin
from teams.models import Organization
# Register your models here.

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'website', 'city']
    readonly_fields = ['created_at', 'update_at']
    list_filter = ['city']
    search_fields = ['id', 'name']
    sortable_by = ['id', 'name']

#admin.site.register(Organization, OrganizationAdmin)