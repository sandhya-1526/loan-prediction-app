import streamlit as st

st.set_page_config(
    page_title="Smart Loan System",
    page_icon="🏦",
    layout="wide"
)

# ---------- LOGIN CHECK ----------
# Agar session state initialize nahi hai ya logged_in False hai
if "logged_in" not in st.session_state or st.session_state.logged_in is False:
    st.session_state.logged_in = False
    st.warning("🔒 Please login to access the system.")
    st.switch_page("pages/Login.py")
    st.stop()  # Iske niche ka code run nahi hoga jab tak login na ho

# ---------- CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #dbeafe, #eef2ff, #f8fafc);
    color: #111827;
}
header {
    visibility: hidden;
}
.title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: #1e3a8a;
    margin-top: 20px;
}
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #475569;
    margin-bottom: 50px;
}
.card {
    background: white;
    border-radius: 20px;
    padding: 30px 20px;
    text-align: center;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 10px;
    min-height: 250px;
}
.card-icon {
    font-size: 55px;
    margin-bottom: 10px;
}
.card-title {
    font-size: 22px;
    font-weight: bold;
    color: #1e3a8a;
    margin-bottom: 8px;
}
.card-text {
    font-size: 14px;
    color: #6b7280;
    margin-bottom: 18px;
}
.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 14px;
    border: none;
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white !important;
    font-size: 16px;
    font-weight: bold;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #1e40af, #1e3a8a);
}
.welcome {
    font-size: 16px;
    font-weight: 600;
    color: #1e3a8a;
}
.footer {
    text-align: center;
    margin-top: 50px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# ---------- WELCOME + LOGOUT ----------
col_left, col_right = st.columns([6, 1])

with col_left:
    username = st.session_state.get('username', 'User')
    st.markdown(f"<div class='welcome'>👋 Welcome, {username}!</div>", unsafe_allow_html=True)

with col_right:
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun() # Refresh karke auth check trigger karega

# ---------- HEADER ----------
st.markdown("<div class='title'>🏦 Smart Loan Approval System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Fast • Secure • AI Powered Loan Decisions</div>", unsafe_allow_html=True)

# ---------- CARDS ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='card'>
        <div class='card-icon'>📝</div>
        <div class='card-title'>Apply Loan</div>
        <div class='card-text'>Fill form and get instant AI-based loan decision</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Apply Now"):
        st.switch_page("pages/User.py")

with col2:
    st.markdown("""
    <div class='card'>
        <div class='card-icon'>📊</div>
        <div class='card-title'>Analytics</div>
        <div class='card-text'>View charts and statistics of all loan applications</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Dashboard"):
        st.switch_page("pages/Analytics.py")

with col3:
    st.markdown("""
    <div class='card'>
        <div class='card-icon'>👨‍💼</div>
        <div class='card-title'>Admin Panel</div>
        <div class='card-text'>Manage and monitor all loan applications</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Admin Access"):
        st.switch_page("pages/Admin.py")

with col4:
    st.markdown("""
    <div class='card'>
        <div class='card-icon'>ℹ️</div>
        <div class='card-title'>About Project</div>
        <div class='card-text'>Learn about this Smart Loan Approval System</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("About"):
        st.switch_page("pages/About.py")

# ---------- FOOTER ----------
st.markdown("<div class='footer'>❤️ Developed by Sandhya</div>", unsafe_allow_html=True)