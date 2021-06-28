from django.db import models



class Order(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    closed_on = models.DateTimeField(blank=True, null=True)
    pair = models.ForeignKey('cryptos.Pair', on_delete=models.CASCADE)
    margin = models.PositiveIntegerField() 
    entry_price = models.PositiveIntegerField()
    exit_price = models.PositiveIntegerField()
    leverage = models.PositiveIntegerField()
    take_profit = models.IntegerField(null=True, blank=True)

    def __str__(self):
        if self.take_profit:
            return f'{self.take_profit} @ {self.closed_on}'
        else:
            return f'{self.timestamp} on the day of light'
        
