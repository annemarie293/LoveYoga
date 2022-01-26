from django.db import models

# Create your models here.


class Trainer(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    years_practicing = models.IntegerField(null=False, blank=False)
    years_teaching = models.IntegerField(null=False, blank=False)
    bio = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name