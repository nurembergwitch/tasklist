from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


'''GENRE_CHOICES = (
    ('CRIME', 'CRIME'),
    ('NON_FICTION', 'Non Fiction'),
    ('OTHER', 'Other'),
    ('SCI_FI', "Sci Fi"),
)'''


class Book(models.Model):
    class GenreChoices(models.TextChoices):
        CRIME = 'C', 'Crime'
        NON_FICTION = 'N', 'Non Fiction'
        OTHER = 'O', 'Other'
        SCI_FI = 'S', "Sci Fi"

    name = models.CharField(max_length=200)
    price = models.FloatField()
    number_in_stock = models.PositiveIntegerField(default=0)
    genre = models.CharField(max_length=100, choices=GenreChoices.choices)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.name


# making my shitty to-do list here

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    desc = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.desc
