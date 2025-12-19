from django.contrib import admin
from .models import Project, Client, Contact, Subscription

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile', 'city', 'created_at')
    search_fields = ('email', 'full_name') 
    list_filter = ('city',)
    readonly_fields = ('created_at',) 

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    readonly_fields = ('subscribed_at',)