from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
rating = ((0, '0-No'),
         (1, '1-Little bit'),
         (2, '2-Recognisable'),
         (3, '3-Moderate'),
         (4, '4-high'),
         (5, '5-Intense'))

alphabet = RegexValidator(r'^[A-Za-z]*$','only alphabet')

class Blend(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=20, validators=[alphabet])
    city = models.CharField(max_length=30, validators=[alphabet])
    altitude = models.IntegerField()
    description = models.CharField(max_length=700)
    processing = models.CharField(max_length=200)
    characteristics = models.CharField(max_length=200)
    img = models.ImageField(upload_to='gallery',null=True)

    def __str__(self):
        return self.name

class Batch(models.Model):
    Blend = models.ForeignKey(Blend, on_delete=models.CASCADE)
    Batch_No = models.IntegerField()

    def __str__(self):
        return '%s - %s' %(self.Blend.name, self.Batch_No)

class Profile(models.Model):
    Blend_Batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    Acidic = models.FloatField()
    Sweet = models.FloatField()
    Salty = models.FloatField()
    Floral = models.FloatField()
    Chocolaty = models.FloatField()
    Nutty = models.FloatField()
    Bitter = models.FloatField()
    Savoury = models.FloatField()
    Spicy = models.FloatField()
    Berries = models.FloatField()

class TasteProfile(models.Model):
    Blend_Batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    Img = models.ImageField(upload_to="gallery", null=True)

class Profile_Review(models.Model):
    blend_Batch_Id = models.ForeignKey(Batch, on_delete=models.CASCADE)
    User_Id = models.CharField(max_length=100)
    Acidic = models.IntegerField(choices=rating, default=0)
    Sweet = models.IntegerField(choices=rating, default=0)
    Salty = models.IntegerField(choices=rating, default=0)
    Floral = models.IntegerField(choices=rating, default=0)
    Chocolaty = models.IntegerField(choices=rating, default=0)
    Nutty = models.IntegerField(choices=rating, default=0)
    Bitter = models.IntegerField(choices=rating, default=0)
    Savoury = models.IntegerField(choices=rating, default=0)
    Spicy = models.IntegerField(choices=rating, default=0)
    Berries = models.IntegerField(choices=rating, default=0)

    def get_absolute_url(self):
        return "/data"

class Gen_Review(models.Model):
    Blend_Batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    review = models.TextField()

    def get_absolute_url(self):
        return "/data"
