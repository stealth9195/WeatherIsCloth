from django.db import models
from django.utils import timezone

# Create your models here.

class user_tbl(models.Model) :
    user_id     = models.CharField(primary_key=True, max_length=50)
    user_pwd   = models.CharField(max_length=50)

class board_tbl(models.Model) :
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(user_tbl,
                               on_delete=models.CASCADE,
                               db_column='writer',
                               null=False
                               )
    content = models.TextField()
    regdate = models.DateTimeField(default=timezone.now)

class city_tbl(models.Model) :
    city_name = models.CharField(primary_key=True, max_length=50)
    city_lat = models.FloatField(default=0.00)
    city_lng = models.FloatField(default=0.00)

class weather_tbl(models.Model) :
    city_name   = models.ForeignKey(city_tbl,
                                    on_delete=models.CASCADE,
                                    db_column='city_name',
                                    null=False)
    date = models.IntegerField(default=0)
    Highest_temperature = models.FloatField(default=0)
    Lowest_temperature = models.FloatField(default=0)

class combination_tbl(models.Model) :
    combination = models.IntegerField(primary_key=True)
    outer = models.CharField(max_length=50)
    torso = models.CharField(max_length=50)
    pants = models.CharField(max_length=50)
    shoes = models.CharField(max_length=50)
    Highest_temperature = models.FloatField(default=0)
    Lowest_temperature = models.FloatField(default=0)

