class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")
        self.file.seek(0)

    def __del__(self):
        self.file.close()

    def list_books(self):
        with open("books.txt", "r") as file:
            book_lines = file.read().splitlines()

        if not book_lines:
            print("There are no books in the library.")
        else:
            print("List of Books:")
            for line in book_lines:
                book_info = line.split(",")
                title = book_info[0]
                author = book_info[1]
                print(f"{title}, {author}")

    def add_book(self):
        while True:
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()

            while True:
                release_year = input("Enter release year: ").strip()
                if release_year.isdigit():
                    release_year = int(release_year)
                    break
                else:
                    print("Please enter a valid release year.")

            while True:
                num_pages = input("Enter number of pages: ").strip()
                if num_pages.isdigit():
                    num_pages = int(num_pages)
                    break
                else:
                    print("Please enter a valid number of pages.")

            if not title or not author:
                print("Please enter all book information.")
            else:
                book_info = (f"{title}, {author}, "
                             f"{release_year}, {num_pages}\n")
                
                with open(self.file_path, "a") as file:
                    file.write(book_info)
                print("Book added successfully.")
                break

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        with open("books.txt", "r") as file:
            book_lines = file.read().splitlines()

        book_removed = False
        for line in book_lines:
            book_info = line.split(",")
            title = book_info[0].strip()
            if title.lower() == title_to_remove.lower():
                book_lines.remove(line)
                print(f"Book '{title_to_remove}' has been removed from the library.")
                book_removed = True
                break

        if not book_removed:
            print(f"Book '{title_to_remove}' is not found in the library.")

        with open("books.txt", "w") as file:
            for line in book_lines:
                file.write(line + "\n")

lib = Library()

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice.")
