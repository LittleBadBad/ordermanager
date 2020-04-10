from django.contrib import admin
from orders.models import Order,Order_item
# Register your models here.
class ItemInline(admin.TabularInline):
    model = Order_item
    extra = 5

class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
admin.site.register(Order,OrderAdmin)