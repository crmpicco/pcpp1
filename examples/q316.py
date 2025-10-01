import requests

def add_book(title, author, isbn):
    url = "www.example123.com"
    data = {
        "title": title,
        "author": author,
        "isbn": isbn
    }
    response = requests.post(url, json=data)

    if response.status_code == 201:
        print("Book added successfully.")
    elif response.status_code == 200:
        print("Book updated successfully.")
    else:
        print(f"Failed to add/update book. Status code: {response.status_code}")

# Example usage:
add_book("Python Programming", "John Doe", "978-1234567890")
