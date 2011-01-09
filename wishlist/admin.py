from django.contrib import admin
from wishlist.models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'price', 'priority')
    search_fields = ('name',)
admin.site.register(Item, ItemAdmin)
