from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy

User = get_user_model()


class Links(models.Model):
    objects = models.Manager()

    full_link = models.URLField(unique=True)
    short_link = models.CharField(max_length=200, unique=True, db_index=True)
    users = models.ManyToManyField(User, related_name="links")

    def __str__(self):
        return self.short_link

    def get_absolute_url(self):
        return reverse_lazy("short:link", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "link"
        verbose_name_plural = "links"
        ordering = ["id"]
