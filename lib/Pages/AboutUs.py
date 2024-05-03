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
lottie_us=load_lottieurl("https://lottie.host/190d7694-ea40-4770-aac5-3a6e2cf965d6/Tq8MQ1jo4W.json")
lottie_we=load_lottieurl("https://lottie.host/b14400c6-5657-4b49-aef1-61e50bb3c154/9YwzyqnspQ.json")
lottie_hi=load_lottieurl("https://lottie.host/a2cc754d-05f5-440a-ac01-c29b7b848897/Lv6FaKojHB.json")
# ------Header Section--------
with st.container():
  left_column,right_column=st.columns(2)
  with left_column:
     st.subheader("Hey There,:wave:")
     st.write("We are happy to see you here.")      
with st.container():
     st.write("---")
     left_column,right_column=st.columns(2)
     with left_column:
          st.header("About Us")
          st.write("##")
          st.write(
               """Welcome to our Library Management System! 
               We are dedicated to revolutionizing the way libraries 
               operate and serve their communities. Our mission is to 
               provide cutting-edge technology solutions that 
               streamline library operations, enhance user experiences, 
               and promote a love for reading and learning."""
          )
          st.write("---")
          st.header("Who We Are")
          st.write("##")
          st.write(
               """We are a team of passionate individuals with diverse
                 backgrounds in software development, library science, 
                 and information technology. United by our shared vision 
                 of empowering libraries, we collaborate closely with
                 librarians and educators to understand their unique challenges 
                 and develop tailored solutions."""
          )
          st.write("---")
          st.header("Our Values")
          st.write("##")
          st.write(
               """
                - Innovation: We constantly seek new ways to improve and innovate, 
                   leveraging the latest technologies to drive efficiency and effectiveness.
                - Accessibility: We are committed to creating inclusive solutions 
                   that are accessible to all members of the community, regardless
                     of background or ability.
                - Collaboration: We believe in the power of collaboration and work 
                    closely with libraries and stakeholders to co-create solutions that 
                    meet their unique needs.
                - Integrity: We operate with honesty, transparency, and integrity in 
                    everything we do, fostering trust and reliability among our clients 
                    and partners.
                - Lifelong Learning: We are advocates for lifelong learning and believe 
                    in the transformative power of education and knowledge."""
          )
     with right_column:
          st.lottie(lottie_us,height=300,key="us")
          st.lottie(lottie_we,height=300,key="we")
          st.lottie(lottie_hi,height=300,key="hi")