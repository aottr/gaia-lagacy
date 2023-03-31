from django.db import models
from django.urls import reverse
from .utils import SubOrders, Gender


class Species(models.Model):

    name = models.CharField(
        max_length=150, help_text='Enter the name of the species')
    suborder = models.IntegerField(
        choices=SubOrders.choices(), default=SubOrders.Snake)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=255)
    path = models.FileField(upload_to='ark/files/%Y/')
    created_at = models.DateTimeField(auto_now_add=True)


class Animal(models.Model):

    name = models.CharField(max_length=200, blank=True,
                            help_text='Give your animal a name.')
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='ark/img/animals/', blank=True)
    notes = models.TextField(blank=True)
    birth_date = models.DateField(auto_now_add=True)
    gender = models.PositiveSmallIntegerField(
        choices=Gender.choices(), default=Gender.Male)
    captive_bred = models.BooleanField(default=True)
    weight = models.IntegerField(
        default=0, help_text='Weight of the animal in grams.')
    size = models.IntegerField(
        default=0, help_text='Size of the animal, height or length, in mm.')
    origin = models.CharField(
        max_length=100, blank=True, help_text='In what country was the animal born.')
    identification_number = models.CharField(
        max_length=255, blank=True, help_text='i-fap or other identification register.')
    dossier = models.ManyToManyField(
        File, blank=True, help_text='Any kinds of papers of the animal.')
