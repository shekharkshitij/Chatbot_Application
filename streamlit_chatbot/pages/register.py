import streamlit as st
from styles import apply_global_styles  # Import global styles
from utils.authentication import register_user  # Import register logic

def register_page():
    """Register Page for the Chatbot App."""
    apply_global_styles()  # Apply global styles

    # Main container for the registration form
    st.markdown('<div class="main-container" style="max-width: 600px; margin: auto;">', unsafe_allow_html=True)
    st.title("Register")

    # Registration Form Fields
    name = st.text_input(
        "Full Name",
        placeholder="Enter your full name",
        key="register_name",
        help="Enter your complete name",
    )
    email = st.text_input(
        "Email",
        placeholder="Enter your email",
        key="register_email",
        help="Enter a valid email address",
    )
    mobile = st.text_input(
        "Mobile Number",
        placeholder="Enter your mobile number",
        key="register_mobile",
        help="Enter your active mobile number",
    )
    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter a strong password",
        key="register_password",
        help="Create a secure password",
    )

    # Submit Button for Registration
    if st.button("Register", key="register_button", help="Click to register"):
        # Validation for input fields
        if not name or not email or not mobile or not password:
            st.warning("All fields are required. Please fill in all the details.")
        else:
            # Attempt to register the user
            if register_user(name, email, mobile, password):
                st.success("Registration successful! Redirecting to Login Page...")
                st.session_state.page = "Login"  # Redirect to Login Page
                st.rerun()  # Reload the app
            else:
                st.error("Email already registered. Please use a different email.")

    # # Link to Navigate Back to Login Page
    # st.markdown(
    #     '''
    #     <div style="text-align: center; margin-top: 20px;">
    #         <a href="?page=login" style="
    #             display: inline-block;
    #             padding: 10px 20px;
    #             background-color: #007bff;
    #             color: white;
    #             font-size: 16px;
    #             text-decoration: none;
    #             border-radius: 5px;
    #             font-weight: bold;
    #             transition: background-color 0.3s ease;
    #         " onmouseover="this.style.backgroundColor='#0056b3'" onmouseout="this.style.backgroundColor='#007bff'">
    #             Back to Login
    #         </a>
    #     </div>
    #     ''',
    #     unsafe_allow_html=True,
    # )

    st.markdown('</div>', unsafe_allow_html=True)
