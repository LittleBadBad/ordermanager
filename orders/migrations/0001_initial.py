# Generated by Django 2.2.10 on 2020-03-23 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20200313_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=20)),
                ('start_date', models.DateField(verbose_name='开始日期')),
                ('end_date', models.DateField(verbose_name='结束日期')),
                ('found_date', models.DateField(verbose_name='创建日期')),
                ('delete_date', models.DateField(verbose_name='删除日期')),
                ('unit', models.CharField(max_length=20)),
                ('verifier_id', models.CharField(max_length=20)),
                ('recaller_id', models.CharField(max_length=20)),
                ('status', models.IntegerField(default=0)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='开始时间')),
                ('end_time', models.TimeField(verbose_name='结束时间')),
                ('place', models.CharField(max_length=50)),
                ('cause', models.CharField(max_length=20)),
                ('speed_limit', models.IntegerField(default=100)),
                ('pattern', models.CharField(max_length=20)),
                ('device', models.CharField(max_length=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
    ]