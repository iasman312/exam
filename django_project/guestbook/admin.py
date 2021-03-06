from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'status', 'email', 'created_at',
                    'updated_at']
    list_filter = ['author']
    search_fields = ['author', 'status']
    fields = ['author', 'email', 'text', 'status']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(Feedback, FeedbackAdmin)