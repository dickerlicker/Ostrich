# Generated by Django 2.0.7 on 2018-08-05 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ranges', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='range',
            old_name='createdbyusername',
            new_name='createdby',
        ),
    ]