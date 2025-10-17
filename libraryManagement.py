import csv
import os

class Book:
    def __init__(self,title,author,isbn):
        self.title= title
        self.author= author
        self.isbn= isbn
        self.available= True

    def __str__(self):
        status= "Available" if self.available else "Issued"
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | {status}"
    
class Library:
    def __init__(self, filename='books_data.csv'):
        self.filename= filename
        self.books= []
        self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r',newline='', encoding='utf-8') as file:
                reader=csv.DictReader(file)
                for row in reader:
                    book=Book(row['title'], row['author'], row['isbn'],row['available']== 'True')
                    self.books.append(book)

    def save_books(self):
        with open(self.filename,'w',newline='',encoding='utf-8')as file:
            fieldnames=['title','author','isbn','available']
            writer= csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for book in self.books:
                writer.writerow({
                    'title': book.title,
                    'author': book.author,
                    'isbn': book.isbn,
                    'available': book.available
                })

    def add_book(self,book):
        self.books.append(book)
        self.save_books()
        print(f'✅ Book "{book.title}" added successfully!')

    def display_books(self):
        if not self.books:
            print("⚠️ No books in the library. ")
        else:
            for book in self.books:
                print(book)

    def issue_book (self,isbn):
        for book in self.books:
            if book.isbn == isbn :
                if book.available:
                    book.available= False
                    self.save_books()
                    print(f'📕 Book "{book.title}" has been issued. ')
                    return
                else:
                    print("❌ Book is already issued. ")
                    return
        print("❌ Book not found!")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn :
                if not book.available:
                    book.available= True
                    self.save_books()
                    print(f'📗 Book "{book.title}" returned successfully.')
                    return
                else:
                    print("⚠️ Book was not issued. ")
                    return
        print("❌ Book not found!")

def menu():
    library=Library()

    while True:
        print("\n=== Library Management System ===")
        print("1. Add book")
        print("2. Display books")
        print("3. Issue book")
        print("4. Return book")
        print("5. Exit")

        choice= input("Enter your choice(1-5): ")

        if choice== '1' :
            title= input("Enter book title: ")
            author= input("Enter author name: ")
            isbn= input("Enter ISBN: ")
            new_book=Book(title,author,isbn)
            library.add_book(new_book)

        elif choice== '2' :
            library.display_books()

        elif choice== '3' :
            isbn= input("Enter ISBN of the book to issue: ")
            library.issue_book(isbn)

        elif choice== '4' :
            isbn= input("Enter ISBN of the book to return:  ")
            library.return_book(isbn)

        elif choice=='5' :
            print("👋 Exiting... Thank you for using the Library Management System!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()