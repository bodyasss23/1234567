from django.db import models
from django.core.exceptions import ValidationError

VALID_BREEDS = ["Abyssinian", "Bengal", "Persian", "Siberian", "Siamese"]

def validate_breed(value):
    if value not in VALID_BREEDS:
        raise ValidationError(f"{value} is not a recognized breed.")

class SpyCat(models.Model):
    name = models.CharField(max_length=255)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=255, validators=[validate_breed])
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Mission(models.Model):
    cat = models.ForeignKey(SpyCat, null=True, blank=True, on_delete=models.SET_NULL, related_name="missions")
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Mission {self.id}"

class Target(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name="targets")
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
