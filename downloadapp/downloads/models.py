from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/photos')


class FileAdmin(models.Model):
    adminUpload = models.FileField(upload_to='media')
    title = models.CharField(max_length=200, null=True)
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
