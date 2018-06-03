from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=32)
    text = models.TextField()
    image = models.ImageField(upload_to='image', blank=True, null=True)

    def __str__(self):
        return self.title
