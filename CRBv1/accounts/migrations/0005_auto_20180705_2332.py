# Generated by Django 2.0.6 on 2018-07-05 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_archived'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='archived',
        ),
        migrations.AddField(
            model_name='user',
            name='isdisabled',
            field=models.BooleanField(db_column='isdisabled', default=False),
        ),
    ]