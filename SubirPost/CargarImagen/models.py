from django.db import models


# Tabla Posts.
class Posts(models.Model):
    image = models.ImageField(upload_to='images/')
    comment = models.TextField()
