# IMPORT LIBRARIES
import streamlit as st
import string
import random

st.set_page_config(
    page_title="Password Generator",
    layout="centered",
)

def generate_password():

    # output password
    output_pass = ''
    password = ''

    random_set = string.ascii_letters + string.digits

    # lowercase
    password = random.choice(string.ascii_lowercase)

    # uppercase
    password += random.choice(string.ascii_uppercase)

    # digits
    password += random.choice(string.digits)

    # special characters
    # password += random.choice(string.punctuation)

    for i in range(4):
        password += random.choice(random_set)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)

    output_pass = password
    return output_pass


st.header("Password Generator")

if st.button('Generate Password'):
    output_password = generate_password()
    st.code(output_password)
    

