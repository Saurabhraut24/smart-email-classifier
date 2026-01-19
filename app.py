import streamlit as st
import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Smart Email Classifier",
    layout="centered"
)

st.title("Smart Email Classification System")
st.write("AI Powered Email Categorization")
st.divider()

# ---------------- Load Model (FROM HUGGING FACE) ----------------
@st.cache_resource
def load_model():
    model_name = "Saurabhraut123/distilbert-email-classifier"

    tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)
    model = DistilBertForSequenceClassification.from_pretrained(model_name)

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
