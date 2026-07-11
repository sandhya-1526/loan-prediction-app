import streamlit as st
import pandas as pd
from utils import load_data, clear_data

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------- LOGIN CHECK ----------
if not st.session_state.get("logged_in", False):
    st.switch_page("pages/Login.py")

# ---------- SESSION ----------
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #dbeafe, #eef2ff);
}

header {
    visibility: hidden;
}

/* Title */
.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #1e3a8a;
    margin-bottom: 25px;
}

/* KPI Card */
.kpi-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
}

/* KPI Number */
.kpi-number {
    font-size: 30px;
    font-weight: bold;
    color: #2563eb;
}

/* KPI Label */
.kpi-label {
    color: #6b7280;
}

/* LABEL FIX */
label {
    color: #0f172a !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}

/* SUBHEADER COLOR FIX */
h3 {
    color: #0f172a !important;
}

/* outer container */
div[data-testid="stTextInput"] {
    background-color: transparent !important;
}

/* inner baseweb wrapper */
div[data-testid="stTextInput"] div[data-baseweb="input"] {
    background-color: #1e293b !important;
    border: 1px solid #475569 !important;
    border-radius: 10px !important;
    min-height: 48px !important;
    padding: 0 12px !important;
}

/* actual input */
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

/* placeholder */
div[data-testid="stTextInput"] input::placeholder {
    color: #94a3b8 !important;
}

/* Buttons */
.stButton > button {
    width: 100%;
    height: 48px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white !important;
    font-size: 16px;
    font-weight: bold;
}

/* WARNING / ERROR / SUCCESS */
div[data-testid="stAlert"] {
    background-color: white !important;
    border-radius: 10px !important;
}

div[data-testid="stAlert"] p {
    color: #0f172a !important;
    font-weight: 600 !important;
    font-size: 15px !important;
}

/* REMOVE EXTRA BOX */
[data-testid="stVerticalBlock"] {
    background: transparent !important;
    box-shadow: none !important;
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<div class='title'>📊 Admin Dashboard</div>", unsafe_allow_html=True)

# ---------- ADMIN LOGIN ----------
if not st.session_state.admin_logged_in:

    username = st.text_input("👤 Admin Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Login as Admin"):
        if username == "admin" and password == "1234":
            st.session_state.admin_logged_in = True
            st.success("✅ Admin Login Successful")
            st.rerun()
        else:
            st.error("❌ Invalid Admin Credentials")

    st.stop()

# ---------- LOAD DATA ----------
df = load_data()

# ---------- NO DATA ----------
if df.empty:
    st.warning("⚠ No loan application data found")

# ---------- DASHBOARD ----------
else:

    total_apps = len(df)
    approved = len(df[df["Status"] == "Approved"])
    rejected = len(df[df["Status"] == "Rejected"])
    total_loan = df["Loan Amount"].sum()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-number'>{total_apps}</div>
            <div class='kpi-label'>Applications</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-number'>{approved}</div>
            <div class='kpi-label'>Approved</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-number'>{rejected}</div>
            <div class='kpi-label'>Rejected</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-number'>₹{total_loan:,}</div>
            <div class='kpi-label'>Total Loan</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    col5, col6 = st.columns(2)

    with col5:
        st.subheader("📌 Loan Status")
        st.bar_chart(df["Status"].value_counts())

    with col6:
        st.subheader("💰 Income vs Loan Amount")
        st.scatter_chart(df[["Income", "Loan Amount"]])

    st.markdown("---")

    st.subheader("📝 All Loan Applications")
    st.dataframe(df, use_container_width=True)

# ---------- ACTION BUTTONS ----------
col7, col8, col9 = st.columns(3)

with col7:
    if st.button("⬅ Back to Home"):
        st.switch_page("app.py")

with col8:
    if st.button("🗑 Clear All Data"):
        clear_data()
        st.success("✅ Data Cleared Successfully")
        st.rerun()

with col9:
    if st.button("🚪 Logout Admin"):
        st.session_state.admin_logged_in = False
        st.rerun()