from django.db import models
from trainers.models import Trainer

# Create your models here.

class YogaClass(models.Model):

    class Meta:
        verbose_name_plural = 'YogaClasses'

    level_choices = [
        (None, 'Skill Level'),
        ('all', 'All'),
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ]

    intensity_choices = [
        (None, 'Intensity Level'),
        ('low', 'Low'),
        ('regular', 'Regular'),
        ('high', 'High')
    ]

    name = models.CharField(max_length=250, null=True, blank=False)
    category = models.CharField(max_length=7, null=True, blank=False)   
    sku = models.CharField(max_length=254, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    practice = models.CharField(max_length=250, null=True, blank=False)
    level = models.CharField(max_length=250, null=True, blank=False, choices=level_choices)
    intensity = models.CharField(max_length=250, null=True, blank=False, choices=intensity_choices)
    session_duration = models.IntegerField(null=True, blank=False)
    series_duration = models.IntegerField(null=True, blank=False)
    equipment = models.CharField(max_length=250, null=True, blank=False)
    trainer = models.ForeignKey(Trainer, null=True, blank=False, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=False)
    image = models.ImageField(null=True, blank=False)

    def __str__(self):
        return self.name

