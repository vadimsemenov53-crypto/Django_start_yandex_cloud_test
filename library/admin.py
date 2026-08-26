from django.contrib import admin

# Register your models here.

from.models import Author, Book, Review

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """"""
    list_display = ('first_name', 'last_name', 'birth_date',)
    list_filter = ('last_name',)
    search_fields = ('first_name', 'last_name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """"""
    list_display = ('title', 'publication_data', 'author',)
    list_filter = ('publication_data', 'author',)
    search_fields = ('title', 'author__first_name', 'author__last_name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating',)
