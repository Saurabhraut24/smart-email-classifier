import streamlit as st
import torch
import os
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Smart Email Classifier",
    layout="centered"
)

st.title("Smart Email Classification System")
st.write("AI Powered Email Categorization")
st.divider()

# ---------------- Load Model (LOCAL) ----------------
@st.cache_resource
def load_model():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_PATH = os.path.join(BASE_DIR, "notebooks", "distilbert_email_classifier")

    tokenizer = DistilBertTokenizerFast.from_pretrained(
        MODEL_PATH,
        local_files_only=True
    )
    model = DistilBertForSequenceClassification.from_pretrained(
        MODEL_PATH,
        local_files_only=True
    )

    model.eval()
    return tokenizer, model

tokenizer, model = load_model()

# ---------------- Label Map ----------------
label_map = {
    0: "Complaint",
    1: "Request",
    2: "Feedback",
    3: "Spam"
}

# ---------------- UI ----------------
st.subheader("Enter Email Text")

email_text = st.text_area(
    "Paste email here",
    height=180
)

# ---------------- Prediction ----------------
if st.button("Classify Email"):
    if email_text.strip() == "":
        st.warning("Please enter email text before classification.")
    else:
        inputs = tokenizer(
            email_text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128
        )

        with torch.no_grad():
            outputs = model(**inputs)
            prediction = torch.argmax(outputs.logits, dim=1).item()

        st.success(
            f"This email belongs to **{label_map[prediction]}** category."
        )

st.divider()
st.caption("Infosys Internship Project")
