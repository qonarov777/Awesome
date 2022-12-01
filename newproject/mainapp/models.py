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
      
      
class Startabout(models.Model):
    title=models.CharField(max_length=50)
    text= models.CharField( max_length=1000)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name ='Start about'
        verbose_name_plural='Start about'
        
        