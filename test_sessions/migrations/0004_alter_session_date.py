# Generated by Django 4.2 on 2023-04-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_sessions', '0003_alter_session_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]
