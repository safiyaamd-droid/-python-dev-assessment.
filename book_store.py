class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        """Return the age of the book assuming current year is 2025."""
        return 2025 - self.publication_year

    def get_summary(self):
        """Return a summary string of the book."""
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


# Example usage
if __name__ == "__main__":
    # Create two book objects
    book1 = Book("1984", "George Orwell", "9780451524935", 1949)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780060935467", 1960)

    # Print details
    for book in [book1, book2]:
        print("Title:", book.title)
        print("Author:", book.author)
        print("Age:", book.get_age(), "years")
        print("Summary:", book.get_summary())
        print()

