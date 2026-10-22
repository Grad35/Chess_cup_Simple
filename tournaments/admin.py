from django.contrib import admin
from .models import Tournament,Application
@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display=("title","date","location","is_open")
    list_filter=("is_open","date"); search_fields=("title","location")
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display=("user","tournament","created_at","status")
    list_filter=("status","tournament"); list_editable=("status",)
    search_fields=("user__username","tournament__title")
