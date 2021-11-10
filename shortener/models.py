from hashlib import md5

from django.db import models


class URL(models.Model):
    long_url = models.URLField(unique=True)
    short_url = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.short_url = md5(self.long_url.encode()).hexdigest()[:10]

        return super().save(*args, **kwargs)
