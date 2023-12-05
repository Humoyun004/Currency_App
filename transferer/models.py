from django.db import models
from django.utils import timezone

# Create your models here.
class History(models.Model):
    transferTo = models.CharField(max_length=25)
    fromTransfer = models.CharField(max_length=25)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    transfered_result = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateTimeField(default=timezone.datetime.now)


    def __str__(self):
        return f"Result of transfering: {self.transfered_result}"