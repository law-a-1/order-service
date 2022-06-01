import json
import pika
import django
import config as cfg
from sys import path
from os import environ
from datetime import datetime

path.append('/home/fredypasaud/Documents/LAW/orderservice/orderservice/settings.py') #Your path to settings.py file
environ.setdefault('DJANGO_SETTINGS_MODULE', 'orderservice.settings') 
django.setup()
from orderapp.models import Order

connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))  
channel = connection.channel() 
channel.queue_declare(queue=cfg.QUEUE_TOPIC)

def callback(ch, method, properties,body):
    data = json.loads(body)
    data = json.loads(body)
    order = Order.objects.create(
        username=data["username"],
        order_total = data["grand_total"],
        order_date = datetime.now())
    order.save()

channel.basic_consume(queue=cfg.QUEUE_TOPIC, on_message_callback=callback)
print("Started Consuming...")
channel.start_consuming()