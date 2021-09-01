from django.contrib import admin

from .models import *


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class AddressAdmin(admin.ModelAdmin):
    list_display = ['country', 'city', 'street', 'house', 'residents', 'question_text']
    list_display_links = ['country', 'city', 'street']
    inlines = [ChoiceInline]


admin.site.register(Address, AddressAdmin)
