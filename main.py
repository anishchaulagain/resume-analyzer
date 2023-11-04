import streamlit as st
import mysql.connector
import bcrypt

# Create a MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="anees@123",
    database="streamlit"
)
cursor = conn.cursor()

# Streamlit app title
st.title("Resume Analyzer for Job Seekers")

st.text("")
st.text("")

authentication_option = st.selectbox("Choose an option:", ["Sign In", "Sign Up"])
# Function to register a new user
show_signup = False
show_login = False

if authentication_option == "Sign Up":
    show_signup = True
elif authentication_option == "Sign In":
    show_login = True

st.text("")
st.text("")
def register_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    conn.commit()

# Function to log in a user
def login_user(username, password):
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    user_data = cursor.fetchone()

    if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data[0].encode('utf-8')):
        return True
    return False

# User registration form
if show_signup:
 st.subheader("Sign Up")
 new_username = st.text_input("Username", key="username_input1")
 new_password = st.text_input("Password", type="password", key="password1")
 if st.button("Register"):
    if new_username and new_password:
        register_user(new_username, new_password)
        st.success("User registered successfully!")

# User login form
if show_login:
 st.subheader("Sign In")
 username = st.text_input("Username", key="username_input2")
 password = st.text_input("Password", type="password", key="password2")
 if st.button("Login"):
    if login_user(username, password):
        st.success("Logged in successfully!")
    else:
        st.error("Authentication failed. Please check your credentials.")

# Close the database connection when done
conn.close()