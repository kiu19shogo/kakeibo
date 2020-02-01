from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:

        db_table = "category"

    category_name = models.CharField(max_length=255, unique=True)
    