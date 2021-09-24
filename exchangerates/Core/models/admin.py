from django.contrib import admin

from .models.CurrencyRates import CurrencyRates
from .models.Currencies import Currencies

class AdminCurrencies(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'symbol')

admin.site.register(Currencies, AdminCurrencies)

class AdminCurrencyRates(admin.ModelAdmin):
    list_display = ('id', 'currency', 'date_added', 'actual_date', 'price_usd')

admin.site.register(CurrencyRates, AdminCurrencyRates)
