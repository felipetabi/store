from django.db import models

# Create your models here.
class Categories(models.Model):
    title = models.Charfield(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title