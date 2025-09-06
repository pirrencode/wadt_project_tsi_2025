# Virtual Library

This project is a Django-based virtual library for managing a catalog of books. It offers both a traditional Django web interface and a Streamlit UI for interaction.

## Features
- Manage books with title, author, publication date, ISBN, and optional description
- Web pages for listing, viewing, creating, updating, and deleting books
- Streamlit interface backed by the Django ORM for book management
- Unit tests covering book CRUD operations

## Getting Started
### Prerequisites
- Python 3.10+
- pip

### Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

### Running the development server
```bash
python manage.py runserver
```
Then open `http://localhost:8000/books/` in your browser.

### Streamlit UI
```bash
streamlit run streamlit_app.py
```

### Running tests
```bash
python manage.py test
```

## Project structure
- `library/` – Django project configuration
- `books/` – app containing the book model, views, URLs, and tests
- `templates/` – HTML templates for Django views
- `streamlit_app.py` – Streamlit interface
- `requirements.txt` – Python dependencies

## License
This project is licensed under the [MIT License](LICENSE).
