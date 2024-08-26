# Generated by Django 4.2.8 on 2024-08-26 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=255, unique=True)),
                ('total_price', models.PositiveIntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
