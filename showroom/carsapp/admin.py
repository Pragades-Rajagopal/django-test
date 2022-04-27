from django.contrib import admin
from .models import Showroom, Cars

admin.site.site_header = 'showroom app'
admin.site.site_title = 'App admin page'
admin.site.index_title = 'Welcome to the Showroom app admin page'

class CarsInline(admin.TabularInline):
    model = Cars

class ShowroomAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['showroom_name', 'city']})]
    inlines = [CarsInline]

admin.site.register(Showroom, ShowroomAdmin)

