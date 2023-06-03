from django.core.management.base import BaseCommand
from core.models import Book, Author


class Command(BaseCommand):
    help = 'suck my dick'

    def handle(self, *args, **kwargs):

        plato = Author.objects.get_or_create(name='Plato')[0]
        mirandola = Author.objects.get_or_create(
            name='Pico della Mirandola')[0]
        aquinas = Author.objects.get_or_create(name='Thomas Aquinas')[0]
        cioran = Author.objects.get_or_create(name='Emil Cioran')[0]
        zizek = Author.objects.get_or_create(name='Slavoj Zizek')[0]
        ligotti = Author.objects.get_or_create(name='Thomas Ligotti')[0]
        wallace = Author.objects.get_or_create(name='David Foster Wallace')[0]
        clarke = Author.objects.get_or_create(name='Arthur Clarke')[0]
        smith = Author.objects.get_or_create(name='Scott Smith')[0]

        Book.objects.get_or_create(
            name='The Republic',
            author=plato,
            price=10,
            genre=Book.GenreChoices.NON_FICTION,
            number_in_stock=5
        )

        Book.objects.get_or_create(
            name='On Human Dignity',
            author=mirandola,
            price=12.99,
            genre=Book.GenreChoices.NON_FICTION,
            number_in_stock=15
        )

        Book.objects.get_or_create(
            name='Summa Theologica',
            author=aquinas,
            price=16.50,
            genre=Book.GenreChoices.OTHER,
            number_in_stock=9
        )
        Book.objects.get_or_create(
            name='The Trouble With Being Born',
            author=cioran,
            price=9.99,
            genre=Book.GenreChoices.OTHER,
            number_in_stock=18
        )
        Book.objects.get_or_create(
            name='Pandemic!',
            author=zizek,
            price=15.00,
            genre=Book.GenreChoices.OTHER,
            number_in_stock=9
        )

        Book.objects.get_or_create(
            name='The Conspiracy Against The Human Race',
            author=ligotti,
            price=19.29,
            genre=Book.GenreChoices.NON_FICTION,
            number_in_stock=17
        )

        Book.objects.get_or_create(
            name='Infinite Jest',
            author=wallace,
            price=10,
            genre=Book.GenreChoices.OTHER,
            number_in_stock=8
        )

        Book.objects.get_or_create(
            name='2001 A Space Odyssey',
            author=clarke,
            price=10,
            genre=Book.GenreChoices.SCI_FI,
            number_in_stock=20
        )

        Book.objects.get_or_create(
            name='A Simple Plan',
            author=smith,
            price=11.49,
            genre=Book.GenreChoices.CRIME,
            number_in_stock=8
        )
