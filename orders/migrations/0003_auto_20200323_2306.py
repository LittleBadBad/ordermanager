# Generated by Django 2.2.10 on 2020-03-23 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200323_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='recive_time',
            field=models.TimeField(null=True, verbose_name='签收日期'),
        ),
        migrations.AddField(
            model_name='order',
            name='reciver_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]