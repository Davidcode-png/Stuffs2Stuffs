from django.utils import timezone
from django.db import models

class FileManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(
            upload_date__gte=timezone.now()-timezone.timedelta(minutes=1)
        ).delete()