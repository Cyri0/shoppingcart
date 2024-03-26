from django.contrib import admin
from .models import ShopItem, OrderItem, Order

# Register your models here.

admin.site.register(ShopItem)
admin.site.register(OrderItem)
admin.site.register(Order)