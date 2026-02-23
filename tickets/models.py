from django.db import models

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')

    def __str__(self):
        return self.title