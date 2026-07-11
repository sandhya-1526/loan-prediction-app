import streamlit as st
import pandas as pd
from utils import load_data

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------- LOGIN CHECK ----------
if not st.session_state.get("logged_in", False):
    st.switch_page("pages/Login.py")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #dbeafe, #eef2ff);
}

/* Title */
.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #1e3a8a;
    margin-bottom: 30px;
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
    font-size: 32px;
    font-weight: bold;
    color: #2563eb;
}

/* KPI Label */
.kpi-label {
    font-size: 16px;
    color: #6b7280;
}

/* SUBHEADER COLOR FIX */
h3 {
    color: #0f172a !important;
}

/* REMOVE EXTRA BOX */
[data-testid="stVerticalBlock"] {
    background: transparent !important;
    box-shadow: none !important;
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<div class='title'>📊 Loan Analytics Dashboard</div>", unsafe_allow_html=True)

# ---------- LOAD DATA ----------
df = load_data()

# ---------- EMPTY DATA ----------
if df.empty:
    st.warning("⚠ No loan applications found")

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
            <div class='kpi-label'>Total Applications</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-number'>{approved}</div>
            <div class='kpi-label'>Approved Loans</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-number'>{rejected}</div>
            <div class='kpi-label'>Rejected Loans</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-number'>₹{total_loan:,}</div>
            <div class='kpi-label'>Total Loan Amount</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    col5, col6 = st.columns(2)

    with col5:
        st.subheader("📌 Approval Status")
        status_count = df["Status"].value_counts()
        st.bar_chart(status_count)

    with col6:
        st.subheader("💰 Income vs Loan Amount")
        st.scatter_chart(df[["Income", "Loan Amount"]])

    st.markdown("---")

    st.subheader("📝 Recent Loan Applications")
    st.dataframe(df.tail(10), use_container_width=True)

# ---------- BUTTON ----------
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")