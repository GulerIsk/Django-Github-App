from django.contrib import admin
from .models import Search


class SearchAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Search
