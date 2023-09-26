from django.db import models

class Product(models.Model):
    name = models.CharField(verbose_name="product_name", max_length=60)
    short_name = models.CharField(verbose_name="short_name", max_length=20, default="Energy Saving")
    srt_desc = models.CharField(verbose_name="short_description", max_length=288)
    desc = models.TextField(verbose_name="html")

    def __str__(self):
        return self.name