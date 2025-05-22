from django.db import models


# Create your models here.
class Tone(models.model):
    ToneID = models.AutoField(primary_key=True)
    ToneName = models.CharField(max_length=8)
    ToneDescription = models.CharField(80)
