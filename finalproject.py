import re
import streamlit as st

# Function to check password strength
def password_strength(password):
    length_criteria = len(password) >= 8
    digit_criteria = bool(re.search(r'\d', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    score = sum([length_criteria, digit_criteria, lowercase_criteria, uppercase_criteria, special_char_criteria])
    
    if score == 5:
        return "Strong"
    elif 3 <= score < 5:
        return "Moderate"
    else:
        return "Weak"

# Streamlit app
def main():
    st.title("Password Strength Detector")
    
    password = st.text_input("Enter your password", type="password")
    
    if st.button("Check Strength"):
        if password:
            strength = password_strength(password)
            st.success(f"Password strength: {strength}")
        else:
            st.error("Please enter a password")

if __name__ == "__main__":
    main()
