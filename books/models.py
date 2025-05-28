from django.db import models

class Book(models.Model):
    STATUS_CHOICES = [
        ('reading', 'Lendo'),
        ('toread', 'Quero ler'),
        ('finished', 'Lido'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.author}"