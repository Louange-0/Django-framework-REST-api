from django.db import models
class book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title + ' by '+ self.author