from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.http.response import HttpResponse, HttpResponsePermanentRedirect

from .forms import BookNameFilterForm
from .models import Book, Category, Task
from .filters import BookFilter

from django.views.generic.list import ListView
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from django.views.decorators.http import require_http_methods
# ==========


# Create your views here.


def index(request):
    '''name = request.GET.get('name')
    books = Book.objects.all()
    if name:
        books = books.filter(name__icontains=name)'''

    # same thing but w a django extension. Need to create a filters py file for it. When you instantiate the FilterSet class it contains a form w all the fields in the meta attribute, so the form (in context) needs to be changed from the one from forms py
    book_filter = BookFilter(request.GET, queryset=Book.objects.all())
    context = {'form': book_filter.form, 'books': book_filter.qs}
    return render(request, 'index.html', context)


# same thing but with class-based views. Hellish
class BookListView(ListView):
    queryset = Book.objects.all()
    # Book.objects.filter(number_in_stock__gt=0) you can filter these down to only books in stock
    template_name = 'index2.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()  # returns the queryset defined above
        self.filterset = BookFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs  # qs is the queryset after filtering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # form needs to be specified bc its not added by default
        context['form'] = self.filterset.form
        return context


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = (DjangoFilterBackend, )
    filterset_class = BookFilter

# ============================== TASKLIST APP


def my_tasks(request):
    category = request.GET.get('category')
    if category == None:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(category__name=category)
    categories = Category.objects.all()
    context = {'tasks': tasks, 'categories': categories}
    return render(request, 'my_tasks.html', context)


def add_task(request):
    if request.method == 'POST':
        data = request.POST
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != 'none':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        task = Task.objects.get_or_create(
            desc=data['taskdesc'],
            category=category
        )[0]

    tasks = Task.objects.all()
    return render(request, 'partials/task-list.html', {'tasks': tasks})


@require_http_methods(['DELETE'])
def delete_task(request, pk):
    task_to_delete = Task.objects.get(pk=pk)
    # added the csrf token script to base html bc delete requests are exempt
    task_to_delete.delete()
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'partials/task-list.html', context)


def search_task(request):
    search_text = request.POST.get('search')
    results = Task.objects.filter(desc__icontains=search_text)
    context = {'results': results}
    return render(request, 'partials/search-results.html', context)

# =============== HTMX FUCKERY


def colors1(request):
    return HttpResponse("<div id='color-demo' class='smooth' style='color:blue' hx-get='/colors2' hx-swap='outerHTML' hx-trigger='every 1s'>Color Swap Demo</div>")


def colors2(request):
    return HttpResponse("<div id='color-demo' class='smooth' style='color:red' hx-get='/colors1' hx-swap='outerHTML' hx-trigger='every 1s'>Color Swap Demo</div>")


@require_http_methods(['DELETE'])
def fade_out_demo(request):
    return HttpResponse('<p>piss</p>')


def shit(request):
    name = request.POST.get('name')
    return HttpResponse('<p>you shat yourself, %s</p>' % name)
