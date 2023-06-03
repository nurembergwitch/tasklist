import django_filters
from .models import Book

'''by default search only filters items with the exact match, it sucks
fields = ['name', 'author__name', 'price', 'genre']
'''


class BookFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()

    class Meta:
        model = Book
        fields = {
            'name': ['icontains'],  # or istartswith
            'author__name': ['icontains'],
            # 'price': ['lt', 'gt'],
            'genre': ['exact']}
