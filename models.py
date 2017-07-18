from django.db import models
from datetime import datetime

# Create your models here.
class Boards(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    create_date = models.DateTimeField(default = datetime.now())

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=255, null=False)
    create_date = models.DateTimeField(default = datetime.now())
    board = models.ForeignKey('Boards', on_delete = models.CASCADE, related_name = 'board_id')
    def __str__(self):
        return self.content
