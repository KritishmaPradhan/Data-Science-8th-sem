import streamlit as st
import requests 
st.write("Hello, Kritishma!")
st.markdown("<h1>Hello</h1>", unsafe_allow_html = True)
st.set_page_config(
    page_title = "Our First Streamlit App"
)
st.markdown("""
            <style>
            button{
                color: black;
                background: pink;
                border: 1px solid pink;
                border-radius: 12px;
                padding: 10px;
                box-shadow: 0 0 10px white;
            }
            </style>
            <button>Submit</button>
            """, unsafe_allow_html = True)
name = st.text_input("Enter your name")
st.number_input("Enter age", min_value = 0, max_value = 100, value =25)

st.markdown("---")

if st.button("Submit"):
    st.success("Successfully clicked Button")
if st.button("Reject"):
    st.error("Error Reject")

r = requests.get('http://127.0.0.1:8000/item')
# if r.status_code == 200:
#     items = r.json()
#     st.write(items)
for items in r.json():
    st.write(items["name"])
