from django.contrib import admin

from .models import Tariff,OriginCart,CartPay,PayHistory

# Register your models here.
admin.site.register(Tariff)
admin.site.register(OriginCart)
admin.site.register(CartPay)
admin.site.register(PayHistory)