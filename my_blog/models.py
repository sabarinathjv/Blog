from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):#shows title instead of object
        return self.title

