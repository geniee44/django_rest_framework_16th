# Generated by Django 3.0.8 on 2022-11-19 12:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20221112_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 19, 12, 17, 38, 735389, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2022, 11, 19, 12, 17, 38, 735045, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]
