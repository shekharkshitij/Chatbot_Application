import streamlit as st
from styles import apply_global_styles  # Import global styles
from openai import OpenAI

# Initialize your OpenAI client
client = OpenAI(
    api_key="_"
)

def chatbot_page():
    """Chatbot Page for the App."""
    apply_global_styles()  # Apply global styles

    # Initialize session state for messages
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! How can I assist you today?"}
        ]

    # WhatsApp-like Chat Interface Styles
    st.markdown(
        """
        <style>
        .chat-container {
            max-width: 800px;
            margin: auto;
            padding: 10px;
            background-color: #1e1e2f;
            border-radius: 10px;
        }
        .message-left, .message-right {
            display: flex;
            margin-bottom: 10px;
        }
        .message-left {
            justify-content: flex-start;
        }
        .message-right {
            justify-content: flex-end;
        }
        .message-bubble-left, .message-bubble-right {
            max-width: 60%;
            padding: 10px 15px;
            border-radius: 15px;
        }
        .message-bubble-left {
            background-color: #e1f5fe;
            color: black;
            border-top-left-radius: 0;
        }
        .message-bubble-right {
            background-color: #c8e6c9;
            color: black;
            border-top-right-radius: 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Chat Title
    st.title("Chatbot - Welcome!")

    # Chat Display
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for idx, message in enumerate(st.session_state.messages):
        if message["role"] == "assistant":
            st.markdown(
                f"""
                <div class="message-left" id="message-assistant-{idx}">
                    <div class="message-bubble-left">{message['content']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div class="message-right" id="message-user-{idx}">
                    <div class="message-bubble-right">{message['content']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown('</div>', unsafe_allow_html=True)

    # Handle message sending
    def handle_message():
        user_input = st.session_state.get("user_input", "").strip()
        if user_input:
            # Add user's message to session state
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state["user_input"] = ""  # Clear the input field

            # Get the chatbot's response
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    store=True,
                    messages=st.session_state.messages,
                )
                assistant_message = response.choices[0].message.content  # Access the content
                st.session_state.messages.append({"role": "assistant", "content": assistant_message})
            except Exception as e:
                # Handle errors gracefully
                print(f"Error: {e}")  # Log error to console
                st.error("An error occurred while fetching the assistant's response.")
                st.session_state.messages.append(
                    {"role": "assistant", "content": "Sorry, I couldn't process your request. Please try again later."}
                )

    # Input Box for Sending Messages (Triggers on Enter)
    st.text_input(
        "Type your message here:",
        key="user_input",
        placeholder="Enter your message...",
        on_change=handle_message,
    )

# Run the chatbot page
if __name__ == "__main__":
    st.set_page_config(page_title="Chatbot App", layout="wide")
    chatbot_page()
