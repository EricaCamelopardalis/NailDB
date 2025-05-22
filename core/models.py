from django.db import models


# Create your models here.
class Polish(models.Model):
    PolishID = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=80)
    Price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    BrandID = models.ForeignKey("Brand", on_delete=models.PROTECT)
    ToneID = models.ForeignKey("Tone", on_delete=models.PROTECT)
    UndertoneID = models.ForeignKey("Undertone", on_delete=models.PROTECT)
    OpacityID = models.ForeignKey("Opacity", on_delete=models.PROTECT)
    LineID = models.ForeignKey("Line", on_delete=models.PROTECT)
    EventID = models.ForeignKey("Event", on_delete=models.SET_NULL, null=True)
    CollectionID = models.ForeignKey("Collection", on_delete=models.SET_NULL, null=True)
    IsDriesMatte = models.BooleanField(default=False)
    IsGlowIntheDark = models.BooleanField(default=False)
    IsUV = models.BooleanField(default=False)
    IsTopper = models.BooleanField(default=False)
    IsThermal = models.BooleanField(default=False)
