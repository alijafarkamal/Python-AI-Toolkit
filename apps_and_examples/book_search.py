import requests

def get_book_details():
    query = input("Enter a book title: ")
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"

    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch data. Please try again.")
        return
    
    books = response.json().get('items', [])
    if not books:
        print("No books found.")
        return

    print("\nSearch results:")
    for i, book in enumerate(books[:15], start=1):  # Limit to 5 results for simplicity
        title = book['volumeInfo'].get('title', 'N/A')
        authors = ', '.join(book['volumeInfo'].get('authors', ['N/A']))
        print(f"{i}. {title} by {authors}")

    choice = int(input("\nEnter the number of the book you want details for: ")) - 1
    if choice < 0 or choice >= len(books):
        print("Invalid choice.")
        return

    selected_book = books[choice]
    info = selected_book.get('volumeInfo', {})
    print("\nBook Details:")
    print(f"Title: {info.get('title', 'N/A')}")
    print(f"Authors: {', '.join(info.get('authors', ['N/A']))}")
    print(f"Published Date: {info.get('publishedDate', 'N/A')}")
    print(f"Publisher: {info.get('publisher', 'N/A')}")
    print(f"Page Count: {info.get('pageCount', 'N/A')}")
    print(f"Categories: {', '.join(info.get('categories', ['N/A']))}")
    print(f"Description: {info.get('description', 'N/A')[:500]}...")  # Truncated description
    print(f"Language: {info.get('language', 'N/A')}")
    print(f"Preview Link: {info.get('previewLink', 'N/A')}")

get_book_details()
