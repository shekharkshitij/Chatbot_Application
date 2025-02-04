# **Streamlit Chatbot Application - README**

## **Overview**
This repository contains a **fully functional chatbot web application** built using **Streamlit**. The chatbot allows users to interact in real-time while maintaining session state and authentication. The application includes **user authentication**, **registration**, **password recovery**, and **session management** using **Streamlit's session state**.

The navbar ensures seamless navigation across different pages without reloading the entire application. **Dynamic page rendering** is implemented using session state and query parameters.

---

## **Features**
✅ **User Authentication**
- Users can log in with their email and password.
- Session state stores user authentication status.

✅ **User Registration**
- New users can register with their name, email, mobile number, and password.
- Passwords are stored securely in the database.

✅ **Forgot Password Functionality**
- Users can recover their password via email.

✅ **Chatbot Interface**
- Interactive chatbot where users can send messages and receive AI-generated responses.
- **WhatsApp-style UI** for chat experience.

✅ **Dynamic Navigation with Session State**
- Uses `st.session_state` for page routing.
- Navigation buttons update the session state instead of reloading.

✅ **Streamlined Navbar**
- The navbar **renders only once globally** in `main.py` to prevent duplicate navbars.
- Users see different navbar options based on authentication status.

✅ **Modern UI with Custom CSS**
- Blue navigation bar for consistency.
- Styled buttons and interactive chat window.

---

## **Installation Guide**

### **Prerequisites**
Ensure you have the following installed:
- Python (>=3.8)
- Streamlit
- SQLite3 (for database management)

### **Clone the Repository**
```bash
git clone https://github.com/your-username/streamlit-chatbot.git
cd streamlit-chatbot
```

### **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## **Application Structure**
```
streamlit_chatbot/
│── pages/
│   ├── login.py
│   ├── register.py
│   ├── forgot_password.py
│   ├── chatbot.py
│   ├── logout.py
│── utils/
│   ├── authentication.py
│   ├── database.py
│── navbar.py
│── styles.py
│── main.py
│── requirements.txt
│── README.md
```

### **File Breakdown**
📌 `main.py` - Handles navigation, session state, and page rendering.  
📌 `navbar.py` - Contains a global navbar, preventing duplicates.  
📌 `styles.py` - Stores global CSS styles for consistent UI.  
📌 `pages/` - Contains all app pages (Login, Register, Chatbot, Logout, etc.).  
📌 `utils/` - Utility files for database and authentication handling.  

---

## **How to Run the App**
Navigate to the project folder and run:
```bash
streamlit run main.py
```
The application will open in your **default web browser**.

---

## **Usage Instructions**

### **Login**
1. Enter **email** and **password**.
2. Click **"Login"** to authenticate.
3. If login is successful, you will be redirected to the **Chatbot**.

### **Register a New User**
1. Click **"Register"** on the navbar.
2. Fill in **Name, Email, Mobile, and Password**.
3. Click **"Register"** to create an account.
4. If registration is successful, you will be redirected to **Login**.

### **Forgot Password**
1. Click **"Forgot Password?"** on the login page.
2. Enter your **registered email**.
3. Click **"Send Password"** to receive your password via email.

### **Chatbot Usage**
1. Once logged in, click **"Chatbot"** in the navbar.
2. Enter messages in the input field and press Enter.
3. The AI will respond based on the conversation.

### **Logout**
1. Click **"Logout"** in the navbar to end the session.

---

## **Database Management**
This application uses **SQLite** for managing user data.

📌 **To check the database:**
```bash
sqlite3 database.db
SELECT * FROM users;
```

---

## **Troubleshooting**
### 🔹 Navbar Appears Twice?
- Ensure **navbar() is removed** from individual pages.
- Navbar is called **only once in `main.py`**.

### 🔹 Page Doesn't Change?
- Make sure the query parameter (`?page=login`) is updating in the URL.
- Use `st.rerun()` to reload after state changes.

### 🔹 Duplicate Streamlit Keys?
- Use unique `key` prefixes for each Streamlit widget.

---

## **Future Enhancements**
🔹 **Enhance Security** - Implement password hashing for better security.  
🔹 **Real-time AI Responses** - Improve chatbot AI with **OpenAI API**.  
🔹 **Database Improvements** - Add support for **MySQL/PostgreSQL**.  
🔹 **Custom User Profiles** - Enable users to update profile info.  

---

## **Contributing**
Contributions are welcome! To contribute:
1. **Fork** the repository.
2. **Create a branch**: `git checkout -b new-feature`
3. **Commit your changes**: `git commit -m "Add new feature"`
4. **Push to branch**: `git push origin new-feature`
5. **Create a Pull Request**

---

## **License**
This project is licensed under the **MIT License**. Feel free to modify and use it.

---

## **Contact**
For issues and discussions:
- **GitHub Issues**: [Open an Issue](https://github.com/shekharkshitij/Chatbot_Application/issues)
- **Email**: mail.kshitijshekhar@gmail.com

Happy Coding! 🚀
