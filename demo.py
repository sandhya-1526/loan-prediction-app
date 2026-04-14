import streamlit as st
from PIL import Image
import pickle
import pandas as pd
import os
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Bank Loan Predictor", layout="centered")

# 🎨 UI STYLE
st.markdown("""
<style>
.big-title {
    font-size:30px !important;
    font-weight:bold;
    color:#4CAF50;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(BASE_DIR, 'ML_Model1.pkl')

    with open(model_path, 'rb') as f:
        return pickle.load(f)

model = load_model()

# ---------------- FILE STORAGE ----------------
FILE = "loan_data.csv"

def save_data(data):
    df = pd.DataFrame(data)
    if os.path.exists(FILE):
        df.to_csv(FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(FILE, index=False)

def load_data():
    if os.path.exists(FILE):
        return pd.read_csv(FILE)
    return pd.DataFrame()

# ---------------- ADMIN LOGIN ----------------
def admin_login():
    st.sidebar.subheader("🔐 Admin Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state["admin"] = True
        else:
            st.sidebar.error("Invalid credentials")

# ---------------- ADMIN PAGE ----------------
def admin_page():
    st.title("📊 Admin Dashboard")

    if st.button("Logout"):
        st.session_state["admin"] = False
        st.rerun()

    df = load_data()

    if df.empty:
        st.warning("No applications yet")
        return

    df["Status"] = df["Status"].fillna("Pending")

    st.subheader("🔍 Search Application")
    search_name = st.text_input("Search by Name")

    if search_name:
        df = df[df["Name"].str.contains(search_name, case=False)]

    df = df[::-1]

    df["Loan Amount"] = df.apply(
        lambda x: x["Loan Amount"] if x["Status"] == "Approved" else "—",
        axis=1
    )

    def highlight_status(val):
        if val == "Approved":
            return "background-color: #d4edda; color: green; font-weight: bold;"
        elif val == "Rejected":
            return "background-color: #f8d7da; color: red; font-weight: bold;"
        else:
            return "background-color: #fff3cd; color: orange; font-weight: bold;"

    st.subheader("📄 All Applications")
    st.dataframe(df.style.applymap(highlight_status, subset=["Status"]), use_container_width=True)

    st.subheader("📈 Summary")

    total = len(df)
    approved = len(df[df["Status"] == "Approved"])
    rejected = len(df[df["Status"] == "Rejected"])
    pending = len(df[df["Status"] == "Pending"])

    total_amount = df[df["Status"] == "Approved"]["Loan Amount"]
    total_amount = pd.to_numeric(total_amount, errors='coerce').sum()

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total", total)
    col2.metric("Approved", approved)
    col3.metric("Rejected", rejected)
    col4.metric("Pending", pending)
    col5.metric("💰 Approved Amount", f"₹ {int(total_amount)}")

    st.subheader("📊 Loan Status Distribution")
    pie_data = pd.DataFrame({
        'Status': ['Approved', 'Rejected', 'Pending'],
        'Count': [approved, rejected, pending]
    })
    st.pyplot(pie_data.set_index('Status').plot.pie(y='Count', autopct='%1.1f%%').figure)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Data", csv, "loan_data.csv", "text/csv")

    if st.button("🗑️ Clear All Data"):
        if os.path.exists(FILE):
            os.remove(FILE)
            st.success("All data deleted successfully!")
            st.rerun()

# ---------------- USER PAGE ----------------
def user_page():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(BASE_DIR, 'bank.png')

    img1 = Image.open(img_path)
    img1 = img1.resize((156,145))
    st.image(img1)

    st.title("🏦 Bank Loan Prediction")

    account_no = st.text_input('Account Number')
    fn = st.text_input('Full Name')

    gen = st.selectbox("Gender", ['Female','Male'])
    mar = st.selectbox("Marital Status", ['No','Yes'])
    dep = st.selectbox("Dependents", ['No','One','Two','More than Two'])
    edu = st.selectbox("Education", ['Not Graduate','Graduate'])

    emp = st.selectbox("Self Employed", ['No','Yes'])
    prop = st.selectbox("Property Area", ['Rural','Semi-Urban','Urban'])
    cred = st.selectbox("Credit History", ['No','Yes'])

    mon_income = st.number_input("Applicant Monthly Income", min_value=0)
    co_mon_income = st.number_input("Co-Applicant Income", min_value=0)
    loan_amt = st.number_input("Loan Amount", min_value=0)

    dur = st.selectbox("Loan Duration",
                       ['2 Month','6 Month','8 Month','1 Year','16 Month'])

    if st.button("Submit"):

        if not fn or not account_no:
            st.warning("Please fill all required fields")
            return

        existing_df = load_data()
        if not existing_df.empty and account_no in existing_df["Account No"].values:
            st.error("Account Number already exists!")
            return

        duration_map = {
            '2 Month': 60,
            '6 Month': 180,
            '8 Month': 240,
            '1 Year': 360,
            '16 Month': 480
        }

        duration = duration_map[dur]

        columns = [
            'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
            'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
            'Loan_Amount_Term', 'Credit_History', 'Property_Area'
        ]

        features_df = pd.DataFrame([[ 
            ['Female','Male'].index(gen),
            ['No','Yes'].index(mar),
            ['No','One','Two','More than Two'].index(dep),
            ['Not Graduate','Graduate'].index(edu),
            ['No','Yes'].index(emp),
            mon_income,
            co_mon_income,
            loan_amt,
            duration,
            1 if cred == 'Yes' else 0,
            ['Rural','Semi-Urban','Urban'].index(prop)
        ]], columns=columns)

        with st.spinner("Processing..."):
            prediction = model.predict(features_df)
            ans = int(prediction[0])

        # 🔥 SMART RULES + REASONS
        reason = ""

        if cred == "No":
            ans = 0
            reason = "❌ No Credit History"

        elif mon_income < 2000:
            ans = 0
            reason = "❌ Income too low"

        elif loan_amt > (mon_income * 10):
            ans = 0
            reason = "❌ Loan amount too high compared to income"

        elif cred == "Yes" and mon_income > 50000 and loan_amt < 200000:
            ans = 1
            reason = "✅ Good income & credit profile"

        status = "Approved" if ans == 1 else "Rejected"

        save_data([{
            "Account No": account_no,
            "Name": fn,
            "Income": mon_income,
            "Loan Amount": loan_amt,
            "Status": status
        }])

        # 🎯 SHOW RESULT WITH REASON
        if ans == 0:
            st.error(f"{fn} → Loan NOT Approved ❌")
            st.warning(f"Reason: {reason}")
        else:
            st.success(f"🎉 Congratulations {fn}! Your Loan is Approved ✅")
            st.info(f"Reason: {reason}")

# ---------------- MAIN ----------------
def run():
    admin_login()

    if "admin" in st.session_state and st.session_state["admin"]:
        admin_page()
    else:
        user_page()

run()