from itertools import product
from django.db import models

class Cart(models.Model):
    username = models.CharField(max_length=255, unique=True)
    grand_total = models.IntegerField(default=0)

class Order(models.Model):
    WAITING = 'WAIT'
    SENDING = 'SEND'
    RECIEVED = 'RCVE'
    REJECT = 'RJCT'
    ORDER_STATUS_CHOICES = [
        (WAITING, 'Waiting'),
        (SENDING, 'Sending'),
        (RECIEVED, 'RCVE'),
        (REJECT, 'RJCT'),
    ]
    order_status = models.CharField(
        max_length = 2,
        choices = ORDER_STATUS_CHOICES,
        default = WAITING,
    )
    username = models.ForeignKey(Cart, related_name= "orders", on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    order_total = models.BigIntegerField()