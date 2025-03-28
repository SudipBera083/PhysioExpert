from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='packages/', null=True, blank=True)

    def __str__(self):
        return self.name


class About(models.Model):
    header = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', null=True, blank=True)

    def __str__(self):
        return self.header
    



class Review(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField(default=5)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} Stars"
