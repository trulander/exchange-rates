from django.contrib import admin

from .models.currencyrate import CurrencyRate
from .models.сurrency import Currency

class AdminCurrencies(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'symbol')

admin.site.register(Currency, AdminCurrencies)

class AdminCurrencyRates(admin.ModelAdmin):
    list_display = ('id', 'currency', 'date_added', 'actual_date', 'price_usd')

admin.site.register(CurrencyRate, AdminCurrencyRates)
