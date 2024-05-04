import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage",page_icon=":books:",layout="wide")
def load_lottieurl(url):
     r=requests.get(url)
     if r.status_code !=200:
          return None
     return r.json()
def local_css(file_name):
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css(r"C:/Users/Dell/Desktop/lib/Pages/style.css")
lottie_books=load_lottieurl("https://lottie.host/987962aa-0dc3-449b-a3fa-a7c965cf2c64/k5ofOOzV9r.json")
lottie_reading=load_lottieurl("https://lottie.host/54b59e24-7e1c-4eb2-b726-59330c964890/z6I8pk2PM6.json")
# ------Header Section--------
with st.container():
     st.subheader("Hi,I am your guide :wave:")
     st.write("We are happy to take your Feedback.")
     st.write("Your words are valuable")
     st.write("[learn more>](C:/Users/Dell/Desktop/lib/Pages/AboutUs.py)")
with st.container():
     st.write("---")
     left_column,right_column=st.columns(2)
     with left_column:
          st.header("What we do")
          st.write("##")
          st.write(
               """The ultimate goal of the Open Library is to make all the published works of humankind available to everyone in the world. 
               While large in scope and ambition, this goal is within our grasp. 
               Achieving it will require the participation of librarians, authors, government officials and technologists.
               Imagine what a comprehensive, open library could be! A talented math whiz who lives in a rural community can explore the works of high math.
               An elderly person can have a large print edition of any book ever published. An innovative young scholar can publish a book directly to this
                 great library on subjects that might not otherwise make it through the long and difficult publication process.
               How can you help? Improve the records we have for the books you love every record is fully editable by clicking the “edit” button on the page.
               If we don't have a record for a book, you can create one. If you're a library with digitized resources, tell us where they are and we'll point people to them.
               Our hope is that libraries and individual book readers will join this project and together we can build towards universal access to all knowledge."""
          )
     with right_column:
          st.lottie(lottie_reading,height=300,key="reading")
with st.container():
     st.write("---")
     left_column,right_column=st.columns(2)
     with left_column:
        st.header("Join Us in Spreading Knowledge!")
        st.write("##")  
        st.subheader(" Donate Today!")
        st.write(
               """
               Welcome to our initiative dedicated to spreading the joy of reading and knowledge sharing. 
               We believe that books have the power to transform lives and communities. 
               However, not everyone has access to the resources they need to pursue their love for reading. 
               That's where you come in! By donating books, you can make a significant impact on someone's life and 
               contribute to a brighter future for all. Join us in this noble cause and help us make a difference, one book at a time.
               """
          )
     with right_column:
          st.lottie(lottie_books,height=300,key="books")
# -----Contact------
with st.container():
     st.write("---")
     st.header("Get in touch with me!")
     st.write("##")
     contact_form="""
       <form action="https://formsubmit.co/somyalakshmi17@gmail.com" method="POST">
       <input type="hidden" names="_captcha" value="false">
       <input type="text" name="name" placeholder="Your name" required>
       <input type="email" name="email" placeholder="your email" required>
       <textarea name="message" placeholder="Your message here" required></textarea>
       <button type="submit">Send</button>
       </form>
      """
     left_column,right_column=st.columns(2)
     with left_column:
          st.markdown(contact_form,unsafe_allow_html=True)
     with right_column:
          st.empty()

