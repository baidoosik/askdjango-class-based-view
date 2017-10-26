from django.db import models

# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStamp):
    title = models.CharField(max_length=200)
    contents = models.TextField()
