# Generated by Django 3.2.13 on 2023-04-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('data', models.DateField()),
                ('description', models.TextField()),
                ('lucky_number', models.PositiveIntegerField()),
                ('color', models.TextField()),
            ],
        ),
    ]
