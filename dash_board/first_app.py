import streamlit as st

# Hardcoded username and password for My Personal File
correct_username = "nurye"
correct_password = "6879"

# Page navigation
PAGES = ["Home", "About", "My Personal File"]
page = st.selectbox("Go to", PAGES)

# Main content
if page == "Home":
    st.title("Home Page")
    
    st.header("Professional Summary")
    st.write("""
    I am a versatile professional proficient in machine learning libraries, computer vision, Python, C++, and
    frameworks like Flask. My expertise extends to databases (MongoDB, PostgreSQL, MySQL) and hardware
    integration like PLC, RASPBERRY PI, ARDUINO, with projects including a traffic light control system using
    computer vision. I aspire to excel as a machine learning engineer, integrating AI with hardware to address
    community challenges.
    """)

    st.header("Skills")
    st.subheader("Technical Skills")
    st.write("""
    I specialize in hardware programming using PLC, Raspberry Pi, Arduino, and PIC, complemented by proficiency in
    machine learning libraries, computer vision, Python, and C++. Additionally, I am well-versed in frameworks like
    Flask and databases including MongoDB, PostgreSQL, and MySQL.
    """)
    st.subheader("Soft Skills")
    st.write("""
    Communication skill, Teamwork and collaboration, problem-solving skill, time management, creativity, and innovation
    """)
    st.subheader("Software Tools")
    st.write("""
    VSCODE, Anaconda, Scikit-learn, Keras, TensorFlow, PyTorch, Pandas, Matplotlib, Python, CV2
    """)

    st.header("Work Experience")
    st.write("""
    - **Automation Engineer** – self-employed - Ethiopia - 2021-Present
      - Engaging with clients seeking custom automated solutions or troubleshooting existing machinery.
    - **Sales and Service Engineer** - Abulkhase PLC – Ethiopia - 2022 – 2023 – part-time
      - Secured deals, engaged in tender processes, and provided comprehensive service support for products.
    """)

    st.header("Education")
    st.write("""
    - **Electro-Mechanical Engineering** – Addis Ababa Science and Technology University – Ethiopia - 2016-2021
      - Explored machine learning, computer vision, programming languages (Python, C++), and frameworks (Flask).
      - Proficient in hardware programming, including PLC and microcontrollers like PIC, Arduino, and 8051.
    """)

elif page == "About":
    st.title("About Page")

    st.write("Contact:")
    st.write("- Email: nryngs2006@gmail.com")
    st.write("- Phone: +251929404324")
    st.write("- GitHub: [https://github.com/Nurye-Nigus](https://github.com/Nurye-Nigus)")
    st.write("- LinkedIn: [https://www.linkedin.com/in/nryngs/](https://www.linkedin.com/in/nryngs/)")

elif page == "My Personal File":
    st.title("My Personal File")

    # Login for My Personal File
    entered_username = st.text_input("Username:")
    entered_password = st.text_input("Password:", type="password")

    # Check login credentials
    if st.button("Login"):
        if entered_username == correct_username and entered_password == correct_password:
            st.success("Login successful!")

            # Display personal file content
            st.header("Personal File Content")
            st.write("This is my personal file content. You have successfully logged in.")
        else:
            st.error("Invalid username or password. Please try again.")
