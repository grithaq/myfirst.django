from django.db import models

# Create your models here.
# class Book(models.Model):
#     title =models.CharField (max_length=100)
#     author =models.CharField(max_length=100)
#     pdf = models.Field()

#     def __str__(self):
#         return self.title

# class Topic(models.Model):
#     top_name=models.CharField(max_length= 100 , unique=True)

#     def __str__(self):
#         return self.top_name

# class Webpage(models.Model):
#     category=models.ForeignKey(Topic,on_delete=models.CASCADE)
#     name =models.CharField(max_length =246)
#     url =models.URLField()

#     def __str__(self):
#         return self.name

# class AccesRecord(models.Model):
#     name= models.ForeignKey(Webpage,on_delete=models.CASCADE)
#     date =models.DateField()

#     def __str__(self):
#         return self.date    


class Person(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    ttl = models.CharField(max_length=60)
    no_telp=models.CharField(max_length=15)
    email = models.EmailField()

class Partai(models.Model):
    nama_partai = models.CharField(max_length=45)
    kode_partai = models.IntegerField()
    gambar_partai =models.ImageField()

class KategoriCaleg(models.Model):
    kategori = models.CharField(max_length=100)

    def __str__(self):
        return self.kategori

class Dapil(models.Model):
    nama_dapil =models.CharField(max_length=50)
    daerah_dapil = models.IntegerField()
    provinsi = models.CharField(max_length=50)
    kota= models.CharField(max_length = 50)
    kab=models.CharField(max_length=50)
    kec=models.CharField(max_length = 50)

# master
class Caleg(models.Model):
    nama = models.CharField(max_length=100)
    no_urut = models.IntegerField()

    partai= models.ForeignKey(Partai,on_delete=models.CASCADE)
    kategori = models.ForeignKey(KategoriCaleg,on_delete=models.CASCADE)
    dapil = models.ForeignKey(Dapil,on_delete=models.CASCADE)