from django.db import models
from django.contrib.auth.models import User

class HealthLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    steps = models.IntegerField(default=0)
    calories = models.FloatField(default=0)
    water_intake = models.FloatField(default=0)
    sleep_hours = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user.username if self.user else 'NoUser'} - {self.date}"
