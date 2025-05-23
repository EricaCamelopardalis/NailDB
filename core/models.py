from django.db import models


# Create your models here.
class Polish(models.Model):
    PolishID = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=80)
    Price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BrandID = models.ForeignKey("core.Brand", on_delete=models.PROTECT)
    ToneID = models.ForeignKey("meta.Tone", on_delete=models.PROTECT)
    UndertoneID = models.ForeignKey("meta.Undertone", on_delete=models.PROTECT)
    OpacityID = models.ForeignKey("meta.Opacity", on_delete=models.PROTECT)
    LineID = models.ForeignKey("meta.Line", on_delete=models.PROTECT)
    EventID = models.ForeignKey(
        "core.Event", on_delete=models.SET_NULL, null=True, blank=True
    )
    CollectionID = models.ForeignKey(
        "core.Collection", on_delete=models.SET_NULL, null=True, blank=True
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
    ParentCompany = models.CharField(max_length=25, null=True, blank=True)
    FoundingYear = models.IntegerField(
        null=True, blank=True
    )  # Add validators eventually
    OperatingCity = models.CharField(max_length=25, null=True, blank=True)
    OperatingRegion = models.CharField(max_length=25, null=True, blank=True)
    WebsiteUrl = models.CharField(max_length=2083, null=True, blank=True)


class Collection(models.Model):
    CollectionID = models.AutoField(primary_key=True)
    BrandID = models.ForeignKey("core.Brand", on_delete=models.PROTECT)
    ThemeID = models.ForeignKey("meta.Theme", on_delete=models.PROTECT)
    CollectionName = models.CharField(max_length=35)
    CollectionYear = models.IntegerField()
    IsInfluencerCollaboratoin = models.BooleanField()
    InfluencerName = models.CharField(max_length=25, null=True, blank=True)
    IsIPCollaboration = models.BooleanField()
    IPCollaborationName = models.CharField(max_length=25, null=True, blank=True)
    IsCharity = models.BooleanField()
    CharityName = models.CharField(max_length=25, null=True, blank=True)


class Event(models.Model):
    EventID = models.AutoField(primary_key=True)
    EventName = models.CharField(max_length=25)
    EventDescription = models.CharField(max_length=80)
    StartDate = models.DateField(null=True, blank=True)
    EndDate = models.DateField(null=True, blank=True)
    OrganizerID = models.ForeignKey("meta.Organizer", on_delete=models.PROTECT)
    ThemeID = models.ForeignKey("meta.Theme", on_delete=models.PROTECT)
