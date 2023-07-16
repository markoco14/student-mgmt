from django.db import models

# Create your models here.

class Weekday(models.Model):
    DAYS_OF_WEEK = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    ]

    day = models.IntegerField(choices=DAYS_OF_WEEK)

    def __str__(self):
        return self.get_day_display()