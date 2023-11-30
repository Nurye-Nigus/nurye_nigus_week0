import streamlit as st

def login():
    st.title("Login to Nurye's Personal File")

    # Hardcoded username and password for Nurye's personal file
    correct_username = "nurye"
    correct_password = "6879"

    # User input for username and password
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    # Login button
    if st.button("Login"):
        if username == correct_username and password == correct_password:
            st.success("Login successful!")
            return True
        else:
            st.error("Invalid username or password. Please try again.")
    return False

def nurye_personal_file():
    st.title("Nurye's Personal File")

    # Your biography content
    st.header("Biography")
    st.write("""
    I am Nurye, a versatile professional proficient in machine learning libraries, computer vision, Python, C++, and
    frameworks like Flask. My expertise extends to databases (MongoDB, PostgreSQL, MySQL) and hardware
    integration like PLC, RASPBERRY PI, ARDUINO, with projects including a traffic light control system using
    computer vision. I aspire to excel as a machine learning engineer, integrating AI with hardware to address
    community challenges.

    **Skills:**
    - Technical Skills
      - Hardware programming using PLC, Raspberry Pi, Arduino, and PIC
      - Proficiency in machine learning libraries, computer vision, Python, and C++
      - Frameworks: Flask
      - Databases: MongoDB, PostgreSQL, MySQL

    - Soft Skills
      - Communication skill, Teamwork and collaboration, problem-solving skill
      - Time management, creativity, and innovation

    - Software Tools
      - VSCODE, Anaconda, Scikit-learn, Keras, TensorFlow, PyTorch, Pandas, Matplotlib, Python, CV2

    **Work Experience:**
    - Automation Engineer – self-employed - Ethiopia - 2021-Present
      - Engaging with clients seeking custom automated solutions or troubleshooting existing machinery.
    - Sales and Service Engineer - Abulkhase PLC – Ethiopia - 2022 – 2023 – part-time
      - Secured deals, engaged in tender processes, and provided comprehensive service support for products.

    **Education:**
    - Electro-Mechanical Engineering – Addis Ababa Science and Technology University – Ethiopia - 2016-2021
      - Explored machine learning, computer vision, programming languages (Python, C++), and frameworks (Flask).
      - Proficient in hardware programming, including PLC and microcontrollers like PIC, Arduino, and 8051.
    """)

def main():
    if login():
        nurye_personal_file()

if __name__ == "__main__":
    main()
