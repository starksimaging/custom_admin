from django.contrib import admin
from .models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'joined_date')
    search_fields = ('last_name', 'last_name', 'email')
    list_filter = ('joined_date')
    ordering = ('joined_date')
    readonly_fields = ('joined_date')



    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Data Info', {
            'fields': ('joined_date',),
            'classes': ('collapse')
        })
    )


    admin.site.site_header = "My Custom Admin"
    admin.site.site_title = 'Customer Admin Portal'
    admin.site.index_title = 'Welcome to the Admin Dashboard'
    admin.site.index_temlate  = 'admin/custom_index.html'