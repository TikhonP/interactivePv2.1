from django.db import models

# Create your models here.
class Poem(models.Model):
    title = models.CharField(max_length=150, default="Без названия.")
    ended = models.BooleanField(default=False)

class Paragraph(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=50, default="Анон")
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)