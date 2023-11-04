import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(initial_sidebar_state="collapsed")

st.title("This is homepage")

if st.button("Logout"):
 st.text("Logging out...")
 switch_page("main")
