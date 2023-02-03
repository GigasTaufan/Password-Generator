import streamlit as st
import string
import random

# Set page
# Page title to Password Generator and layout centered
st.set_page_config(
    page_title="Password Generator",
    layout="centered"
)

# Password generator function
def generate_password(length, include_lowercase, inlcude_uppercase, include_digits, include_punctuation):
    password = ''
    random_set = ''

    # If include lowercase
    if include_lowercase:
        random_set += string.ascii_lowercase
        password += random.choice(string.ascii_lowercase)
    
    # If inlcude uppercase
    if inlcude_uppercase:
        random_set += string.ascii_uppercase
        password += random.choice(string.ascii_uppercase)

    # If include digits
    if include_digits:
        random_set += string.digits
        password += random.choice(string.digits)

    # If include punctuation
    if include_punctuation:
        random_set += string.punctuation
        password += random.choice(string.punctuation)

    for i in range(length-3):
        password+=random.choice(random_set)

    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)

    return password
    

st.header("Password Generator")

length = st.slider('Password Length', min_value=8, max_value=32, value=8, step=1)
include_lowercase = st.checkbox('Include Lowercase Letters', value=True)
include_uppercase = st.checkbox('Include Uppercase Letters', value=True)
include_digits = st.checkbox('Include Digits', value=True)
include_punctuation = st.checkbox('Inclued Punctuation', value=False)

if st.button('Generate Password'):
    output_password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_punctuation)
    st.code(output_password)


# Hide style
# Hide burger menu and made with streamlit watermark
hide_st_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
