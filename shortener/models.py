from hashlib import md5

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import HttpResponse

from actuate_shortener.settings import SITE_ID


class URL(models.Model):
    long_url = models.URLField(unique=True)
    short_url = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    hash = models.CharField(max_length=10, unique=True)

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            hash_sufix = md5(self.long_url.encode()).hexdigest()[:10]
            self.hash = hash_sufix
            self.short_url = f'{SITE_ID}{hash_sufix}'

        validate = URLValidator()
        try:
            validate(self.long_url)
        except ValidationError as e:
            raise HttpResponse(status=500, reason=f'Invalid url: {e}')

        return super().save(*args, **kwargs)
