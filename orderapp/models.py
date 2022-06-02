from django.db import models

class Order(models.Model):
    WAIT = 'WAITING'
    SEND = 'SENDING'
    RECV = 'RECEIEVED'
    RJCT = 'REJECT'
    ORDER_STATUS_CHOICES = [
        (WAIT, 'WAITING'),
        (SEND, 'SENDING'),
        (RECV, 'RECIEVED'),
        (RJCT, 'REJECT'),
    ]
    order_status = models.CharField(
        max_length = 9,
        choices = ORDER_STATUS_CHOICES,
        default = WAIT,
    )
    username = models.CharField(max_length=255)
    order_date = models.DateTimeField()
    order_total = models.BigIntegerField()