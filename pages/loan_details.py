import streamlit as st
import math

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Loan Details",
    page_icon="💰",
    layout="centered"
)

# ---------- GET USER DATA ----------
loan_amount = st.session_state.get("loan_amount", 0)
annual_interest = st.session_state.get("interest", 8.5)
years = st.session_state.get("years", 1)
name = st.session_state.get("name", "User")
status = st.session_state.get("status", "Rejected")
income = st.session_state.get("income", 0)

# ---------- EMI CALCULATION ----------
monthly_interest = annual_interest / 12 / 100
months = years * 12

if monthly_interest > 0:
    emi = (
        loan_amount *
        monthly_interest *
        ((1 + monthly_interest) ** months)
    ) / (((1 + monthly_interest) ** months) - 1)
else:
    emi = loan_amount / months

total_payment = emi * months
total_interest = total_payment - loan_amount

# ---------- CSS ----------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #dbeafe, #eef2ff);
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #1e3a8a;
    margin-bottom: 30px;
}

.box {
    padding: 25px;
    border-radius: 18px;
    background: rgba(255,255,255,0.35);
    backdrop-filter: blur(10px);
}

.detail {
    font-size: 20px;
    margin-bottom: 15px;
    color: #0f172a;
}

.result {
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    color: green;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------- UI ----------
st.markdown("""
<div class='title'>
💳 Loan Details
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='box'>", unsafe_allow_html=True)

st.markdown(f"<div class='detail'><b>Applicant:</b> {name}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='detail'><b>Monthly Income:</b> ₹{income:,}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='detail'><b>Loan Amount:</b> ₹{loan_amount:,}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='detail'><b>Interest Rate:</b> {annual_interest}%</div>", unsafe_allow_html=True)
st.markdown(f"<div class='detail'><b>Loan Duration:</b> {years} Years</div>", unsafe_allow_html=True)
st.markdown(f"<div class='detail'><b>Monthly EMI:</b> ₹{emi:,.2f}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='detail'><b>Total Interest:</b> ₹{total_interest:,.2f}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='detail'><b>Total Payment:</b> ₹{total_payment:,.2f}</div>", unsafe_allow_html=True)

st.markdown(f"<div class='result'>✅ Loan {status}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------- BUTTON ----------
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")