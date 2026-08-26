from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from library.models import Book, Author

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView, View

from library.forms import AuthorForm, BookForm

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from library.services import BookService

# from students.models import Student1
# from students.services import StudentService

# class Student1DetailView(DetailView):
#     model = Student1
#     template_name = 'students/student_detail111.html'
#     context_object_name = 'student'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         student_id = self.object.id
#
#         context['full_name'] = StudentService.get_full_name(student_id)
#         context['avg_score'] = StudentService.calculate_avg_score(student_id)
#         context['has_passed'] = StudentService.has_passed(student_id)
#
#         return context


class ReviewBookView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)

        if not request.user.has_perm('library.can_review_book'):
            return HttpResponseForbidden('У вас нет права для рецензирования книги.')

        book.review = request.POST.get('review')
        book.save()

        return redirect('library:book_detail', pk=pk)


class RecommendBookView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)

        if not request.user.has_perm('library.can_recommend_book'):
            return HttpResponseForbidden('У вас нет права для рекомендации книги.')

        book.recommend = True
        book.save()

        return redirect('library:book_detail', pk=pk)


# Create your views here.

# def book_list(request):
#     """"""
#     books = Book.objects.all()
#     context = {
#          'books':books,
#     }
#     return render(request, 'library/books_list.html', context=context)
#
#
# def book_detail(request, book_id):
#     """"""
#     book = Book.objects.get(id=book_id)
#     context = {
#          'book':book,
#     }
#     return render(request, 'library/book_detail.html', context=context)


class AuthorListView(ListView):
    model = Author
    template_name = 'library/authors_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        queryset = cache.get('authors_queryset')

        if not queryset:
            queryset = super().get_queryset()
            cache.set('authors_queryset', queryset, 60 * 15)

        return queryset


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_form.html'
    success_url = reverse_lazy('library:authors_list')
    login_url = 'users:login'


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_form.html'
    success_url = reverse_lazy('library:authors_list')
    login_url = 'users:login'


@method_decorator(cache_page(60 * 15), name='dispatch')
class BookListView(LoginRequiredMixin, ListView):
    """"""
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(publication_data__year__gt=1000)

class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """"""
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:books_list')
    login_url = 'users:login'
    permission_required = 'library.add_book'


@method_decorator(cache_page(60 * 15), name='dispatch')
class BookDetailView(LoginRequiredMixin, DetailView):
    """"""
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'


    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        print(context)
        context['author_books_count'] = Book.objects.filter(author=self.get_object().author).count()
        print(context)

        book_id = self.object.id
        context['avg_rating'] = BookService.calc_avg_rating(book_id)
        context['is_popular'] = BookService.is_popular(book_id)

        return context


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """"""
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:books_list')
    login_url = 'users:login'
    permission_required = 'library.change_book'


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """"""
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy('library:books_list')
    permission_required = 'library.delete_book'




