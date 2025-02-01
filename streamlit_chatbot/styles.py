import streamlit as st

def apply_global_styles():
    st.markdown(
        """
        <style>
        /* General Input Field Styling */
        input[type="text"], input[type="email"], input[type="password"] {
            border: 1px solid #ccc; /* Neutral border color */
            border-radius: 5px; /* Smooth rounded corners */
            padding: 15px; /* Increased padding for a larger input area */
            height: 50px; /* Larger height for better visibility */
            width: 100%; /* Full width to fit container */
            background-color: #1e1e2f; /* Consistent dark background */
            color: white; /* White text for better contrast */
            font-size: 16px; /* Larger font size for readability */
            outline: none; /* Remove default browser outline */
            transition: border-color 0.3s ease, background-color 0.3s ease; /* Smooth transitions */
        }

        /* Focus State Styling */
        input[type="text"]:focus, input[type="email"]:focus, input[type="password"]:focus {
            border: 1px solid #888; /* Light gray border on focus */
            background-color: #2b2b40; /* Slightly lighter background on focus */
            box-shadow: none; /* Remove shadow */
        }

        /* Validation State Styling */
        input[type="text"]:invalid, input[type="email"]:invalid, input[type="password"]:invalid {
            border: 1px solid #ccc; /* Neutral border color for invalid state */
            background-color: #1e1e2f; /* Maintain consistent background color */
            box-shadow: none; /* Remove shadow for invalid state */
        }

        /* Input Field Margins for Consistency */
        input[type="text"], input[type="email"], input[type="password"] {
            margin-bottom: 15px; /* Add spacing below inputs */
        }

        /* Styling for Labels */
        label {
            font-weight: bold;
            color: white; /* Consistent label color for dark background */
            margin-bottom: 5px;
            display: block; /* Ensure labels are above input fields */
        }

        /* Button Styling */
        button {
            background-color: #007bff; /* Primary blue color */
            color: white; /* White text for contrast */
            padding: 10px 15px;
            border: none; /* Remove default border */
            border-radius: 5px; /* Rounded corners for a modern look */
            cursor: pointer; /* Pointer cursor on hover */
            font-size: 16px; /* Readable font size */
            display: block;
            margin-top: 10px; /* Add margin above buttons */
            transition: background-color 0.3s ease; /* Smooth hover transition */
        }

        button:hover {
            background-color: #0056b3; /* Darker blue on hover */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
