import streamlit as st

# Hardcoded username and password for My Personal File
correct_username = "nurye"
correct_password = "6879"

# Page navigation
PAGES = ["Home", "About", "My Personal File"]
page = st.radio("Go to", PAGES)

# Main content
col1, col2, col3 = st.columns(3)  # Create three columns for the pages

if page == "Home":
    col1.title("Home Page")
    
    col1.header("Professional Summary")
    col1.write("""
    I am a versatile professional proficient in machine learning libraries, computer vision, Python, C++, and
    frameworks like Flask. My expertise extends to databases (MongoDB, PostgreSQL, MySQL) and hardware
    integration like PLC, RASPBERRY PI, ARDUINO, with projects including a traffic light control system using
    computer vision. I aspire to excel as a machine learning engineer, integrating AI with hardware to address
    community challenges.
    """)

    col2.header("Skills")
    col2.subheader("Technical Skills")
    col2.write("""
    I specialize in hardware programming using PLC, Raspberry Pi, Arduino, and PIC, complemented by proficiency in
    machine learning libraries, computer vision, Python, and C++. Additionally, I am well-versed in frameworks like
    Flask and databases including MongoDB, PostgreSQL, and MySQL.
    """)
    col2.subheader("Soft Skills")
    col2.write("""
    Communication skill, Teamwork and collaboration, problem-solving skill, time management, creativity, and innovation
    """)
    col2.subheader("Software Tools")
    col2.write("""
    VSCODE, Anaconda, Scikit-learn, Keras, TensorFlow, PyTorch, Pandas, Matplotlib, Python, CV2
    """)

    col3.header("Work Experience")
    col3.write("""
    - **Automation Engineer** – self-employed - Ethiopia - 2021-Present
      - Engaging with clients seeking custom automated solutions or troubleshooting existing machinery.
    - **Sales and Service Engineer** - Abulkhase PLC – Ethiopia - 2022 – 2023 – part-time
      - Secured deals, engaged in tender processes, and provided comprehensive service support for products.
    """)

    col3.header("Education")
    col3.write("""
    - **Electro-Mechanical Engineering** – Addis Ababa Science and Technology University – Ethiopia - 2016-2021
      - Explored machine learning, computer vision, programming languages (Python, C++), and frameworks (Flask).
      - Proficient in hardware programming, including PLC and microcontrollers like PIC, Arduino, and 8051.
    """)

elif page == "About":
    col1.title("About Page")

    col1.write("Contact:")
    col1.write("- Email: nryngs2006@gmail.com")
    col1.write("- Phone: +251929404324")
    col1.write("- GitHub: [https://github.com/Nurye-Nigus](https://github.com/Nurye-Nigus)")
    col1.write("- LinkedIn: [https://www.linkedin.com/in/nryngs/](https://www.linkedin.com/in/nryngs/)")

elif page == "My Personal File":
    col1.title("My Personal File")

    # Login for My Personal File
    entered_username = col1.text_input("Username:")
    entered_password = col1.text_input("Password:", type="password")

    # Check login credentials
    if col1.button("Login"):
        if entered_username == correct_username and entered_password == correct_password:
            col1.success("Login successful!")

            # Display personal file content
            col2.header("Personal File Content")
            col2.write("This is your personal file content. You have successfully logged in.")
        else:
            col1.error("Invalid username or password. Please try again.")
