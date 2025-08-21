from django.contrib import admin
from teams.models import Organization, Role, Member
# Register your models here.

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'website', 'city']
    readonly_fields = ['created_at', 'update_at']
    list_filter = ['city']
    search_fields = ['id', 'name']
    sortable_by = ['id', 'name']

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'organization']
    readonly_fields = ['created_at', 'update_at']
    list_filter = ['organization']
    search_fields = ['id', 'name', 'organization__name']
    sortable_by = ['id', 'name', 'organization__name']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'member_id', 'user__first_name', 'role__name', 'organization', 'is_active']
    readonly_fields = ['created_at', 'update_at']
    list_filter = ['organization', 'role', 'is_active']
    search_fields = ['id', 'name', 'organization__name', 'role__name']
    sortable_by = ['id', 'name', 'organization__name', 'role__name']



#admin.site.register(Organization, OrganizationAdmin)