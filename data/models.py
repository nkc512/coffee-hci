from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.conf import settings
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
    price=models.FloatField(default=340)
    slug = models.SlugField()
    def __str__(self):
        return self.name

class Batch(models.Model):
    blend = models.ForeignKey(Blend, on_delete=models.CASCADE)
    batch_no = models.IntegerField()

    def __str__(self):
        return '%s - %s' %(self.blend.name, self.batch_no)

class Profile(models.Model):
    blend_batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    acidic = models.FloatField()
    sweet = models.FloatField()
    salty = models.FloatField()
    floral = models.FloatField()
    chocolaty = models.FloatField()
    nutty = models.FloatField()
    bitter = models.FloatField()
    savoury = models.FloatField()
    spicy = models.FloatField()
    berries = models.FloatField()

class TasteProfile(models.Model):
    blend_batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="gallery", null=True)

class Profile_Review(models.Model):
    blend_batch_id = models.ForeignKey(Batch, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100)
    acidic = models.IntegerField(choices=rating, default=0)
    sweet = models.IntegerField(choices=rating, default=0)
    salty = models.IntegerField(choices=rating, default=0)
    floral = models.IntegerField(choices=rating, default=0)
    chocolaty = models.IntegerField(choices=rating, default=0)
    nutty = models.IntegerField(choices=rating, default=0)
    bitter = models.IntegerField(choices=rating, default=0)
    savoury = models.IntegerField(choices=rating, default=0)
    spicy = models.IntegerField(choices=rating, default=0)
    berries = models.IntegerField(choices=rating, default=0)

    def get_absolute_url(self):
        return "/data"

class Gen_Review(models.Model):
    blend_batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    review = models.TextField()

    def get_absolute_url(self):
        return "/data"

class Item(models.Model):
    title=models.ForeignKey(Blend,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("core:product", kwargs={"slug": self.slug})
    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={"slug": self.slug})
        


class OrderItem(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return self.item

class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)
    startdate=models.DateTimeField(auto_now_add=True)
    ordered_date=models.DateTimeField()
    ordered=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
'''
class Cart(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    order_date = models.DateField(null=True)
    payment_type = models.CharField(max_length=100, null=True)
    payment_id = models.CharField(max_length=100, null=True)

    def __unicode__(self): 
            return "%s" % (self.user)

    def add_to_cart(self, name):
        coffee = Blend.objects.get(pk=name)
        try:
            preexisting_order = CoffeeOrder.objects.get(coffee=coffee, cart=self)
            preexisting_order.quantity += 1
            preexisting_order.save()
        except CoffeeOrder.DoesNotExist:
            new_order = CoffeeOrder.objects.create(
                coffee=coffee,
                cart=self,
                quantity=1
                )
            new_order.save()

            def __unicode__(self):
                return "%s" % (self.book_id)


    def remove_from_cart(self, name):
        coffee = Blend.objects.get(pk=name)
        try:
            preexisting_order = BookOrder.objects.get(coffee=coffee, cart=self)
            if preexisting_order.quantity > 1:
                preexisting_order.quantity -= 1
                preexisting_order.save()
            else:
                preexisting_order.delete()
        except CoffeeOrder.DoesNotExist:
            pass    
'''