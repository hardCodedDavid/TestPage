# Create a Book class with title, author, num_pages, and book_type
# properties, and a print_info method to print the book's information.
class Book:
    def __init__(self, title, author, num_pages, book_type):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.book_type = book_type
    
    def print_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of Pages: {self.num_pages}")
        print(f"Type: {self.book_type}")
        print()
        
# Create a Library class with an empty books list, and add_book, print_books, 
# and borrow_book methods.
class Library:
    def __init__(self):
        self.books = []

    # Implement the add_book method to add a Book instance to the books list. 
    def add_book(self, book):
        self.books.append(book)

    # Implement the print_books method to loop through the books 
    # list and call the print_info method on each book instance.    
    def print_books(self):
        for book in self.books:
            book.print_info()

    # Implement the borrow_book method to loop through the books list, and return the Book 
    # instance with a matching title, if found.        
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return book
        return None

# Main program
if __name__ == '__main__':
    # Create the library
    my_library = Library()
    
    # Read the books from file and add them to the library
    with open("books.txt") as f:
        for line in f:
            title, author, num_pages, book_type = line.strip().split(",")
            my_library.add_book(Book(title, author, int(num_pages), book_type))
    
    # Print all the books in the library
    print("Books in the library:")
    my_library.print_books()
    
    # Borrow a book from the library
    while True:
        title = input("Enter the title of the book you want to borrow: ")
        book = my_library.borrow_book(title)
        if book:
            print(f"You have borrowed {book.title}")
            break
        else:
            print("Sorry, that book is not in the library. Please try again.")
    
    # Print all the books in the library again
    print("Books in the library after borrowing:")
    my_library.print_books()
