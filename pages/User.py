import streamlit as st
import pandas as pd
from utils import load_model, save_data, load_data

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Loan Application",
    page_icon="🏦",
    layout="wide"
)

# ---------- AUTHENTICATION CHECK ----------
if "logged_in" not in st.session_state or st.session_state.logged_in is False:
    st.warning("🔒 Please login first to access the Loan Application.")
    st.switch_page("pages/Login.py")
    st.stop()

# ---------- MODEL ----------
model = load_model()

# ---------- CSS (Keeping your styles) ----------
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #e0f2fe, #eef2ff); }
header { visibility: hidden; }
.main-title { text-align: center; font-size: 50px; font-weight: 800; color: #0f172a; margin-top: 10px; margin-bottom: 30px; }
label { color: #0f172a !important; font-weight: 700 !important; }
div[data-testid="stTextInput"] div[data-baseweb="input"],
div[data-testid="stNumberInput"] div[data-baseweb="input"] {
    background-color: #1e293b !important; border-radius: 10px !important;
}
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input { color: #f1f5f9 !important; }
.financial-title { font-size: 30px; font-weight: 800; color: #0f172a; margin-top: 25px; margin-bottom: 20px; }
.stButton > button {
    width: 100%; height: 52px; border-radius: 12px;
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white !important; font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🏦 Loan Application Form</div>", unsafe_allow_html=True)

# ---------- FORM ----------
col1, col2 = st.columns(2)
with col1:
    account_no = st.text_input("Account Number")
    fn = st.text_input("Full Name")
    gen = st.selectbox("Gender", ['Female', 'Male'])
    mar = st.selectbox("Marital Status", ['No', 'Yes'])
    dep = st.selectbox("Dependents", ['No', 'One', 'Two', 'More than Two'])

with col2:
    edu = st.selectbox("Education", ['Not Graduate', 'Graduate'])
    emp = st.selectbox("Self Employed", ['No', 'Yes'])
    prop = st.selectbox("Property Area", ['Rural', 'Semi-Urban', 'Urban'])
    cred = st.selectbox("Credit History", ['No', 'Yes'])

st.markdown("<div class='financial-title'>💰 Financial Details</div>", unsafe_allow_html=True)
col3, col4, col5 = st.columns(3)
with col3:
    mon_income = st.number_input("Monthly Income", min_value=0)
with col4:
    co_mon_income = st.number_input("Co-Applicant Income", min_value=0)
with col5:
    loan_amt = st.number_input("Loan Amount", min_value=0)

dur = st.selectbox("Loan Duration", ['2 Month', '6 Month', '8 Month', '1 Year', '16 Month'])

# ---------- SUBMIT & SMART LOGIC ----------
if st.button("🚀 Submit Application"):
    if not fn or not account_no:
        st.warning("⚠ Please fill all required fields")
        st.stop()

    df = load_data()
    if not df.empty and account_no in df["Account No"].values:
        st.error("❌ Account already exists")
        st.stop()

    duration_map = {'2 Month': 2/12, '6 Month': 6/12, '8 Month': 8/12, '1 Year': 1, '16 Month': 16/12}

    # --- SMART VALIDATION ---
    # 1. Agar Credit History 'No' hai, toh 99% chances hain rejection ke
    if cred == 'No':
        ans = 0
    # 2. Agar Loan Amount income ke muqable bahut zyada hai (e.g., 50 times)
    elif loan_amt > (mon_income + co_mon_income) * 50:
        ans = 0
    else:
        # Agar ye basic risk nahi hain, tabhi ML model ka decision maanein
        features = pd.DataFrame([[
            ['Female', 'Male'].index(gen),
            ['No', 'Yes'].index(mar),
            ['No', 'One', 'Two', 'More than Two'].index(dep),
            ['Not Graduate', 'Graduate'].index(edu),
            ['No', 'Yes'].index(emp),
            mon_income, co_mon_income, loan_amt,
            int(duration_map[dur] * 12),
            1 if cred == 'Yes' else 0,
            ['Rural', 'Semi-Urban', 'Urban'].index(prop)
        ]])
        pred = model.predict(features)
        ans = int(pred[0])

    reason = "Approved" if ans else "Rejected"

    # Save data
    save_data([{
        "Account No": account_no,
        "Name": fn,
        "Income": mon_income,
        "Loan Amount": loan_amt,
        "Status": reason
    }])

    # Session storage for details page
    st.session_state.update({
        "name": fn, "loan_amount": loan_amt, "interest": 8.5,
        "years": duration_map[dur], "status": reason, "income": mon_income
    })

    if ans:
        st.success("✅ Congratulations! Your loan is Approved.")
        st.switch_page("pages/loan_details.py")
    else:
        st.error("❌ Sorry, your loan application has been Rejected due to high risk factors.")