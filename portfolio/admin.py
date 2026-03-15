from django.contrib import admin
from .models import ContactMessage, MediaItem, Experience

@admin.register(MediaItem)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at')
    list_filter = ('category',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date')
    
@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at')
    readonly_fields = ('created_at',) # Prevent editing the timestamp