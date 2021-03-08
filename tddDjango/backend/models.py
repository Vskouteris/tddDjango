from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Detail(models.Model):
    CATEGORY_OPTIONS = [
        ('HOURS', 'HOURS'),
        ('DIMENSIONS', 'DIMENSIONS'),
        ('TYPE', 'TYPE'),
        ('EXTRA', 'EXTRA'),
        ('ONTOULE', 'ONTOULE')
    ]
    # parameter = models.ManyToManyField(Parameter)
    name = models.CharField(max_length=100,null=True)   #name of the detail of the parameter e.g: dimensions,ontoule
    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=255,default=CATEGORY_OPTIONS[0])
    price = models.FloatField()
    extra_price = models.FloatField(default=0)   #one field for the user to add to the price manually

    def __str__(self):
        return self.name+"-"+self.category

class Parameter(models.Model):
    details= models.ManyToManyField(Detail,help_text="choose all Details affecting the parameter",blank=True)
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=300,null=True)
    extra_price = models.FloatField(default=0)   #one field for the user to add to the price manually
      
    def __str__(self):
        try:
            text = self.name+" ("+str(self.description) +" )"
        except:
            text = str(self.name)
        return text

    @property
    def get_parameter_total(self):
        allDetails = self.details.all()
        total = self.extra_price + sum([detail.price for detail in allDetails])
        return total    

class Offer(models.Model):
    parameters= models.ManyToManyField(Parameter,help_text="choose all parameters affecting the offer",blank=True)
    customer_name = models.CharField(max_length=100,null=True,help_text="What is the name of the client?")
    # na mpei kapoia stigmh auto email = models.EmailField()
    description = models.CharField(max_length=500,null=True,help_text="put a description for this offer")
    number = models.IntegerField(null=True,help_text="How many pieces does the customer want")     #number of temaxia
    extra_price = models.FloatField(default=0)


    def __str__(self):
        return self.customer_name+" asked for "+str(self.number)+" pieces"

    @property
    def get_all_parameters_in_offer(self):
        allParameters = self.parameters.all()
        return allParameters[::1]
    
    @property
    def get_offer_total_price(self):
        allParameters = self.parameters.all()
        total = self.extra_price + sum ([par.get_parameter_total for par in allParameters])
        return total
