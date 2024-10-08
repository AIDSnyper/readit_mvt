from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=404)
    email = models.EmailField()
    subject = models.CharField(max_length=404)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
