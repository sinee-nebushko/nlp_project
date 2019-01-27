from django.db import models


class Article(models.Model):
    content = models.TextField()

    class Meta:
        app_label = "text-form-field-text"

    def __str__(self):
        return self.content
