# Generated by Django 2.0.6 on 2018-07-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranges', '0002_auto_20180705_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rangestudents',
            name='progress',
            field=models.IntegerField(db_column='progress', null=True),
        ),
    ]
