import pandas as pd
import streamlit as st
import plotly.express as px
from auth import user_login, user_signup
from database import insert_user_profile

st.write("# Data Visualization App")


email = st.text_input("Email")
password = st.text_input("Password", type="password")


if st.button("Sign Up"):
    response = user_signup(email, password)
    
    if response and response.user:
        
        
        insert_user_profile(response.user.id, full_name="")
        st.success("Sign up successful!")
        
    else:
        st.error("Sign up failed: " + response.error if response else "Unknown error")

        
