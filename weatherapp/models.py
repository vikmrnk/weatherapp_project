from django.db import models
from django.conf import settings

# Define your models here

class FavoriteCity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    city_name = models.CharField(max_length=100)
    session_id = models.CharField(max_length=200, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Favorite Cities"
        unique_together = ('user', 'city_name', 'session_id')
        
    def __str__(self):
        return self.city_name
