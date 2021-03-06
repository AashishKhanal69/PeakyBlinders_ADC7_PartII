from django.db import models
from django.conf import settings 

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.PROTECT)
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestap = models.DateTimeField(auto_now=False, auto_now_add=True)
    files = models.FileField(upload_to='')

    def __str__(self):
        return self.title     

                                                                                   
