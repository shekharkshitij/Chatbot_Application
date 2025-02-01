import streamlit as st

def navbar(key_prefix=None):
    """Reusable Horizontal Navigation Bar Component."""
    if key_prefix is None:
        key_prefix = st.session_state.get('page', 'default')

    st.markdown(
        """
        <style>
        /* Navbar Styling */
        .navbar {
            background-color: #007bff; /* Blue navbar background */
            padding: 10px 20px; /* Spacing inside the navbar */
            display: flex;
            justify-content: space-between; /* Space out title and links */
            align-items: center;
            position: sticky; /* Sticky to prevent content overlap */
            top: 0;
            z-index: 1000; /* Ensure it stays above other elements */
            width: 100%;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.3); /* Subtle shadow for elevation */
        }
        .navbar-links {
            display: flex; /* Align links horizontally */
            gap: 15px; /* Add space between links */
            background-color: #007bff;
        }
        .navbar-title {
            align-self: center;
            color: white; /* White text for title */
            font-size: 30px; /* Larger font size for title */
            font-weight: bold;
            text-align: center;
            margin-bottom: 5px;
            padding: 5px;
        }
        .button-container {
            display: flex; /* Align buttons horizontally */
            gap: 10px; /* Add space between buttons */
        }
        .button {
            background-color: #007bff; /* Blue background for buttons */
            color: white; /* White text for buttons */
            font-size: 16px;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            padding: 10px 20px; /* Padding inside the buttons */
            transition: background-color 0.3s ease;
            cursor: pointer;
            border: none; /* Remove default border */
        }
        .button:hover {
            background-color: #0056b3; /* Darker blue on hover */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="navbar-title"><center>Streamlit Chatbot<center></div>', unsafe_allow_html=True)
    st.markdown('<div class="navbar-links">', unsafe_allow_html=True)
    st.markdown('<div class="button-container">', unsafe_allow_html=True)

    # Navbar Links with unique keys
    if "user" in st.session_state:  # If the user is logged in
        col1, col2 = st.columns(2)  # Use columns for horizontal alignment
        with col1:
            if st.button("Chatbot", key=f"{key_prefix}_chatbot", help="Chatbot"):
                st.session_state.page = "Chatbot"
                st.rerun()
        with col2:
            if st.button("Logout", key=f"{key_prefix}_logout", help="Logout"):
                st.session_state.page = "Logout"
                st.rerun()
    else:  # If the user is not logged in
        col3, col4 = st.columns(2)  # Use columns for horizontal alignment
        with col3:
            if st.button("Login", key=f"{key_prefix}_login", help="Login"):
                st.session_state.page = "Login"
                st.rerun()
        with col4:
            if st.button("Register", key=f"{key_prefix}_register", help="Register"):
                st.session_state.page = "Register"
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)  # Close button container
    st.markdown('</div>', unsafe_allow_html=True)  # Close navbar-links
    st.markdown('</div>', unsafe_allow_html=True)  # Close navbar