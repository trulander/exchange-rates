from django.db import models
from .Currencies import Currencies

class CurrencyRates(models.Model):
    currency = models.ForeignKey('Currencies', related_name='currency_rates', db_index=True, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    actual_date = models.DateTimeField(auto_now=False)
    price_usd = models.DecimalField(max_digits=20, decimal_places=15)
    percent_change_1h = models.FloatField()
    percent_change_24h = models.FloatField()

    # class Meta(object):
    #     app_label = 'exchangerates'
        #db_table = 'exchangerates_CurrencyRates'
    def __str__(self):
        return f"{self.actual_date.date()} {self.actual_date.time()} - {self.price_usd}"
