# Generated by Django 3.1.7 on 2021-03-06 22:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210305_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formtest',
            name='birth_date',
            field=models.DateField(default=datetime.date(2021, 3, 6)),
        ),
    ]
