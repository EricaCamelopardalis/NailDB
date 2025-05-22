from django.db import models


# Create your models here.
class Polish(models.Model):
    PolishID = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=80)
    Price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    BrandID = models.ForeignKey("core.Brand", on_delete=models.PROTECT)
    ToneID = models.ForeignKey("meta.Tone", on_delete=models.PROTECT)
    UndertoneID = models.ForeignKey("meta.Undertone", on_delete=models.PROTECT)
    OpacityID = models.ForeignKey("meta.Opacity", on_delete=models.PROTECT)
    LineID = models.ForeignKey("meta.Line", on_delete=models.PROTECT)
    EventID = models.ForeignKey("core.Event", on_delete=models.SET_NULL, null=True)
    CollectionID = models.ForeignKey(
        "core.Collection", on_delete=models.SET_NULL, null=True
    )
    IsDriesMatte = models.BooleanField(default=False)
    IsGlowIntheDark = models.BooleanField(default=False)
    IsUV = models.BooleanField(default=False)
    IsTopper = models.BooleanField(default=False)
    IsThermal = models.BooleanField(default=False)


class Brand(models.Model):
    BrandID = models.AutoField(primary_key=True)
    BrandName = models.CharField(max_length=25)
    Country = models.CharField(max_length=20)
    BrandCategoryID = models.ForeignKey("meta.BrandCategory", on_delete=models.PROTECT)
    ParentCompany = models.CharField(max_length=25, null=True)
    FoundingYear = models.IntegerField(null=True)  # Add validators eventually
    OperatingCity = models.CharField(max_length=25, null=True)
    OperatingRegion = models.CharField(max_length=25, null=True)
    WebsiteUrl = models.CharField(max_length=2083, null=True)


class Collection(models.Model):
    CollectionID = models.AutoField(primary_key=True)
    BrandID = models.ForeignKey("core.BrandID", on_delete=models.PROTECT)
    ThemeID = models.ForeignKey("meta.Theme", on_delete=models.PROTECT)
    CollectionName = models.CharField(max_length=35)
    CollectionYear = models.IntegerField()
    IsInfluencerCollaboratoin = models.BooleanField()
    InfluencerName = models.CharField(max_length=25, null=True)
    IsIPCollaboration = models.BooleanField()
    IPCollaborationName = models.CharField(max_length=25, null=True)
    IsCharity = models.BooleanField()
    CharityName = models.CharField(max_length=25, null=True)
