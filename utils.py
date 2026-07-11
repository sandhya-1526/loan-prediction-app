import pickle
import pandas as pd
import os

# ---------- BASE DIRECTORY ----------
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

# ---------- MODEL PATH ----------
MODEL_PATH = os.path.join(
    BASE_DIR,
    "ML_Model1.pkl"
)

# ---------- DATA FILE ----------
DATA_FILE = os.path.join(
    BASE_DIR,
    "loan_data.csv"
)

# ---------- LOAD MACHINE LEARNING MODEL ----------
def load_model():

    try:

        with open(MODEL_PATH, "rb") as file:

            model = pickle.load(file)

        return model

    except Exception as e:

        print("Model Loading Error:", e)

        return None

# ---------- SAVE LOAN DATA ----------
def save_data(data):

    df = pd.DataFrame(data)

    # ---------- APPEND DATA ----------
    if os.path.exists(DATA_FILE):

        df.to_csv(
            DATA_FILE,
            mode="a",
            header=False,
            index=False
        )

    # ---------- CREATE FILE ----------
    else:

        df.to_csv(
            DATA_FILE,
            index=False
        )

# ---------- LOAD LOAN DATA ----------
def load_data():

    if os.path.exists(DATA_FILE):

        return pd.read_csv(DATA_FILE)

    # ---------- EMPTY DATAFRAME ----------
    return pd.DataFrame()

# ---------- CLEAR DATA ----------
def clear_data():

    if os.path.exists(DATA_FILE):

        os.remove(DATA_FILE)