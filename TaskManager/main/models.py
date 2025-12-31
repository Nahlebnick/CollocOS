from django.db import models

class Task(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(blank=True)

    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='todo'
    )

    def __str__(self):
        return self.title
