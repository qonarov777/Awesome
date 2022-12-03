from django.db import models

class Starthome(models.Model):
    title= models.CharField( max_length=50)
    text1= models.CharField(max_length=50)
    text2= models.CharField(max_length=50)
    text3= models.CharField(max_length=50)
    # image=models.ImageField(upload_to='media/Start home/')
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name ='Home'
        verbose_name_plural='Home'
      
class Startteam(models.Model):
    image= models.ImageField (upload_to='media/Start team')
    name= models.CharField(max_length=50)
    job=models.CharField( max_length=50)
    text= models.CharField( max_length=500)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name ='Team'
        verbose_name_plural='Team'
        
class Startportfolio(models.Model):
    image= models.ImageField (upload_to='media/Start porfolio')
    number= models.CharField(max_length=50)
    text= models.CharField( max_length=500)
    
    def __str__(self):
        return self.number
    
    class Meta:
        verbose_name ='Portfolio'
        verbose_name_plural='Portfolio'
        
class Startme(models.Model):
    email=models.EmailField( max_length=254)
    phone= models.IntegerField()
    facebook=models.CharField( max_length=50)
    twitter=models.CharField(max_length=50)
    instagram=models.CharField( max_length=50)
    telegram=models.CharField( max_length=50)
    location= models.CharField(max_length=500)
    
    def __str__(self):
        return self.location
    
    class Meta:
        verbose_name ='Address'
        verbose_name_plural='Address'