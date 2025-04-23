from django.contrib import admin
from .models import FavoriteCity

@admin.register(FavoriteCity)
class FavoriteCityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'user', 'session_id', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('city_name', 'user__username')
