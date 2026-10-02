import os
from datetime import datetime
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from mistralai.client import Mistral


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Mistral AI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# API KEY CONFIGURATION
# ============================================================
#
# LOCAL:
#     Reads MISTRAL_API_KEY from .env
#
# STREAMLIT CLOUD:
#     Reads MISTRAL_API_KEY from Streamlit Secrets
#
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

# Load local .env file if it exists
load_dotenv(dotenv_path=ENV_FILE)

# First try environment variable
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# If environment variable is not available,
# try Streamlit Cloud Secrets
if not MISTRAL_API_KEY:

    try:
        MISTRAL_API_KEY = st.secrets["MISTRAL_API_KEY"]

    except Exception:
        MISTRAL_API_KEY = None


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ==============================
       MAIN APPLICATION
       ============================== */

    .stApp {
        background-color: #f5f9ff;
    }


    /* ==============================
       SIDEBAR
       ============================== */

    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #dbeafe;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #075985;
    }


    /* ==============================
       MAIN TITLE
       ============================== */

    h1 {
        color: #075985 !important;
        font-weight: 800 !important;
    }

    h2,
    h3 {
        color: #0f766e !important;
    }


    /* ==============================
       CHAT MESSAGES
       ============================== */

    [data-testid="stChatMessage"] {
        border-radius: 16px;
        padding: 14px;
        margin-bottom: 12px;
        border: 1px solid #dbeafe;
        background-color: #ffffff;
    }


    /* ==============================
       CHAT INPUT
       ============================== */

    [data-testid="stChatInput"] {
        border: 2px solid #bfdbfe;
        border-radius: 15px;
        background-color: #ffffff;
    }


    /* ==============================
       BUTTONS
       ============================== */

    .stButton > button {
        border-radius: 10px;
        border: 1px solid #2563eb;
        background-color: #2563eb;
        color: white;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #1d4ed8;
        border-color: #1d4ed8;
        color: white;
    }


    /* ==============================
       SELECT BOX
       ============================== */

    div[data-baseweb="select"] > div {
        border-radius: 10px;
        border: 1px solid #93c5fd;
        background-color: white;
    }


    /* ==============================
       FOOTER
       ============================== */

    .footer-text {
        text-align: center;
        color: #64748b;
        font-size: 12px;
        margin-top: 25px;
        padding: 15px;
    }


    /* ==============================
       DIVIDER
       ============================== */

    hr {
        border-color: #dbeafe;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "model" not in st.session_state:
    st.session_state.model = "mistral-small-latest"


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🤖 Mistral AI")

    st.caption(
        "A modern AI chatbot powered by "
        "Mistral AI, Python and Streamlit."
    )

    st.divider()

    st.subheader("⚙️ Settings")

    selected_model = st.selectbox(
        "Choose Mistral Model",
        [
            "mistral-small-latest",
            "mistral-medium-latest",
            "mistral-large-latest"
        ],
        index=0
    )

    st.session_state.model = selected_model

    st.write("")

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()

    st.divider()

    st.subheader("💡 About")

    st.info(
        "This chatbot uses the Mistral API to generate "
        "intelligent responses and maintain conversation "
        "history."
    )

    st.subheader("🔐 Security")

    st.success(
        "API keys are loaded from .env locally or "
        "Streamlit Secrets in the cloud."
    )

    st.subheader("🚀 Features")

    st.write(
        """
        • Multi-turn conversations

        • Mistral model selection

        • Conversation history

        • Secure API key handling

        • API error handling

        • Responsive interface
        """
    )


# ============================================================
# MAIN HEADER
# ============================================================

st.title("🤖 Mistral AI Chatbot")

st.markdown(
    """
    ### Intelligent conversations powered by Mistral AI

    Ask questions, learn programming, generate ideas,
    write code, summarize information, or simply chat.
    """
)

st.divider()


# ============================================================
# CHECK API KEY
# ============================================================

if not MISTRAL_API_KEY:

    st.error(
        "❌ MISTRAL_API_KEY was not found."
    )

    st.info(
        "For local development, create a .env file "
        "in the same folder as app.py."
    )

    st.code(
        "MISTRAL_API_KEY=your_actual_api_key",
        language="text"
    )

    st.info(
        "For Streamlit Cloud, add MISTRAL_API_KEY "
        "under App Settings → Secrets."
    )

    st.stop()


# ============================================================
# CREATE MISTRAL CLIENT
# ============================================================

try:

    client = Mistral(
        api_key=MISTRAL_API_KEY
    )

except Exception as error:

    st.error(
        "❌ Failed to initialize the Mistral API client."
    )

    with st.expander("Technical Details"):

        st.code(
            str(error),
            language="text"
        )

    st.stop()


# ============================================================
# WELCOME SCREEN
# ============================================================

if len(st.session_state.messages) == 0:

    st.subheader("💬 Start a Conversation")

    st.write(
        "Ask Mistral AI anything. Here are some examples:"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            "💻 Explain Java OOP concepts"
        )

    with col2:

        st.info(
            "🐍 Give me a Python project idea"
        )

    with col3:

        st.success(
            "🤖 Explain Generative AI"
        )

    st.write("")


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    role = message["role"]

    content = message["content"]

    message_time = message.get("time", "")

    if role == "user":

        with st.chat_message(
            "user",
            avatar="👤"
        ):

            st.markdown(content)

            if message_time:

                st.caption(
                    f"🕐 {message_time}"
                )

    elif role == "assistant":

        with st.chat_message(
            "assistant",
            avatar="🤖"
        ):

            st.markdown(content)

            if message_time:

                st.caption(
                    f"🕐 {message_time}"
                )


# ============================================================
# CHAT INPUT
# ============================================================

user_input = st.chat_input(
    "Ask Mistral AI anything..."
)


# ============================================================
# PROCESS USER MESSAGE
# ============================================================

if user_input:

    user_input = user_input.strip()

    if not user_input:

        st.warning(
            "Please enter a message."
        )

        st.stop()


    # ========================================================
    # SAVE USER MESSAGE
    # ========================================================

    current_time = datetime.now().strftime(
        "%d %b %Y, %I:%M %p"
    )

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
            "time": current_time
        }
    )


    # ========================================================
    # PREPARE MISTRAL MESSAGES
    # ========================================================

    api_messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful, professional and friendly "
                "AI assistant. Give clear, accurate and useful "
                "answers. For programming questions, provide "
                "correct and beginner-friendly explanations "
                "and code."
            )
        }
    ]


    for message in st.session_state.messages:

        api_messages.append(
            {
                "role": message["role"],
                "content": message["content"]
            }
        )


    # ========================================================
    # CALL MISTRAL API
    # ========================================================

    with st.spinner(
        "🤖 Mistral AI is thinking..."
    ):

        try:

            response = client.chat.complete(
                model=st.session_state.model,
                messages=api_messages,
                temperature=0.7,
                max_tokens=2000
            )


            # =================================================
            # EXTRACT RESPONSE
            # =================================================

            assistant_response = (
                response
                .choices[0]
                .message
                .content
            )


            if not assistant_response:

                raise Exception(
                    "Mistral returned an empty response."
                )


            # =================================================
            # SAVE ASSISTANT RESPONSE
            # =================================================

            assistant_time = datetime.now().strftime(
                "%d %b %Y, %I:%M %p"
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": assistant_response,
                    "time": assistant_time
                }
            )


            # Refresh interface

            st.rerun()


        # ====================================================
        # ERROR HANDLING
        # ====================================================

        except Exception as error:

            error_text = str(error).lower()


            # -----------------------------------------------
            # Remove failed user message
            # -----------------------------------------------

            if st.session_state.messages:

                last_message = (
                    st.session_state.messages[-1]
                )

                if (
                    last_message["role"] == "user"
                    and last_message["content"] == user_input
                ):

                    st.session_state.messages.pop()


            # -----------------------------------------------
            # INVALID API KEY
            # -----------------------------------------------

            if (
                "401" in error_text
                or "unauthorized" in error_text
                or "authentication" in error_text
                or "invalid api key" in error_text
                or "invalid_api_key" in error_text
            ):

                st.error(
                    "🔐 Invalid Mistral API key."
                )

                st.info(
                    "Check your .env file locally or "
                    "Streamlit Cloud Secrets."
                )


            # -----------------------------------------------
            # RATE LIMIT
            # -----------------------------------------------

            elif (
                "429" in error_text
                or "rate limit" in error_text
                or "too many requests" in error_text
            ):

                st.warning(
                    "⏳ Mistral API rate limit reached. "
                    "Please wait and try again later."
                )


            # -----------------------------------------------
            # TIMEOUT
            # -----------------------------------------------

            elif (
                "timeout" in error_text
                or "timed out" in error_text
            ):

                st.error(
                    "🌐 Request timed out. "
                    "Please check your internet connection."
                )


            # -----------------------------------------------
            # NETWORK ERROR
            # -----------------------------------------------

            elif (
                "connection" in error_text
                or "network" in error_text
            ):

                st.error(
                    "🌐 Network error. "
                    "Please check your internet connection."
                )


            # -----------------------------------------------
            # MODEL NOT FOUND
            # -----------------------------------------------

            elif (
                "404" in error_text
                or "not found" in error_text
            ):

                st.error(
                    "❌ The selected Mistral model "
                    "was not found."
                )


            # -----------------------------------------------
            # OTHER API ERROR
            # -----------------------------------------------

            else:

                st.error(
                    "❌ Mistral API request failed."
                )

                with st.expander(
                    "🔍 Technical Details"
                ):

                    st.code(
                        str(error),
                        language="text"
                    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer-text">
        Powered by Mistral AI • Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)