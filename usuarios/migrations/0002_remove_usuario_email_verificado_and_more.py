# Generated by Django 5.2.1 on 2025-05-28 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='email_verificado',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='token_verificacion',
        ),
    ]
