from django.db import models

# Create your models here.


class Trainer(models.Model):
    name = models.CharField(max_length=254)
    years_practicing = models.IntegerField()
    years_teaching = models.IntegerField()
    bio = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name