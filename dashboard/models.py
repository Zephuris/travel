from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Travel(models.Model):
    title = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    destination = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    tour_lead = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'travel')

    def __str__(self) -> str:
        return self.title