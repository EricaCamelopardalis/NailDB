from django.db import models


# Create your models here.
class Polish(models.Model):
    PolishID = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=80)
    Price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    BrandID = models.ForeignKey("Brand", on_delete=models.PROTECT)
    ToneID = models.ForeignKey("meta.Tone", on_delete=models.PROTECT)
    UndertoneID = models.ForeignKey("meta.Undertone", on_delete=models.PROTECT)
    OpacityID = models.ForeignKey("meta.Opacity", on_delete=models.PROTECT)
    LineID = models.ForeignKey("meta.Line", on_delete=models.PROTECT)
    EventID = models.ForeignKey("Event", on_delete=models.SET_NULL, null=True)
    CollectionID = models.ForeignKey("Collection", on_delete=models.SET_NULL, null=True)
    IsDriesMatte = models.BooleanField(default=False)
    IsGlowIntheDark = models.BooleanField(default=False)
    IsUV = models.BooleanField(default=False)
    IsTopper = models.BooleanField(default=False)
    IsThermal = models.BooleanField(default=False)


class Brand(models.model):
    BrandID = models.AutoField(primary_key=True)
    BrandName = models.CharField(max_length=25)
    Country = models.CharField(max_length=20)
    BrandCategoryID = models.ForeignKey("meta.BrandCategory", on_delete=models.PROTECT)
    ParentCompany = models.CharField(max_length=25, null=True)
    FoundingYear = models.IntegerField(null=True)  # Add validators eventually
    OperatingCity = models.CharField(max_length=25, null=True)
    OperatingRegion = models.CharField(max_length=25, null=True)
    WebsiteUrl = models.CharField(max_length=2083, null=True)
