# for this project, we should first think about the aspects of a library and its functions.
# A library has available books for lending, they let students borrow and return books.
# so we should set up 2 classes: Library and Student


class Library:
    def __init__(self, booklist):
        self.availableBooks = booklist

    def displayBooks(self):
        print("\nThe books we have in stock are:")
        for book in self.availableBooks:
            print(book)

    def lendBooks(self, reqBook):
        if reqBook in self.availableBooks:
            print(f"\nYou have successfully borrowed '{reqBook}'")
            self.availableBooks.remove(reqBook)
        #     update the books which are available
        else:
            print("\nSorry, we do not have this book at the moment.")

    def returnBook(self, returnBook):
        self.availableBooks.append(returnBook)
        print(f"\nThank you for returning '{returnBook}'!")


class Student:
    def requestBook(self):
        reqBook = input("Enter the name of the book you would like to borrow: ")
        return reqBook

    def returnBook(self):
        returnBook = input("Enter the name of the book you are returning: ")
        return returnBook

list_of_books = [
    "The Covenant of Water by Abraham Verghese",
    "Lessons in Chemistry by Bonnie Garmus",
    "Fourth Wing by Rebecca Yarros",
    "The Night Circus by Erin Morgenstern",
    "Harry Potter and the Prisoner of Azkaban by J.K. Rowling",
    "Demon Copperhead by Barbara Kingsolver",
    "Tomorrow, and Tomorrow, and Tomorrow by Gabrielle Zevin",
    "The Seven Husbands of Evelyn Hugo by Taylor Jenkins Reid",
    "Diary of a Wimpy Kid: The Long Haul by Jeff Kinney",
    "The Alchemist by Paulo Coelho",
    "Spare by Prince Harry",
    "Becoming by Michelle Obama",
    "Sapiens: A Brief History of Humankind by Yuval Noah Harari",
    "Educated by Tara Westover",
    "Atomic Habits by James Clear",
    "Outliers by Malcolm Gladwell",
    "The Body Keeps the Score by Bessel van der Kolk",
    "Born a Crime by Trevor Noah",
    "The Power of Now by Eckhart Tolle",
    "The Subtle Art of Not Giving a F*ck by Mark Manson",
    "Dare to Lead by Brené Brown",
    "The Splendid and the Vile by Erik Larson",
    "Greenlights by Matthew McConaughey",
    "Quiet by Susan Cain",
    "The Light We Carry by Michelle Obama"
]

def main():
    library = Library(list_of_books)
    student = Student()

    while True:
        print("\n=== LIBRARY MENU ===")
        print("1. Display available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            library.displayBooks()

        elif choice == '2':
            requestedBook = student.requestBook()
            library.lendBooks(requestedBook)

        elif choice == '3':
            returnedBook = student.returnBook()
            library.returnBook(returnedBook)

        elif choice == '4':
            print("\nThank you for using the library system!")
            break

        else:
            print("\nInvalid choice. Please select a valid option.")

main()
