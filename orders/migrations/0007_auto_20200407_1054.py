# Generated by Django 2.2.10 on 2020-04-07 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200406_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_item',
            name='device',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order_item',
            name='pattern',
            field=models.CharField(max_length=100),
        ),
    ]
