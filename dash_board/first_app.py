import streamlit as st

def login():
    st.title("Login Page")

    # Hardcoded username and password for demonstration purposes
    correct_username = "nurye"
    correct_password = "6879"

    # User input for username and password
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    # Login button
    if st.button("Login"):
        if username == correct_username and password == correct_password:
            st.success("Login successful!")
            # You can redirect to another page or perform further actions after successful login
        else:
            st.error("Invalid username or password. Please try again.")

if __name__ == "__main__":
    login()
