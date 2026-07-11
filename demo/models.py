from django.db import models


class Notice(models.Model):
    PRIORITY_CHOICES = [
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="Medium"
    )
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
