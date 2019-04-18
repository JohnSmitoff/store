from django.db import models

# Create your models here.


class Owner(models.Model):
    OWNER_SEX = (("M", "Mail"), ("F", "Femail"))
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    owner_sex = models.CharField(max_length=1, choices=OWNER_SEX)
    image_url = models.URLField(default='http://skandalno.net/wp-content/uploads/2014/02/Boiko-Borisov-1.jpg')

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}\n"
            f"sex: {self.owner_sex}\n"
            f"id - {self.pk}"
        )


class Animal(models.Model):
    KIND_CHOICES = (("D", "Dog"), ("C", "Cat"))

    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=20)
    description = models.TextField()
    image_url = models.URLField()
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} and I am a {self.kind} - {self.age} years old with owner - ({self.owner})"
