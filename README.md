# 📚 **Streamlit Chatbot Application - README**

---

## 🚀 **Overview**

Welcome to the **Streamlit Chatbot Application**! This project is a fully functional web application built using **Streamlit**, designed to provide a seamless user experience with features like **user registration**, **login authentication**, **password recovery**, and an **AI-powered chatbot**. 

The app uses **SQLite** as the backend database for managing user credentials securely, and incorporates **dynamic routing**, **session management**, and a **responsive navbar** for smooth navigation.

---

## 🗂️ **Project Structure**

```
STREAMLIT_CHATBOT/
├── pages/
│   ├── __init__.py
│   ├── chatbot.py
│   ├── forgot_password.py
│   ├── login.py
│   ├── logout.py
│   └── register.py
├── utils/
│   ├── __init__.py
│   ├── authentication.py
│   └── database.py
├── __pycache__/
├── initialize_db.py
├── main.py
├── navbar.py
├── requirements.txt
├── styles.py
└── users.db
```

### 🔑 **File/Folder Descriptions**

- **`main.py`**: The core file handling routing, navigation, and initializing the application.
- **`navbar.py`**: Centralized navigation bar that dynamically updates based on user login status.
- **`pages/`**: Contains individual pages:
  - `login.py` - User login interface.
  - `register.py` - New user registration form.
  - `forgot_password.py` - Password recovery page via email.
  - `logout.py` - Handles user logout.
  - `chatbot.py` - The chatbot interface powered by OpenAI.
- **`utils/`**: Contains helper modules:
  - `authentication.py` - User authentication logic.
  - `database.py` - Functions for database interaction.
- **`initialize_db.py`**: Script to set up the SQLite database schema.
- **`styles.py`**: Custom CSS styles for consistent UI/UX design.
- **`users.db`**: SQLite database file to store user credentials securely.

---

## 🧩 **Features**

- ✅ **User Authentication** (Login & Secure Sessions)
- ✅ **User Registration** (With Validation)
- ✅ **Password Recovery** (Email-based Recovery)
- ✅ **AI-Powered Chatbot** (OpenAI Integration)
- ✅ **Responsive Navigation Bar** (Dynamic Based on User Session)
- ✅ **Database Management** (SQLite for Storing User Data)
- ✅ **Session State Handling** (For Seamless Navigation)
- ✅ **Modern UI/UX Design** (Custom CSS Styling)

---

## ⚙️ **Installation & Setup**

### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/shekharkshitij/Chatbot_Application.git
cd streamlit_chatbot
```

### 2️⃣ **(Optional) Create a Virtual Environment**

```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

### 3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4️⃣ **Initialize the Database**

```bash
python initialize_db.py
```
This will create the `users.db` SQLite file with the required tables.

### 5️⃣ **Run the Application**

```bash
streamlit run main.py
```

You'll get a **localhost URL**. Open it in your browser to interact with the app.

---

## 🗝️ **Usage Instructions**

### 👤 **Login Page**
1. Enter your **email** and **password**.
2. Click **Login** to authenticate.
3. Upon successful login, you will be redirected to the **Chatbot Page**.

### 📝 **Registration Page**
1. Click **Register** on the navbar.
2. Fill in your **Name**, **Email**, **Mobile Number**, and **Password**.
3. Click **Register** to create an account.

### 🔑 **Forgot Password**
1. Click on **Forgot Password** on the login page.
2. Enter your registered email address.
3. Check your inbox for the recovery email.

### 🤖 **Chatbot Page**
1. After logging in, navigate to the **Chatbot Page**.
2. Type your message in the input box.
3. Press **Enter** or click **Send** to chat with the AI.

### 🚪 **Logout**
- Click on **Logout** in the navbar to end your session securely.

---

## 📊 **Database Schema**

The SQLite database (`users.db`) contains the following table:

### **Table: `users`**
| Field        | Type     | Description              |
| ------------ | -------- | ------------------------ |
| `id`         | INTEGER  | Primary Key (Auto Increment) |
| `name`       | TEXT     | User's Full Name         |
| `email`      | TEXT     | User's Email (Unique)    |
| `mobile`     | TEXT     | User's Mobile Number     |
| `password`   | TEXT     | Hashed Password          |

---

## 🛠️ **Tech Stack**

- **Frontend:** Streamlit (Python-based UI)
- **Backend:** Python
- **Database:** SQLite
- **APIs:** OpenAI API for Chatbot
- **Email Service:** SMTP (for Password Recovery)

---

## 🚩 **Key Components Explained**

### 1️⃣ **Session State Management**
The app relies on `st.session_state` to manage:
- User authentication sessions
- Dynamic page routing
- Storing temporary data like chatbot messages

### 2️⃣ **Dynamic Routing**
Navigation between pages like Login, Register, Chatbot, etc., is handled using:
```python
st.session_state.page = "Page_Name"
st.rerun()
```

### 3️⃣ **Centralized Navbar**
The navbar is dynamic and updates based on whether a user is logged in:
- Shows **Login/Register** when logged out
- Shows **Chatbot/Logout** when logged in

### 4️⃣ **Authentication System**
- **Registration:** Users register with a unique email.
- **Login:** Secure login using credentials.
- **Password Recovery:** Sends password recovery emails using SMTP.

### 5️⃣ **Database Operations**
All database-related functions are centralized in `utils/database.py`, ensuring separation of concerns.

---

## 🔒 **Security Considerations**

- Passwords are stored securely (ensure proper hashing for production).
- SMTP credentials should be handled securely (preferably using environment variables).
- Avoid hardcoding API keys; use `.env` files in production.

---

## ✅ **Future Enhancements**

- Add **Password Hashing** for enhanced security.
- Integrate **OAuth (Google/GitHub Login)**.
- Enhance the chatbot with advanced features like **contextual memory**.
- Add **user profile management**.
- Implement **dark mode** and advanced UI features.

---

## 🤝 **Contributing**

We welcome contributions! 

### **Steps to Contribute:**
1. Fork the repository 🍴
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit: `git commit -m "Added new feature"`
4. Push to your fork: `git push origin feature-branch`
5. Open a Pull Request 🚀

---

## 💼 **License**

This project is licensed under the **MIT License**. Feel free to use and modify as needed.

---

## 📧 **Contact**

For questions, suggestions, or support:
- **Email:** mail.kshitijshekhar@gmail.com
- **GitHub:** [your-username](https://github.com/shekharkshitij)

---

### ⭐ **If you found this project helpful, give it a star!** ⭐

---

**Made with ❤️ using Streamlit.**
