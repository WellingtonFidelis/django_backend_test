# Generated by Django 3.1.7 on 2021-04-03 00:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210319_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formtest',
            name='birth_date',
            field=models.DateField(default=datetime.date(2021, 4, 3)),
        ),
    ]
