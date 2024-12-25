"""
    A class to create a graphical user interface for a Library Management System using Tkinter.
    Attributes:
    -----------
    library : Library
        An instance of the Library class to manage library operations.
    root : Tk
        The root window of the Tkinter application.
    title_label : Label
        A label widget to display the title of the application.
    add_button : Button
        A button widget to add a new book to the library.
    display_button : Button
        A button widget to display all books in the library.
    search_button : Button
        A button widget to search for a book in the library.
    checkout_button : Button
        A button widget to check out a book from the library.
    return_button : Button
        A button widget to return a book to the library.
    exit_button : Button
        A button widget to exit the application.
    new_window : Toplevel
        A new window for various operations like adding, searching, checking out, and returning books.
    title_entry : Entry
        An entry widget to input the title of a book.
    author_entry : Entry
        An entry widget to input the author of a book.
    isbn_entry : Entry
        An entry widget to input the ISBN of a book.
    search_entry : Entry
        An entry widget to input the title of a book to search.
    checkout_entry : Entry
        An entry widget to input the title of a book to check out.
    return_entry : Entry
        An entry widget to input the title of a book to return.
    Methods:
    --------
    __init__(root):
        Initializes the LibraryGUI with the root window and sets up the GUI.
    create_widgets():
        Creates and packs the widgets for the main window.
    add_book():
        Opens a new window to add a book to the library.
    add_book_to_library():
        Adds the book to the library and closes the add book window.
    display_books():
        Displays all books in the library in a message box.
    search_book():
        Opens a new window to search for a book in the library.
    search_book_in_library():
        Searches for the book in the library and displays the result in a message box.
    check_out_book():
        Opens a new window to check out a book from the library.
    check_out_book_from_library():
        Checks out the book from the library and displays the result in a message box.
    return_book():
        Opens a new window to return a book to the library.
    return_book_to_library():
        Returns the book to the library and displays the result in a message box.
    """
    import tkinter as tk
from tkinter import messagebox

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
    
    def display_books(self):
        if not self.books:
            return "No books available in the library."
        
        catalog = "\nLibrary Catalog:\n"
        for book in self.books:
            availability = "Available" if book.available else "Checked Out"
            catalog += f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {availability}\n"
        return catalog
    
    def search_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                availability = "Available" if book.available else "Checked Out"
                return f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {availability}"
        return f"Book '{title}' not found in the library."
    
    def check_out_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                if book.available:
                    book.available = False
                    return f"You have checked out '{book.title}'."
                else:
                    return f"'{book.title}' is already checked out."
        return f"Book '{title}' not found in the library."
    
    def return_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                if not book.available:
                    book.available = True
                    return f"You have returned '{book.title}'. Thank you!"
                else:
                    return f"'{book.title}' is already in the library."
        return f"Book '{title}' not found in the library."

class LibraryGUI:
    
    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("Library Management System")
        
        self.create_widgets()
    
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Library Management System", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        
        self.add_button = tk.Button(self.root, text="Add a Book", command=self.add_book, font=("Helvetica", 14))
        self.add_button.pack(pady=5)
        
        self.display_button = tk.Button(self.root, text="Display Books", command=self.display_books, font=("Helvetica", 14))
        self.display_button.pack(pady=5)
        
        self.search_button = tk.Button(self.root, text="Search for a Book", command=self.search_book, font=("Helvetica", 14))
        self.search_button.pack(pady=5)
        
        self.checkout_button = tk.Button(self.root, text="Check Out a Book", command=self.check_out_book, font=("Helvetica", 14))
        self.checkout_button.pack(pady=5)
        
        self.return_button = tk.Button(self.root, text="Return a Book", command=self.return_book, font=("Helvetica", 14))
        self.return_button.pack(pady=5)
        
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=("Helvetica", 14))
        self.exit_button.pack(pady=5)
    
    def add_book(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Add a Book")
        
        self.title_entry_label = tk.Label(self.new_window, text="Title:")
        self.title_entry_label.pack(pady=5)
        self.title_entry = tk.Entry(self.new_window)
        self.title_entry.pack(pady=5)
        
        self.author_entry_label = tk.Label(self.new_window, text="Author:")
        self.author_entry_label.pack(pady=5)
        self.author_entry = tk.Entry(self.new_window)
        self.author_entry.pack(pady=5)
        
        self.isbn_entry_label = tk.Label(self.new_window, text="ISBN:")
        self.isbn_entry_label.pack(pady=5)
        self.isbn_entry = tk.Entry(self.new_window)
        self.isbn_entry.pack(pady=5)
        
        self.add_button = tk.Button(self.new_window, text="Add Book", command=self.add_book_to_library)
        self.add_button.pack(pady=10)
    
    def add_book_to_library(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        self.library.add_book(title, author, isbn)
        messagebox.showinfo("Success", f"'{title}' has been added to the library.")
        self.new_window.destroy()
    
    def display_books(self):
        books = self.library.display_books()
        messagebox.showinfo("Library Catalog", books)
    
    def search_book(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Search for a Book")
        
        self.search_entry_label = tk.Label(self.new_window, text="Title:")
        self.search_entry_label.pack(pady=5)
        self.search_entry = tk.Entry(self.new_window)
        self.search_entry.pack(pady=5)
        
        self.search_button = tk.Button(self.new_window, text="Search", command=self.search_book_in_library)
        self.search_button.pack(pady=10)
    
    def search_book_in_library(self):
        title = self.search_entry.get()
        result = self.library.search_book(title)
        messagebox.showinfo("Search Result", result)
        self.new_window.destroy()
    
    def check_out_book(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Check Out a Book")
        
        self.checkout_entry_label = tk.Label(self.new_window, text="Title:")
        self.checkout_entry_label.pack(pady=5)
        self.checkout_entry = tk.Entry(self.new_window)
        self.checkout_entry.pack(pady=5)
        
        self.checkout_button = tk.Button(self.new_window, text="Check Out", command=self.check_out_book_from_library)
        self.checkout_button.pack(pady=10)
    
    def check_out_book_from_library(self):
        title = self.checkout_entry.get()
        result = self.library.check_out_book(title)
        messagebox.showinfo("Check Out Result", result)
        self.new_window.destroy()
    
    def return_book(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Return a Book")
        
        self.return_entry_label = tk.Label(self.new_window, text="Title:")
        self.return_entry_label.pack(pady=5)
        self.return_entry = tk.Entry(self.new_window)
        self.return_entry.pack(pady=5)
        
        self.return_button = tk.Button(self.new_window, text="Return", command=self.return_book_to_library)
        self.return_button.pack(pady=10)
    
    def return_book_to_library(self):
        title = self.return_entry.get()
        result = self.library.return_book(title)
        messagebox.showinfo("Return Result", result)
        self.new_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()
