from django.db import models


class Currencies(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    symbol = models.CharField(max_length=50)

    # class Meta(object):
    #     app_label = 'exchangerates'
        #db_table = 'exchangerates_Currencies'
