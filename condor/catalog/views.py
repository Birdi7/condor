from catalog.models import Author, Book, BookInstance, Genre
from django.shortcuts import render


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.count()

    num_instances_available = BookInstance.objects.filter(status__exact="a").count()

    num_authors = Author.objects.count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)
