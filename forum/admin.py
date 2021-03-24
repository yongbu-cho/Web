from django.contrib import admin


# Register your models here.
from .models import  Presenting, Suggestion

class SuggestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class PresentingAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Presenting, PresentingAdmin)
admin.site.register(Suggestion, SuggestionAdmin)


