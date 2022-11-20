from django.contrib import admin

from .models import Teams, Predictions

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ['user', 'index', 'round', 'team', 'ranking', 'group', 'point']

class PredictAdmin(admin.ModelAdmin):
    list_display = ['user', 'index', 'round', 'rank', 'group', 'prediction', 'result', 'point']

admin.site.register(Teams, TeamAdmin)
admin.site.register(Predictions, PredictAdmin)
