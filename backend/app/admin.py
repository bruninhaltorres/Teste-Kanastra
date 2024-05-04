from django.contrib import admin
from app.models import Person

class Persons(admin.ModelAdmin):
    list_display = ('name', 'governmentId', 'email', 'debtAmount', 'debtDueDate')
    list_display_links = ('name', 'governmentId')
    search_fields = ('governmentId',)
    list_per_page = 20 

admin.site.register(Person, Persons)
