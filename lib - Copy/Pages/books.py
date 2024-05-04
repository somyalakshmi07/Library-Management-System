import requests
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
import uuid
import csv
import datetime
from datetime import datetime

st.set_page_config(page_title="My Webpage",page_icon=":books:", layout="wide")
def load_lottieurl(url):
     r=requests.get(url)
     if r.status_code !=200:
          return None
     return r.json()
def local_css(file_name):
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css(r"C:/Users/Dell/Desktop/lib/style.css")
lottie_add=load_lottieurl("https://lottie.host/44d4c64c-f651-4920-a6eb-c415f9f11914/bXqFYflWo4.json")

class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

def add_book(title, author, category):
    book = Book(title, author, category)
    with open('C:/Users/Dell/Desktop/lib/Pages/books.csv', 'a') as f:
        f.write(f"{book.title},{book.author},{book.category}\n")
    

def get_all_books():
    try:
        books = pd.read_csv('C:/Users/Dell/Desktop/lib/Pages/books.csv', names=["Title", "Author", "Category"])
        return books.to_dict('records')
    except FileNotFoundError:
        return []

def search_books(query):
    books = pd.read_csv('C:/Users/Dell/Desktop/lib/Pages/books.csv', names=["title", "author", "category"])
    return books[books["title"].str.contains(query, case=False)].values.tolist()


def delete_book(title, books):
    """
    Delete a book from the list of books if its title matches the given title.

    Parameters:
    title (str): The title of the book to be deleted.
    books (list): List of dictionaries representing books.

    Returns:
    list: Updated list of books.
    """
    # updated_books = [book for book in books if 'title' in book and book['title'] != title]
    with open('C:/Users/Dell/Desktop/lib/Pages/books.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    i=0
    for dictionary in data:
        if dictionary["title"] != title :
            i += 1
        else :
          data.pop(i)
    df = pd.DataFrame(data)
    df.to_csv('C:/Users/Dell/Desktop/lib/Pages/books.csv', index=False, header=True)
    return books

    # if len(books) != len(updated_books):
    #     return updated_books
    # else:
    #     return books
def borrower_registration():
    """
    Register a new borrower.

    Returns:
        dict: Dictionary containing borrower information.
    """
    form = st.form("borrower_registration_{}".format(uuid.uuid4()))
    # Get borrower information
    borrower = {
        'name': form.text_input("Enter borrower's name:", placeholder="Name"),
        'age': form.number_input("Enter borrower's age:", placeholder="Age"),
        'address': form.text_input("Enter borrower's address:", placeholder="Address"),
        'email': form.text_input("Enter borrower's email:", placeholder="Email"),
        'membership_type': form.text_input("Enter borrower's membership type:", placeholder="Membership Type"),
        'member_since': form.date_input("Enter borrower's membership start date:")
    }

    if form.form_submit_button("Register"):
        if all(borrower[key] for key in borrower):
            st.markdown("Borrower registered successfully.")
            # Create a DataFrame from the dictionary of borrower information
            df = pd.DataFrame([borrower])
            # Save the DataFrame to a CSV file
            df.to_csv("C:/Users/Dell/Desktop/lib/Pages/browser.csv", index=False)
            return borrower
        else:
            st.error("Please fill in all fields.")
    else:
        st.warning("Borrower registration cancelled.")
        return {}
def is_member(name):
    """
    Check if the borrower is a member and has a pro membership type.
    """
    members = pd.read_csv('C:/Users/Dell/Desktop/lib/Pages/browser.csv')
    member = members[members['name'] == name]
    return not member.empty and member['membership_type'].iloc[0] == 'pro' 
def borrow_books():
    """
    Borrow books.
    """
    # Get borrower information
    borrower = {
        'name': st.text_input("Enter borrower's name:")
    }

    # Check if the borrower is a member with a pro membership type
    if not is_member(borrower['name']):
        st.markdown("Sorry, you need to be a pro member to borrow books.")
        return
    form1=st.form("Borrow books")
    # Get borrowed books information
    borrowed_books = []
    while True:
        book_title = form1.text_input("Enter borrowed book title:")
        if book_title:
            borrowed_books.append({'Book Title': book_title})
        else:
            break

    if form1.form_submit_button("Borrow"):
        if borrowed_books:
            st.markdown("Books borrowed successfully.")
            # Create a DataFrame from borrowed books data
            df = pd.DataFrame(borrowed_books)
            # Save the DataFrame to a CSV file
            df.to_csv('C:/Users/Dell/Desktop/lib/Pages/borrowed_books.csv', index=False, mode='a', header=not df.empty)
        else:
            st.warning("No books selected for borrowing.")
def view_borrowers_with_book():
    """
    View borrowers with borrowed books.
    """
    try:
        borrowers = pd.read_csv('C:/Users/Dell/Desktop/lib/Pages/browser.csv')
        borrowers_books = pd.read_csv('C:/Users/Dell/Desktop/lib/Pages/borrowed_books.csv')

        # Concatenate borrowers and borrowed books dataframes
        merged_df = pd.concat([borrowers, borrowers_books], axis=1)

        if merged_df.empty:
            st.write("No borrowers or borrowed books found.")
        else:
            st.subheader("Borrowers with Borrowed Books")
            st.write(merged_df)
    except FileNotFoundError:
        st.error("Data files not found.")

def is_member(name):
    # Placeholder function to check if the borrower is a member with a pro membership type
    # You can implement your logic here, for example, by checking a database of members
    # For demonstration purposes, let's assume all users are pro members
    return True

def is_book_available(title, author):
    # Placeholder function to check if the book is available
    # You can implement your logic here, for example, by checking a database of books
    # For demonstration purposes, let's assume all books are available
    return True

def issue_book():
    """
    Issue a book to a borrower.
    """
    form2 = st.form("Issue_form")
    
    # Get borrower information
    borrower = {
        'name': form2.text_input("Enter borrower's name:"),
        'issue date': form2.date_input('issue date'),
    }
    if borrower["issue date"] == datetime.date.today():
        issue_date = datetime.date.today()
    else:
        form2.warning("Please use currrent date")
    
    return_date = issue_date + datetime.timedelta(days=10)
    date = {
        'return date': form2.markdown(f"The book **must** be returned by {return_date} :exclamation::exclamation:")
    }
    # Get book information
    book = {
        'title': form2.text_input("Enter book title:"),
        'author': form2.text_input("Enter author:")
    }

    # Check if the borrower is a member with a pro membership type
    if not is_member(borrower['name']):
        st.markdown("Sorry, you need to be a pro member to borrow books.")
        return

    # Check if the book is available
    if not is_book_available(book['title'], book['author']):
        st.markdown("Sorry, the book is not available.")
        return

    if form2.form_submit_button("Issue Book"):
        if borrower['name'] and book['title']:
            st.markdown("Book issued successfully.")
            # Save the issued book information to a CSV file
            df = pd.DataFrame({'Borrower Name': [borrower['name']], 'Book Title': [book['title']], 'Issue Date': [borrower['issue date']], 'Return ate': [date['return date']]})
            df.to_csv('C:/Users/Dell/Desktop/lib/Pages/borrowed_books.csv', index=False, mode='a', header=not df.empty)
        else:
            st.warning("Please enter a borrower and a book title.")
    
    

menu = ["Add Book", "View Books", "Search Books",'Delete Book','Borrow','Borrower Registration','View Borrowers','Issue Book']
choice = st.sidebar.selectbox("Select an option", menu)

if choice == "Add Book":
    st.subheader("Add a Book")
    title = st.text_input("Enter the book title")
    author = st.text_input("Enter the author")
    categories = ["Fiction", "Non-Fiction", "Science", "History","Novel","Fantasy","Technical","Mystery","Auto biograpy"]
    category = st.selectbox("Select a category", categories)
    if st.button("Add"):
        add_book(title, author, category)
        st.success("Book added.")
    st.markdown(f'<style>{choice} {{cursor: pointer;}}</style>', unsafe_allow_html=True)

elif choice == "View Books":
    st.subheader("Book List")
    books = get_all_books()
    if not books:
        st.write("No books found.")
    else:
        headers = ["Title", "Author", "Category"]
        book_df = pd.DataFrame(books, columns=headers)
        st.write(book_df)

elif choice == "Search Books":
    st.subheader("Search Books")
    query = st.text_input("Enter a search query")
    if st.button("Search"):
        books = search_books(query)
        if not books:
            st.write("No books found.")
        else:
            headers = ["Title", "Author", "Category"]
            book_df = pd.DataFrame(books, columns=headers)
            st.write(book_df)

elif choice == 'Delete Book':
    st.header("Delete Book")
    title = st.text_input("Enter the title of the book to delete:")
    delete_button = st.button("Delete")
    st.subheader("Book List")
    books = get_all_books()
    if not books:
        st.write("No books found.")
    else:
        headers = ["Title", "Author", "Category"]
        book_df = pd.DataFrame(books, columns=headers)
        st.write(book_df)

    if delete_button:  # Check if delete_button is clicked
        books = delete_book(title, books="books.csv")
        if len(books) != len(get_all_books()):  # Check if title exists in the books
            st.session_state['books'] = books
            st.success(f"{title} has been deleted from the library.")
        else:
            st.warning(f"{title} not found in the library.")
    else:
        st.warning("Please click the 'Delete' button to delete a book.")

elif choice == "Borrower Registration":
    borrower_registration()

elif choice == "Borrow":
    borrow_books()
elif choice == "View Borrowers":
    view_borrowers_with_book()
elif choice == "Issue Book":
    form2 = st.form("Issue_form")
    borrower = {
        'name': form2.text_input("Enter borrower's name:")
    }
    book = {
        'title': form2.text_input("Enter book title:"),
        'author': form2.text_input("Enter author:")
    }
    issue_date = form2.date_input("Enter issue date:")
    issue_date.strftime("%Y-%m-%d")
    return_date = form2.date_input("Enter return date:")
    return_date.strftime("%Y-%m-%d")

    if form2.form_submit_button("Issue Book"):
        if borrower['name'] and book['title']:
            st.markdown("Book issued successfully.")
            # Convert issue_date and return_date to datetime objects
            issue_date_datetime = datetime.strptime(str(issue_date), "%Y-%m-%d")
            return_date_datetime = datetime.strptime(str(return_date), "%Y-%m-%d")

            # Save the issued book information to a CSV file
            df = pd.DataFrame({'Borrower Name': [borrower['name']], 'Book Title': [book['title']], 'Issue Date': [issue_date_datetime], 'Return Date': [return_date_datetime]})
            df.to_csv('C:/Users/Dell/Desktop/lib/Pages/borrowed_books.csv', index=False, mode='a', header=not df.empty)
        else:
            st.warning("Please enter a borrower and a book title.")
st.lottie(lottie_add,height=300,key="add")