# Generated by Django 2.2.10 on 2020-04-08 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='reciver_id',
            new_name='receiver_id',
        ),
    ]