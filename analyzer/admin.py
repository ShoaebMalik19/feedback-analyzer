from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('text', 'sentiment', 'confidence')  # Show these columns
    search_fields = ('text',)  # Add search box
    list_filter = ('sentiment',)  # Add filter sidebar