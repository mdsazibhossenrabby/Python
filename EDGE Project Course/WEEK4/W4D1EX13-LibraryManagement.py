
from matplotlib.style import library


class Library:

    def __init__(self):
        self.books=[]

    def addBook(self,book):
        self.books.append(book)
        print(f"The book {book} added to the library")

    def removeBook(self,book):
        if book in self.books:
            self.books.remove(book)
            print(f"The book {book} rempoves from the library")
        else :
            print(f"The book {book} not found in the library")

    def displayBooks(self):
        print(f"Books in the Library : {self.books}")


library=Library()
library.addBook("The Grat Gatsby")
library.displayBooks()
library.removeBook("1987")