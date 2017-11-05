from django.db import models
from django.urls import reverse

# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStamp):
    title = models.CharField(max_length=200)
    contents = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])