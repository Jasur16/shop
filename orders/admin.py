from django.contrib import admin
from .models import OrderHistoryModel


@admin.register(OrderHistoryModel)
class OrderHistoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'created_at']
    list_display_links = ['id', 'first_name', 'last_name', 'created_at']
