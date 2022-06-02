# Generated by Django 4.0.5 on 2022-06-02 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0002_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('WAITING', 'WAITING'), ('SENDING', 'SENDING'), ('RECEIEVED', 'RECIEVED'), ('REJECT', 'REJECT')], default='WAITING', max_length=9),
        ),
    ]