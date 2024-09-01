class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = False

    def borrow_book(self):
        self.borrowed = True

    def return_book(self):
        self.borrowed = False

    def display_info(self):
        status = 'Borrowed' if self.borrowed else 'Available'
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Status: {status}")

class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.borrowed:
            book.borrow_book()
            self.borrowed_books.append(book)
        else:
            print("Book is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print("Book not found in borrowed list.")

    def display_info(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        print(f"Member ID: {self.member_id}, Name: {self.name}")
        print("Borrowed Books:", ", ".join(borrowed_titles))

# Example usage:
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

member = LibraryMember(1, "Alice Smith")
member.borrow_book(book1)
member.borrow_book(book2)

book1.display_info()
book2.display_info()
member.display_info()

member.return_book(book1)
book1.display_info()
member.display_info()
