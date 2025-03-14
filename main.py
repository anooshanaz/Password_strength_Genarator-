# import streamlit as st
# import random
# import string

# def generate_password(length, use_digit, use_special):
#     characters = string.ascii_letters  # Uppercase and lowercase letters

#     if use_digit:
#         characters += string.digits  # Numbers 0 to 9

#     if use_special:
#         characters += string.punctuation  # Special characters @#$%^&*

#     return "".join(random.choice(characters) for _ in range(length))

# # UI design in Streamlit
# st.title("Password Generator")

# length = st.slider("Password length", min_value=6, max_value=32, value=12)
# use_digit = st.checkbox("Include digits")
# use_special = st.checkbox("Include special characters")

# if st.button("Generate Password"):
#     password1 = generate_password(length, use_digit, use_special)
#     st.write(f"Generated password: `{password1}`")

import streamlit as st
import random
import string

# Set Page Config
st.set_page_config(page_title="Password Generator", page_icon="🔑", layout="centered")

# Custom CSS to Set Background Image
background_url = "data:image/jpeg;base64,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"  # Change URL for a different image
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("{background_url}") no-repeat center center fixed;
        background-size: cover;
    }}
    .password-box {{
        background-color: rgba(0, 0, 0, 0.7);
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-size: 1.5rem;
        color: #00ffcc;
        font-weight: bold;
        margin-top: 20px;
    }}
    h1, label {{
        color: white;
        text-align: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# UI Title
st.title("🔐 Password Generator")

# Function to Generate Password
def generate_password(length, use_digit, use_special):
    characters = string.ascii_letters  # Uppercase and lowercase letters
    if use_digit:
        characters += string.digits  # Numbers 0 to 9
    if use_special:
        characters += string.punctuation  # Special characters
    return "".join(random.choice(characters) for _ in range(length))

# UI Components
length = st.slider("🔢 Password Length", min_value=6, max_value=32, value=12)
use_digit = st.checkbox("🔢 Include Digits")
use_special = st.checkbox("🔣 Include Special Characters")

# Generate Button
if st.button("🎲 Generate Password"):
    password1 = generate_password(length, use_digit, use_special)
    st.markdown(f'<div class="password-box">🔑 {password1}</div>', unsafe_allow_html=True)
