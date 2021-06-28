from django.contrib import admin

from . import models

admin.site.register(models.Coin)
admin.site.register(models.Pair)