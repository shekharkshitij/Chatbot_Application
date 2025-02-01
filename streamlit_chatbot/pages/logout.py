import streamlit as st
from styles import apply_global_styles  # Import global styles

def logout_page():
    """Logout Page for the Chatbot App."""
    apply_global_styles()  # Apply global styles

    # Title for the Logout Page
    st.markdown('<div style="max-width: 600px; margin: auto; text-align: center;">', unsafe_allow_html=True)
    st.title("Logout")

    # Check if the user is logged in
    if "user" in st.session_state:
        # Clear the session state
        del st.session_state["user"]
        st.success("You have been successfully logged out!")
        # Redirect to the login page with a button
        if st.button("Go to Login", key="logout_to_login"):
            st.session_state.page = "Login"
            st.rerun()
    else:
        st.warning("You are not logged in.")
        # Redirect to the login page with a button
        if st.button("Go to Login", key="not_logged_in_to_login"):
            st.session_state.page = "Login"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
