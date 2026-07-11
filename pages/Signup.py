import streamlit as st
from database import register_user

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Signup - Smart Loan System",
    page_icon="📝",
    layout="centered"
)

# ---------- CUSTOM CSS (ULTIMATE BOX REMOVAL & TEXT CLARITY) ----------
st.markdown("""
<style>
/* 1. Overall Background */
.stApp {
    background: linear-gradient(135deg, #dbeafe, #eef2ff) !important;
}

/* 2. Hide Streamlit Elements */
header, footer { visibility: hidden !important; }

/* 3. FORCE REMOVE ALL HIDDEN WHITE BOXES & BORDERS */
[data-testid="stVerticalBlock"], 
[data-testid="stVerticalBlockBorderWrapper"],
[data-testid="stVerticalBlockBorderWrapper"] > div,
.st-emotion-cache-1kyx9g7, 
.st-emotion-cache-6qob1r {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* 4. YOUR CUSTOM GLASS-MORPHISM SIGNUP BOX */
.signup-box {
    background: rgba(255, 255, 255, 0.4) !important;
    padding: 3rem;
    border-radius: 25px;
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    width: 100%;
}

/* 5. TEXT STYLING (BLACK & BOLD FOR VISIBILITY) */
.signup-title {
    text-align: center;
    font-size: 40px;
    font-weight: 800;
    color: #000000 !important; /* Title Black */
    margin-bottom: 5px;
}

.signup-subtitle {
    text-align: center;
    color: #1a1a1a !important; /* Subtitle Dark Grey/Black */
    margin-bottom: 25px;
    font-size: 16px;
    font-weight: 500;
}

/* Labels (Username, Password etc.) */
label {
    color: #000000 !important; /* Pure Black */
    font-weight: 800 !important; /* Extra Bold */
    font-size: 15px !important;
    margin-bottom: 5px;
}

/* 6. INPUT FIELDS (TEXT INSIDE BOX) */
.stTextInput > div > div > input {
    background-color: white !important;
    border-radius: 12px !important;
    border: 1px solid #475569 !important;
    height: 48px;
    color: #000000 !important; /* Text inside input BLACK */
    font-weight: 600 !important; /* Slightly bold text */
}

/* Placeholder text visibility */
.stTextInput > div > div > input::placeholder {
    color: #4b5563 !important;
    font-weight: 400;
}

/* 7. BUTTONS */
.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    border: none !important;
    background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: white !important;
    font-size: 16px;
    font-weight: bold;
    margin-top: 15px;
    transition: 0.3s;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #1e40af, #1e3a8a) !important;
    box-shadow: 0px 5px 15px rgba(37, 99, 235, 0.4);
}

/* Footer & "Already have an account" text */
.footer-text, .stWrite {
    text-align: center;
    margin-top: 25px;
    color: #000000 !important;
    font-size: 14px;
    font-weight: 600;
}

div[data-testid="stMarkdownContainer"] p {
    color: #000000 !important; /* General text Black */
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# ---------- UI LAYOUT ----------
#st.markdown("<div class='signup-box'>", unsafe_allow_html=True)

st.markdown("<div class='signup-title'>📝 Create Account</div>", unsafe_allow_html=True)
st.markdown("<div class='signup-subtitle'>Register to access Smart Loan Approval System</div>", unsafe_allow_html=True)

# ---------- INPUT FORM ----------
username = st.text_input("👤 Username", placeholder="Choose a unique username")
email = st.text_input("📧 Email Address", placeholder="name@example.com")
password = st.text_input("🔑 Password", type="password", placeholder="Minimum 6 characters")
confirm_password = st.text_input("🔒 Confirm Password", type="password", placeholder="Repeat your password")

# ---------- SIGNUP LOGIC ----------
if st.button("Create Account"):
    if username == "" or email == "" or password == "" or confirm_password == "":
        st.warning("⚠️ Please fill all fields")
    elif password != confirm_password:
        st.error("❌ Passwords do not match")
    elif len(password) < 6:
        st.warning("⚠️ Password must be at least 6 characters")
    else:
        success = register_user(username, email, password)
        
        if success:
            st.success("✅ Account Created Successfully!")
            st.balloons()
            st.info("👉 Redirecting to Login Page...")
            st.session_state["registered_email"] = email
            st.switch_page("pages/Login.py")
        else:
            st.error("❌ Email already exists or Registration failed")

# ---------- REDIRECT TO LOGIN ----------
st.markdown("<br>", unsafe_allow_html=True)
st.write("Already have an account?")
if st.button("Go to Login"):
    st.switch_page("pages/Login.py")

st.markdown("</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("<div class='footer-text'>❤️ Developed by Sandhya</div>", unsafe_allow_html=True)