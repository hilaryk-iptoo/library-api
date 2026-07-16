from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="CIT Backend Course API",
    version="0.1.0"
)

# ==========================
# Models
# ==========================

class Category(BaseModel):
    name: str
    description: Optional[str] = None


class Book(BaseModel):
    title: str
    author: str
    category: str
    year: int


# ==========================
# Fake Database
# ==========================

categories = []
books = []

# ==========================
# Welcome Endpoint
# ==========================

@app.get("/welcome", tags=["default"], summary="Welcome")
def welcome():
    return {
        "message": "Welcome to the CIT Backend Course API"
    }

# ==========================
# Categories
# ==========================

@app.post("/categories", tags=["default"], summary="Create Category")
def create_category(category: Category):
    categories.append(category)
    return {
        "message": "Category created successfully",
        "category": category
    }


@app.get("/categories", tags=["default"], summary="Get All Categories")
def get_categories():
    return categories

# ==========================
# Books
# ==========================

@app.post("/books", tags=["default"], summary="Create Book")
def create_book(book: Book):
    books.append(book)
    return {
        "message": "Book created successfully",
        "book": book
    }


@app.get("/books", tags=["default"], summary="Get All Books")
def get_books():
    return books


@app.get("/books/{book_id}", tags=["default"], summary="Get Book By ID")
def get_book(book_id: int):

    if book_id < 0 or book_id >= len(books):
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return books[book_id]


@app.get("/books/search", tags=["default"], summary="Search Books")
def search_books(keyword: str):

    results = []

    for book in books:
        if keyword.lower() in book.title.lower():
            results.append(book)

    return results


@app.patch("/books/{book_id}", tags=["default"], summary="Update Book")
def update_book(book_id: int, book: Book):

    if book_id < 0 or book_id >= len(books):
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    books[book_id] = book

    return {
        "message": "Book updated successfully",
        "book": book
    }