from library.models import Review, Book

class BookService:

    @staticmethod
    def calc_avg_rating(book_id):
        reviews = Review.objects.filter(book_id=book_id)

        if not reviews.exists():
            return None

        total_rating = sum(review.rating for review in reviews)
        avg_rating = total_rating / reviews.count()

        return avg_rating

    @staticmethod
    def is_popular(book_id, threshold=4):
        avg_rating = BookService.calc_avg_rating(book_id)

        if avg_rating is None:
            return None

        return avg_rating >= threshold