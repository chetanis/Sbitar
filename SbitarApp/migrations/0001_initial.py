# Generated by Django 4.2.9 on 2024-01-26 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('specialty', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
    ]
