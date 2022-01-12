from django.db import models
from trainers.models import Trainer

# Create your models here.

class YogaClass(models.Model):

    class Meta:
        verbose_name_plural = 'YogaClasses'

    name = models.CharField(max_length=250)
    description = models.TextField()
    practice = models.CharField(max_length=250)
    level = models.CharField(max_length=250)
    intensity = models.CharField(max_length=250)
    session_duration = models.IntegerField()
    series_duration = models.IntegerField()
    equipment = models.CharField(max_length=250, null=True, blank=True)
    trainer = models.ForeignKey(Trainer, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
