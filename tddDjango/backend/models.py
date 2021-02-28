from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Offer(models.Model):
    customer_name = models.CharField(max_length=100,null=True,help_text="What is the name of the client?")
    # na mpei kapoia stigmh auto email = models.EmailField()
    description = models.CharField(max_length=500,null=True,help_text="put a description for this offer")
    number = models.IntegerField(null=True,help_text="How many pieces does the customer want")     #number of temaxia
    extra_price = models.FloatField(default=0)

    def __str__(self):
        # allParameters = self.parameter_set.all()
        # text = str([parameter+"-" for parameter in allParameters])
        # print(text)
        return self.customer_name+" asked for "+str(self.number)+" pieces"

    @property
    def get_all_parameters_in_offer(self):
        allParameters = self.parameter_set.all()
        return allParameters[::1]
    
    @property
    def get_offer_total_price(self):
        allParameters = self.parameter_set.all()
        total = self.extra_price + sum ([par.get_parameter_total for par in allParameters])
        return total

class Parameter(models.Model):
    offer = models.ManyToManyField(Offer)
    name = models.CharField(max_length=100,null=True)
    # price = models.FloatField(null=True)  #mallon de to xreiazomai ayto
    description = models.CharField(max_length=300,null=True)
    extra_price = models.FloatField(default=0)   #one field for the user to add to the price manually
      
    def __str__(self):
        allDetails = self.detail_set.all()
        text = str([str(detail)+"-" for detail in allDetails])
        return self.name+" ("+str(self.description)+"-"+text+") "
    
    @property
    def get_all_details_in_offer(self):
        alldetails = self.detail_set.all()
        return alldetails[::1]
    
    @property
    def get_parameter_total(self):
        allDetails = self.detail_set.all()
        total = self.extra_price + sum([detail.price for detail in allDetails])
        return total

class Detail(models.Model):
    parameter = models.ManyToManyField(Parameter)
    name = models.CharField(max_length=100,null=True)   #name of the detail of the parameter e.g: dimensions,ontoule
    #category might be a string or a dict we'll see or a property finally
    category = models.CharField(max_length=100,null=True,unique=True)  #unique categories for this detail e.g: for dimensions 30x60 or 50x70,for ontoule 2f k-k or 3f x4   
    price = models.FloatField()
    extra_price = models.FloatField(default=0)   #one field for the user to add to the price manually

    def __str__(self):
        return self.name+"-"+self.category
    