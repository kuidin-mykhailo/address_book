from django.contrib import admin

from .models import Record, City, Person


@admin.register(Record)
class AddressBookAdmin(admin.ModelAdmin):
    list_display = ['person', 'city', 'address']
    search_fields = ['person', 'address']
    list_filter = ['city']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email']
