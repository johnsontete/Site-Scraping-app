from django.db import models

# Create your models here.
class Scrapeinks(models.Model):
    address = models.CharField(max_length=1000, null=True,blank=True)
    name = models.CharField(max_length=1000, null=True,blank=True)

    def __str(self):
        return self.name
    