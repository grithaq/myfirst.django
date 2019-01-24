from django.db import models

# Create your models here.
# class Book(models.Model):
#     title =models.CharField (max_length=100)
#     author =models.CharField(max_length=100)
#     pdf = models.Field()

#     def __str__(self):
#         return self.title

class Topic(models.Model):
    top_name=models.CharField(max_length= 100 , unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    category=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name =models.CharField(max_length =246)
    url =models.URLField()

    def __str__(self):
        return self.name

class AccesRecord(models.Model):
    name= models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date =models.DateField()

    def __str__(self):
        return self.date    