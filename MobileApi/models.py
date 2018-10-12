from django.db import models

# Create your models here.

class RecommendedItems(models.Model):
    ItemID=models.CharField(max_length=1000)
    ItemName=models.CharField(max_length=1000)
    TimeStamp=models.CharField(max_length=1000)

    def __str__(self):
        return self.ItemID


