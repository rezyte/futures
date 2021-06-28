from django.db import models


class Coin(models.Model):
    title = models.CharField(max_length=225)
    # price = 
    logo = models.ImageField(null=True, blank=True)
    acro = models.CharField(max_length=8)

    def __str__(self):
        return self.title

class Pair(models.Model):
    first = models.ForeignKey(
        'Coin', on_delete=models.CASCADE,
        related_name="first_pair",
        related_query_name="fist_pair",
    )
    second = models.ForeignKey(
        'Coin', on_delete=models.CASCADE,
        related_name="fsecond_pair",
        related_query_name="second_pair",
    )    
    # last_price = models.ForeignKey('Coin')
    pair_name = models.CharField(null=True, blank=True, max_length=20)

    def save(self, *args, **kwargs):
        self.pair_name = f'{self.first.acro}{self.second.acro}'
        super(Pair, self).save(*args, **kwargs)

    def __str__(self):
        return self.pair_name


