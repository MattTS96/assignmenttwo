from django.db import models


class iframes(models.Model):
    iframe_detail = models.TextField(max_length=5000)