# Generated by Django 4.2.9 on 2024-01-26 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SbitarApp', '0007_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
