from django.db import models


# Create your models here.
class Tone(models.Model):
    ToneID = models.AutoField(primary_key=True)
    ToneName = models.CharField(max_length=8)
    ToneDescription = models.CharField(80)


class Undertone(models.Model):
    UndertoneID = models.AutoField(primary_key=True)
    UndertoneName = models.CharField(max_length=12)
    UndertoneDescription = models.CharField(80)


class Opacity(models.Model):
    OpacityID = models.AutoField(primary_key=True)
    OpacityName = models.CharField(max_length=12)
    OpacityDescription = models.CharField(max_length=80)


class Line(models.Model):
    LineID = models.AutoField(primary_key=True)
    BrandID = models.ForeignKey("core.Brand", on_delete=models.PROTECT)
    LineName = models.CharField(max_length=25)
    LineDescription = models.CharField(max_length=80)
    BottleSize = models.DecimalField(max_digits=4, decimal_places=1)


class BrandCategory(models.Model):
    BrandCategoryID = models.AutoField(primary_key=True)
    BrandCategoryName = models.CharField(max_length=12)
    BrandCategoryDescription = models.CharField(max_length=80)


class Theme(models.model):
    ThemeID = models.AutoField(primary_key=True)
    ThemeName = models.CharField(max_length=35)
    ThemeDescription = models.CharField(max_length=80)
