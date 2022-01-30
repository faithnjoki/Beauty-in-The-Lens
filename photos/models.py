from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null="true")
    description = models.TextField()
    image = models.ImageField(null ="false",blank ="false")

    def __str__(self):
        return self.description
