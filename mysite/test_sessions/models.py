from django.db import models

# Create your models here.
class Session(models.Model):
    Title = models.CharField(max_length=60)
    Description =  models.CharField(max_length=120)
    Candidateid = models.IntegerField()
    CandidateName = models.CharField(max_length=60)
    Date = models.DateTimeField()
    LocationName = models.CharField(max_length=60)
    Latitude = models.DecimalField(decimal_places=6, max_digits=10)
    Longitude = models.DecimalField(decimal_places=6, max_digits=10)

    def __str__(self):
        return self.Title