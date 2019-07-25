from django.db import models

# Create your models here.
class Shop (models.Model):
    item = models.CharField(max_length=225)
    photo = models.URLField(max_length=225)
    harga = models.CharField(max_length=100)
    deskripsi = models.TextField()
    def __str__(self):
        return self.nama

