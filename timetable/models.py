
from django.db import models

class TimeSlot(models.Model):
    Day = models.CharField(max_length=20)
    Start_Time = models.TimeField()
    End_Time = models.TimeField()
    Subject_Name = models.CharField(max_length=100)
    Faculty_Name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Day} - {self.Subject_Name}"
