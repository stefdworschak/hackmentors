from django.db import models
import uuid


class SnapPaddyImage(models.Model):
    """ Represents an image created by a user """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    cutout = models.CharField(max_length=255, default='')
    base64image = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
    
    def __str__(self):
        return str(self.uuid)
