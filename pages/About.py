import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

/* ===== BACKGROUND ===== */
.stApp {
    background: linear-gradient(135deg, #dbeafe, #eef2ff, #f8fafc);
    color: #111827;
}

/* ===== REMOVE STREAMLIT HEADER ===== */
header {
    visibility: hidden;
}

/* ===== REMOVE LEFT BARS ===== */
h1, h2, h3, h4, h5, h6,
blockquote,
[data-testid="stMarkdownContainer"] {

    border-left: none !important;

    padding-left: 0px !important;
}

/* ===== TITLE ===== */
.title {

    font-size: 52px;

    font-weight: 700;

    text-align: center;

    color: #1e3a8a;

    margin-top: 20px;

    margin-bottom: 10px;
}

/* ===== SUBTITLE ===== */
.subtitle {

    text-align: center;

    color: #475569;

    margin-bottom: 40px;

    font-size: 20px;
}

/* ===== MAIN CONTAINER ===== */
.about-container {

    background: transparent;

    padding: 10px;

    border-radius: 20px;

    margin-top: 10px;
}

/* ===== SECTION BOX ===== */
.section-box {

    background: rgba(255,255,255,0.25);

    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.3);

    padding: 25px;

    border-radius: 18px;

    margin-bottom: 25px;

    box-shadow: 0px 8px 25px rgba(0,0,0,0.05);
}

/* ===== SECTION TITLE ===== */
.section {

    font-size: 24px;

    font-weight: 700;

    margin-bottom: 15px;

    color: #1e293b;
}

/* ===== TEXT ===== */
p, li {

    font-size: 17px;

    line-height: 1.8;

    color: #374151;
}

/* ===== LIST ===== */
ul {
    padding-left: 20px;
}

/* ===== FOOTER ===== */
.footer {

    text-align: center;

    margin-top: 30px;

    color: #64748b;

    font-size: 15px;
}

/* ===== BUTTON ===== */
.stButton > button {

    width: 100%;

    height: 50px;

    border-radius: 14px;

    background: linear-gradient(135deg, #2563eb, #1d4ed8);

    color: white !important;

    border: none;

    font-size: 16px;

    font-weight: bold;

    margin-top: 20px;
}

/* ===== BUTTON HOVER ===== */
.stButton > button:hover {

    background: linear-gradient(135deg, #1e40af, #1e3a8a);

    transform: scale(1.02);
}

/* ===== HIDE SIDEBAR BUTTON ===== */
[data-testid="collapsedControl"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class='title'>
    💳 Smart Loan Approval System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
    Machine Learning Based Financial Decision Application
</div>
""", unsafe_allow_html=True)

# ---------- MAIN CONTAINER ----------
st.markdown("<div class='about-container'>", unsafe_allow_html=True)

# ---------- OVERVIEW ----------
st.markdown("""
<div class='section-box'>

<div class='section'>
📌 Project Overview
</div>

<p>
This project is a <b>Machine Learning-based Loan Approval System</b>
that predicts whether a loan should be approved or rejected based on
user financial and personal information.

The application helps automate banking decisions using intelligent
prediction models and modern data analysis techniques.
</p>

</div>
""", unsafe_allow_html=True)

# ---------- OBJECTIVES ----------
st.markdown("""
<div class='section-box'>

<div class='section'>
🎯 Objectives
</div>

<ul>
<li>Automate the loan approval process</li>
<li>Reduce manual effort and human errors</li>
<li>Improve financial decision accuracy</li>
<li>Provide fast and reliable predictions</li>
<li>Enhance banking efficiency using AI</li>
</ul>

</div>
""", unsafe_allow_html=True)

# ---------- TECHNOLOGIES ----------
st.markdown("""
<div class='section-box'>

<div class='section'>
⚙️ Technologies Used
</div>

<ul>
<li>Python</li>
<li>Streamlit</li>
<li>Pandas & NumPy</li>
<li>Scikit-learn</li>
<li>SQLite Database</li>
<li>HTML & CSS Styling</li>
</ul>

</div>
""", unsafe_allow_html=True)

# ---------- WORKING ----------
st.markdown("""
<div class='section-box'>

<div class='section'>
🧠 How It Works
</div>

<ul>
<li>User enters financial and personal details</li>
<li>Data is processed and validated</li>
<li>Machine Learning model analyzes the data</li>
<li>Loan approval prediction is generated</li>
<li>Final decision is displayed instantly</li>
</ul>

</div>
""", unsafe_allow_html=True)

# ---------- DEVELOPER ----------
st.markdown("""
<div class='section-box'>

<div class='section'>
👩‍💻 Developed By
</div>

<p>
<b>Sandhya Bhardwaj</b><br>
B.Tech CSE (3rd Year, 6th Semester)<br>
Machine Learning & Data Analytics Enthusiast
</p>

</div>
""", unsafe_allow_html=True)

# ---------- BACK BUTTON ----------
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

# ---------- CLOSE CONTAINER ----------
st.markdown("</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div class='footer'>
    ❤️ Developed by Sandhya 
</div>
""", unsafe_allow_html=True)