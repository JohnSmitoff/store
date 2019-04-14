from django.db import models

# Create your models here.


class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"owner_id -> {self.pk} : name - {self.first_name} {self.last_name} "


class Animal(models.Model):
    KIND_CHOICES = (("D", "Dog"), ("C", "Cat"))

    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=20)
    description = models.TextField()
    image_url = models.URLField()
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    owner = models.ForeignKey(Owner, on_delete=None, null=True, blank=True)

    def __str__(self):
        return f"{self.name} and I am a {self.kind} - {self.age} years old with owner - ({self.owner})"
