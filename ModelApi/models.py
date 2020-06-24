from django.db import models

# Create your models here.

class PlantDisease(models.Model):
    ImageFile = models.FileField(blank=True,null=True, upload_to="plant_images/%Y/%m/%d")
    PerdictedDisease=models.CharField(blank=True,null=True,max_length=100)

    def __str__(self):
        return str(self.ImageFile)+" has "+str(self.PerdictedDisease)

