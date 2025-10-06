class Book:
    def __init__(self, _book):
        self._book = _book
        self.title = _book.title
        self.author = _book.author
        self._is_checked_out = _book._is_checked_out
        return _book(self)
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def check_out_book(self, title):
        if title in [book.title for book in self.books if not book._is_checked_out]:
            for book in self.books:
                if book.title == title and not book._is_checked_out:
                    book._is_checked_out = True
                    return f'You have checked out "{title}".'
    def return_book(self, title):
        for book in self.books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return f'You have returned "{title}".'
        return f'"{title}" was not checked out.'
    def list_available_books(self):
        available_books = [book.title for book in self.books if not book._is_checked_out]
        return available_books if available_books else "No books available."