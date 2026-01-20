# 📧 AI Powered Smart Email Classifier for Enterprises

An end-to-end **AI-based email classification system** that automatically categorizes customer emails and assigns urgency levels using **Machine Learning** and **Transformer-based models (DistilBERT)**.
This project was developed as part of an **Infosys Internship Program** following an agile, milestone-driven approach.

---

## 🚀 Live Application (Deployed)

🔗 **Web App:**
[https://smart-email-classifier-auvg.onrender.com](https://smart-email-classifier-auvg.onrender.com)

> ⚠️ Note: This application is deployed on Render Free Plan.
> Initial loading may take **30–60 seconds** if the service is idle.

---

## 🖼️ Project Preview
<img width="1919" height="972" alt="image" src="https://github.com/user-attachments/assets/b08c7563-8c5e-4d35-9b0f-e873598eb0a3" />
---

## 📌 Project Overview

Enterprises receive thousands of customer emails daily. Manually reading and prioritizing them is time-consuming and error-prone.
This project automates:

* 📂 **Email Categorization** (Complaint, Request, Feedback, Spam)
* ⏱️ **Urgency Detection** (High / Medium / Low)
* 🤖 **AI-based Decision Making**
* 🌐 **Web-based Deployment**

---

## 🧠 Technologies Used

### Programming & Frameworks

* Python
* Streamlit
* Scikit-learn
* PyTorch

### NLP & ML

* TF-IDF
* Logistic Regression
* Naive Bayes
* DistilBERT (Hugging Face Transformers)

### Deployment

* Hugging Face Model Hub
* GitHub
* Render Cloud Platform

---

## 🗂️ Project Structure

```
smart-email-classifier/
│
├── app.py                 # Streamlit web application
├── requirements.txt       # Project dependencies
├── notebooks/             # Model training & experiments
│   ├── data_preprocessing.ipynb
│   ├── email_classification.ipynb
│   ├── email_classification_distilbert.ipynb
│   └── urgency_detection.ipynb
│
├── documents/             # Internship documentation
│   ├── Unit_Test_Plan_v0.1.xlsx
│   ├── Defect_Tracker_Template_v0.1.xlsx
│   └── Agile_Template_v0.1.xlsx
│
└── README.md
```

---

## 🧪 Milestone-wise Implementation

### 🔹 Milestone 1: Data Collection & Preprocessing

**Duration:** 27 Nov – 11 Dec

**Tasks Completed:**

* Collected Consumer Complaint Dataset from Kaggle
* Removed missing complaint narratives
* Selected relevant columns (text, category, subcategory)
* Performed text cleaning:

  * Lowercasing
  * HTML & URL removal
  * Punctuation & stopwords removal
* Generated final dataset: `cleaned_complaints.csv`

✅ **Milestone 1 Completed Successfully**

---

### 🔹 Milestone 2: Email Classification Model

**Duration:** 11 Dec – 25 Dec

**Models Implemented:**

#### Baseline ML Models

* TF-IDF + Logistic Regression
* TF-IDF + Naive Bayes

**Results:**

* Logistic Regression Accuracy: ~76.8%
* Naive Bayes Accuracy: ~60%

#### Transformer Model

* DistilBERT (Fine-tuned)
* Hugging Face Trainer API

**Outcome:**

* Better contextual understanding
* Lower validation loss (~0.70)

✅ **Milestone 2 Completed Successfully**

---

### 🔹 Milestone 3: Urgency Detection & Scoring

**Duration:** 25 Dec – 8 Jan

**Features:**

* ML-based urgency prediction
* Rule-based keyword detection (urgent, asap, not working)
* Hybrid scoring mechanism

**Output:**

* Final urgency levels: High / Medium / Low

✅ **Milestone 3 Completed Successfully**

---

### 🔹 Milestone 4: Deployment, Testing & Documentation

**Duration:** 8 Jan – 22 Jan

**Completed Tasks:**

* Model uploaded to Hugging Face Hub
* Streamlit web app created
* Deployed on Render Cloud
* Unit Test Plan prepared
* Defect Tracker documented
* End-to-end testing completed

✅ **Milestone 4 Completed Successfully**

---

## 🧾 Testing & Quality Assurance

### Unit Testing

* Data preprocessing validation
* Model prediction verification
* Urgency scoring logic testing

### Defect Tracking

* Logged functional, UI, algorithmic, and performance defects
* All identified issues resolved and verified
* Sprint-wise defect tracking followed

---

## 📈 Key Learnings

* Classical ML models provide strong baselines
* Transformer models significantly improve context understanding
* Hybrid ML + rule-based logic enhances urgency detection
* Real-world deployment requires optimization for memory and startup time

---

## 🔮 Future Enhancements

* Add REST API support
* Improve model accuracy with more epochs
* Add user authentication
* Implement analytics dashboard
* Scale deployment using paid cloud instances

---

## 👨‍💻 Author

**Saurabh Mahavir Raut**
Infosys Internship Program
AI / Machine Learning Domain

---

## 📜 License

This project is licensed under the MIT License.


