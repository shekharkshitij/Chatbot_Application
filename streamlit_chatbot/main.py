import streamlit as st

# Ensure this is the first Streamlit command
st.set_page_config(page_title="Chatbot App", layout="wide")

from navbar import navbar  # Import the navbar component
from styles import apply_global_styles  # Import global styles

# Apply global styles for the entire app
apply_global_styles()

navbar()

# Initialize session state for page routing
if "page" not in st.session_state:
    st.session_state.page = "Login"  # Default page is Login

# Define page navigation logic
def navigate_to(page_name):
    """Handles page navigation by updating session state and rerunning the app."""
    st.session_state.page = page_name
    st.rerun()  # Reload the app to reflect the navigation

# Get the current page from the navbar links (query parameters)
query_params = st.query_params
if "page" in query_params:
    st.session_state.page = query_params["page"][0]

# Page routing logic with conditional checks
if st.session_state.page == "Login":
    from pages.login import login_page
    login_page()
elif st.session_state.page == "Register":
    from pages.register import register_page
    register_page()
elif st.session_state.page == "Forgot Password":
    from pages.forgot_password import forgot_password_page
    forgot_password_page()
elif st.session_state.page == "Chatbot":
    # Ensure user is logged in to access Chatbot
    if "user" in st.session_state:
        from pages.chatbot import chatbot_page
        chatbot_page()
    else:
        st.warning("You need to log in to access the Chatbot page.")
        navigate_to("Login")
elif st.session_state.page == "Logout":
    from pages.logout import logout_page
    logout_page()  # No need to pass key_prefix here
else:
    st.error("Page not found.")
    navigate_to("Login")

# Trigger a rerun if necessary
if st.session_state.get("rerun", False):
    st.session_state.rerun = False
    st.rerun()  # Reload the app if necessary
