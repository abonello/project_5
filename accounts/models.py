import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserCoins(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='relateduser')
    coin_amount = models.PositiveSmallIntegerField(default=0)


    class Meta:
        verbose_name_plural = "User coins"

    def __str__(self):
        return "{} has {} coins".format(self.user, self.coin_amount)
