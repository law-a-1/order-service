from django.db import models

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
        max_length = 4,
        choices = ORDER_STATUS_CHOICES,
        default = WAITING,
    )
    username = models.CharField(max_length=255)
    order_date = models.DateTimeField()
    order_total = models.BigIntegerField()