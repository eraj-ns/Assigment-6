class Book:
    total_books = 3

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")
