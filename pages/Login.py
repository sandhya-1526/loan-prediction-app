import streamlit as st
from database import login_user

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

# ---------- ALREADY LOGGED IN CHECK ----------
if st.session_state.get("logged_in", False):
    st.switch_page("app.py")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #dbeafe, #eef2ff);
}

header {
    visibility: hidden;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #1e3a8a;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}

.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    border: none;
    background: #2563eb;
    color: white !important;
    font-size: 16px;
    font-weight: bold;
}

label {
    color: #0f172a !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}

div[data-testid="stTextInput"] {
    background-color: transparent !important;
}

div[data-testid="stTextInput"] div[data-baseweb="input"] {
    background-color: #1e293b !important;
    border: 1px solid #475569 !important;
    border-radius: 10px !important;
    min-height: 48px !important;
    padding: 0 12px !important;
}

div[data-testid="stTextInput"] input {
    background-color: #1e293b !important;
    color: #f1f5f9 !important;
    border: none !important;
    border-radius: 10px !important;
    height: 48px !important;
    font-size: 16px !important;
    caret-color: #f1f5f9 !important;
    padding: 0 !important;
}

div[data-testid="stTextInput"] input::placeholder {
    color: #94a3b8 !important;
}

div[data-testid="stAlert"] {
    background-color: white !important;
    border-radius: 10px !important;
}

div[data-testid="stAlert"] p {
    color: #0f172a !important;
    font-weight: 600 !important;
    font-size: 15px !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🔐 Login</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Smart Loan Approval System</div>", unsafe_allow_html=True)

email = st.text_input("📧 Email")
password = st.text_input("🔑 Password", type="password")

if st.button("Login"):
    user = login_user(email, password)
    if user:
        st.session_state.logged_in = True
        st.session_state.username = user[1]
        st.success("✅ Login Successful")
        st.switch_page("app.py")
    else:
        st.error("❌ Invalid Credentials")

st.markdown("---")

if st.button("Create Account"):
    st.switch_page("Signup.py")