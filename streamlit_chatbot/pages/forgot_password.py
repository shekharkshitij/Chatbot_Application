import streamlit as st
from styles import apply_global_styles  # Import global styles
import sqlite3
import smtplib
from email.mime.text import MIMEText
from utils.database import create_connection  # Database connection utility


def send_email(to_email, password):
    """Send an email with the user's password."""
    try:
        sender_email = "mail.kshitijshekhar@gmail.com"  # Replace with your email
        sender_password = "ifun tjqt jbcx nxbp"  # Replace with your app password

        # Configure SMTP server
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)

        # Compose the email
        message = MIMEText(f"Your password is: {password}")
        message["Subject"] = "Password Recovery"
        message["From"] = sender_email
        message["To"] = to_email

        # Send the email
        smtp_server.sendmail(sender_email, to_email, message.as_string())
        smtp_server.quit()
        return True
    except Exception as e:
        st.error(f"Failed to send email: {e}")
        return False


def forgot_password_page():
    """Forgot Password Page for Password Recovery."""
    apply_global_styles()  # Apply global styles

    st.markdown('<div class="main-container" style="max-width: 600px; margin: auto;">', unsafe_allow_html=True)
    st.title("Forgot Password")

    # Retrieve query parameters
    query_params = st.query_params
    email_query = query_params.get("email", [""])[0]  # Get the email from query params if provided

    # User inputs their registered email
    email = st.text_input(
        "Enter your registered email",
        placeholder="Enter your email",
        value=email_query,  # Pre-fill the email field if available in query params
        key="forgot_email",
    )

    if st.button("Send Password", key="forgot_password_button"):
        if not email:
            st.warning("Please enter your registered email address.")
        else:
            # Check if the email exists in the database
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
            user = cursor.fetchone()
            conn.close()

            if user:
                password = user[0]
                # Send email with the user's password
                if send_email(email, password):
                    st.success("Password sent successfully! Redirecting to Login Page...")
                    st.session_state.page = "Login"  # Redirect to Login Page
                    st.rerun()  # Trigger a rerun to load the Login Page
                else:
                    st.error("Failed to send the email. Please try again later.")
            else:
                st.error("Email not found. Please check and try again.")

    # # Back to Login link
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
