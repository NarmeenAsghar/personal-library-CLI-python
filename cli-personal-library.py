# empty list
library = []

# Adding function
def add_book(title, author, year, category, read_status):
    book = {
        "title": title,
        "author": author,
        "year": year,
        "category": category,
        "read_status": read_status
    }
    library.append(book)

# Removing function
def remove_book(title):
    global library
    library = [book for book in library if book["title"].lower() != title.lower()]

# Searching function
def search_books(search_by, search_value):
    result = []
    for book in library:
        if search_by == "Title" and search_value.lower() in book["title"].lower():
            result.append(book)
        elif search_by == "Author" and search_value.lower() in book["author"].lower():
            result.append(book)
    return result

# Displaying function
# enumerate() is a built-in function that adds a counter to an iterable (like a list, tuple, or string) and returns it as an enumerate object. 
# enumerate() allows you to loop through both the index (position) and the value of each element in the iterable.
def display_books():
    if library:
# This line takes each book from the library and stores it in the `book` variable along with an index (which starts from 1). Then, we use `idx` (the index) and `book` (the book data) inside the loop.
        for idx, book in enumerate(library, start=1):
            status = "Read" if book["read_status"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['category']} - {status}")
    else:
        print("📚 Your library is empty. 📚")

def library_overview():
    total_books = len(library)
    read_books = len([book for book in library if book["read_status"]])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    print(f"📘 Total books: {total_books}")
    print(f"📖 Percentage read: {percentage_read:.2f}%")

def main():
    while True:
        print("\n📚 PERSONAL LIBRARY MANAGER 📚\n")
        print("=" * 100)
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Overview")
        print("6. Exit")
        
        choice = input("Choose an option (1-6) 📋: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            year = int(input("Enter the publication year: "))
            category = input("Enter the category: ")
            read_status = input("Have you read this book? (yes/no): ").strip().lower()
            read_status = True if read_status == "yes" else False
            add_book(title, author, year, category, read_status)
            print(f"-------------------------'{title}' added successfully! 🎉-------------------------")

        elif choice == "2":
            title_to_remove = input("Enter the title of the book to remove: ")
            remove_book(title_to_remove)
            print(f"-------------------------'{title_to_remove}' removed successfully! ✂️-------------------------")

        elif choice == "3":
            search_by = input("Search by (Title/Author): ").strip()
            search_value = input(f"Enter the {search_by.lower()} to search for: ").strip()
            results = search_books(search_by, search_value)
            if results:
                for idx, book in enumerate(results, start=1):
                    status = "Read" if book["read_status"] else "Unread"
                    print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['category']} - {status}")
            else:
                print(f"-------------------------No books found matching '{search_value}' 😞-------------------------")

        elif choice == "4":
            display_books()

        elif choice == "5":
            library_overview()

        elif choice == "6":
            print("=" * 100)
            print("\nThank you for using the Personal Library Manager. Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
