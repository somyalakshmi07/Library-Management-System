import streamlit as st
import pandas as pd
import requests
from streamlit_lottie import st_lottie
# Set page configuration
st.set_page_config(page_title="My Library", page_icon=":books:", layout="wide")

# Add CSS to set background image
st.markdown("""
<style>
.stApp {{
background-image: url("https://example.com/banner.png");
background-size: cover;
}}
</style>
""", unsafe_allow_html=True)

# Add title
st.markdown("<h1 style='text-align:center;color:#4F8BF9;'>My Library</h1>", unsafe_allow_html=True)

# Load books data from CSV file
books = pd.read_csv("C:/Users/Dell/Desktop/lib/Pages/books.csv")

# Add search bar and search button
search_query = st.text_input("",placeholder="Search...", key="search_query")
col1, col2, col3, col4, col5, col6, col7= st.columns(7)
trigger = True
with col4:
    if st.button("Search", key="search_button"):
        trigger = True
    else:
        trigger = False
column1, column2, column3 = st.columns(3)
with column2:    
    if trigger:
        # Filter dataframe based on search query
        filtered_books = books[books["title"].str.contains(search_query, case=False)]
        # Display filtered dataframe
        st.dataframe(filtered_books)
def load_lottieurl(url):
     r=requests.get(url)
     if r.status_code !=200:
          return None
     return r.json()
def local_css(file_name):
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css(r"C:/Users/Dell/Desktop/lib/style.css")
lottie_book=load_lottieurl("https://lottie.host/281bdf4a-c02c-4073-b1ca-b98ece6baeda/dBx7kPCXdB.json")
lottie_learning=load_lottieurl("https://lottie.host/63ebd78c-cc80-4e95-b0b6-f82c28fcbe09/mbLO1T8zmx.json")
with st.container():
     left_column,right_column=st.columns(2)
     with left_column:
          st.header("Unlock Your Imagination, Open a Book!")
          st.write("##")
          st.write(
               """Dear Book Lover,
In a world where possibilities are limitless and adventures know no bounds, there exists a magical portal awaiting your discovery - the pages of a book.
Within these boundless realms of ink and paper, you'll find the power to transcend time and space, to journey to faraway lands, to walk in the shoes of heroes and heroines, and to dream the dreams of countless souls who've poured their hearts onto these pages.
With each turn of a page, you're not just reading words, you're embarking on a voyage of discovery. You're delving into the depths of human imagination, exploring the uncharted territories of the mind, and awakening dormant passions and curiosities.
In the embrace of a book, you'll find solace in moments of solitude, companionship in times of loneliness, and wisdom in the face of uncertainty. Every book is a treasure trove waiting to be unearthed, a key to unlock the mysteries of the universe, and a beacon of hope guiding you through life's darkest hours.
So, dear reader, I implore you: Open a book and let its magic unfold. Lose yourself in its pages, immerse yourself in its stories, and discover the endless wonders that await you. For in the world of books, there are no limits, only infinite possibilities waiting to be explored.
Happy reading, dear book lover. Your next adventure awaits between the covers of a book."""
          )
     with right_column:
          st.lottie(lottie_learning,height=300,key="learning")
          st.lottie(lottie_book,height=300,key="book")