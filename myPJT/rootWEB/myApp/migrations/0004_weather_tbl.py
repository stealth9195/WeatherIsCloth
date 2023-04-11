# Generated by Django 4.1.7 on 2023-04-06 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_city_tbl'),
    ]

    operations = [
        migrations.CreateModel(
            name='weather_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField(default=0)),
                ('Highest_temperature', models.FloatField(default=0)),
                ('Lowest_temperature', models.FloatField(default=0)),
                ('city_name', models.ForeignKey(db_column='city_name', on_delete=django.db.models.deletion.CASCADE, to='myApp.city_tbl')),
            ],
        ),
    ]
