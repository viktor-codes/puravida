from django.db import models


class Subscribers(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email


class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title
