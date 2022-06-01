# Generated by Django 4.0.4 on 2022-05-27 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0002_remove_order_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.CharField(default='none', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
