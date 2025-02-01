import streamlit as st
from styles import apply_global_styles  # Import global styles
from utils.authentication import authenticate_user  # Import authentication logic

def login_page(key_prefix="login"):
    """Login Page for the Chatbot App."""
    apply_global_styles()  # Apply global styles for consistent design

    # Main container for the login page
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.title("Login")

    # Email Input Field
    email = st.text_input(
        "Email",
        placeholder="Enter your email",
        key=f"{key_prefix}_email",  # Unique key for this input
        help="Enter your registered email",
    )

    # Password Input Field
    password = st.text_input(
        "Password",
        placeholder="Enter your password",
        type="password",
        key=f"{key_prefix}_password",  # Unique key for this input
        help="Enter your password",
    )

    # Buttons Section
    st.markdown('<div style="margin-top: 20px;">', unsafe_allow_html=True)

    # Login Button
    if st.button("Login", key=f"{key_prefix}_login_button", help="Click to login"):
        user = authenticate_user(email, password)  # Authenticate the user
        if user:
            st.success(f"Welcome back, {user[1]}!")  # Show success message
            st.session_state.user = user  # Save user info in session state
            st.session_state.page = "Chatbot"  # Navigate to Chatbot page
            st.rerun()  # Reload the app for navigation
        else:
            st.error("Invalid email or password. Please try again.")  # Show error message

    # Forgot Password Button
    if st.button("Forgot Password?", key=f"{key_prefix}_forgot_password_button", help="Recover your password"):
        st.session_state.page = "Forgot Password"  # Navigate to Forgot Password page
        st.rerun()  # Reload the app for navigation

    # New User Registration Button (below other buttons)
    st.markdown('<div style="margin-top: 10px; text-align: center;">', unsafe_allow_html=True)
    if st.button("New User?", key=f"{key_prefix}_new_user_button", help="Create a new account"):
        st.session_state.page = "Register"  # Navigate to Register page
        st.rerun()  # Reload the app for navigation
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
