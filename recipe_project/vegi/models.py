from django.db import models

class Receipe(models.Model):
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.receipe_name
