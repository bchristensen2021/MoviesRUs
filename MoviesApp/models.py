from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=1, unique=True)
    description = models.CharField(max_length=25)

    class Meta:
        db_table = "category"

    def __str__(self):
        return (self.description)    
 
class Rating(models.Model):
    rating = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=30)
    
    class Meta:
        db_table = "rating"

    def __str__(self):
        return (self.description) 

class Movie(models.Model):
    title = models.CharField(max_length=75)
    year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    rating = models.ForeignKey(Rating, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "movie"

    def __str__(self):
        return (self.title)