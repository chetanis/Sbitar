# Generated by Django 4.2.9 on 2024-01-26 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SbitarApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='availability',
        ),
    ]