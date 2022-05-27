# Generated by Django 4.0.4 on 2022-05-27 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('grand_total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('WAIT', 'Waiting'), ('SEND', 'Sending'), ('RCVE', 'RCVE'), ('RJCT', 'RJCT')], default='WAIT', max_length=4)),
                ('order_date', models.DateTimeField()),
                ('order_total', models.BigIntegerField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orderapp.cart')),
            ],
        ),
    ]