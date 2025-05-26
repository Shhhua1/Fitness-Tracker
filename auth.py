from supabase import create_client
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

@st.cache_resource
def get_client():
    """Initialize and return a Supabase client."""
    return create_client(SUPABASE_URL, SUPABASE_KEY)

supabase = get_client()
        
def user_signup(email, password):
    """Sign up a new user with email and password."""
    
    response = supabase.auth.sign_up({"email": email, "password": password})
    
    if response.user:
        return {"success": True, "email": response.user.email}
    
    else:
        return {"success": False, "error": response.error.message}
  

def user_login(email, password):
    """Log in a user with email and password."""
    
    response = supabase.auth.sign_in({"email": email, "password": password})
    
    if response.user:
        return {"success": True, "email": response.user.email}
    
    else:
        return {"success": False, "error": response.error.message}
    
