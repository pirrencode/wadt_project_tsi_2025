import os
import django
import streamlit as st

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()

from books.models import Book

st.title('Virtual Library')

books = Book.objects.all()
if books:
    for book in books:
        with st.expander(f"{book.title} by {book.author}"):
            st.write(f"Published: {book.publication_date}")
            st.write(f"ISBN: {book.isbn}")
            if book.description:
                st.write(book.description)
            if st.button('Edit', key=f'edit_{book.id}'):
                st.session_state['edit_id'] = book.id
                st.experimental_rerun()
            if st.button('Delete', key=f'delete_{book.id}'):
                book.delete()
                st.experimental_rerun()
else:
    st.info('No books available.')

if 'edit_id' in st.session_state:
    book = Book.objects.get(id=st.session_state['edit_id'])
    with st.form('edit_form'):
        title = st.text_input('Title', book.title)
        author = st.text_input('Author', book.author)
        publication_date = st.date_input('Publication Date', book.publication_date)
        isbn = st.text_input('ISBN', book.isbn)
        description = st.text_area('Description', book.description or '')
        if st.form_submit_button('Update Book'):
            book.title = title
            book.author = author
            book.publication_date = publication_date
            book.isbn = isbn
            book.description = description
            book.save()
            del st.session_state['edit_id']
            st.experimental_rerun()
else:
    with st.form('add_form'):
        title = st.text_input('Title')
        author = st.text_input('Author')
        publication_date = st.date_input('Publication Date')
        isbn = st.text_input('ISBN')
        description = st.text_area('Description')
        if st.form_submit_button('Add Book'):
            Book.objects.create(
                title=title,
                author=author,
                publication_date=publication_date,
                isbn=isbn,
                description=description,
            )
            st.experimental_rerun()
