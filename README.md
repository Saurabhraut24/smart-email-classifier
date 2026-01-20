# Smart Email Classifier
## Milestone 1 – Data Collection & Preprocessing

In Milestone 1, we focused on collecting and preprocessing the dataset required for training
the email classification model.

### Key Steps
- Collected Consumer Complaint Dataset from Kaggle
- Removed missing complaint narratives
- Selected relevant columns (text, category, subcategory)
- Performed text cleaning (lowercasing, stopwords removal, punctuation removal)
- Generated final cleaned dataset: `cleaned_complaints.csv`

📄 Detailed report is available in:
`reports/Milestone_1_Report.pdf`

## Smart Email Classification – Milestone 2

### Objective
Build an NLP-based machine learning system to classify customer emails into predefined categories using both traditional machine learning models and transformer-based models.

---

## Project Overview
This project focuses on automated email categorization for enterprises.  
It demonstrates a complete NLP pipeline starting from data preprocessing to model training and evaluation using both classical ML and modern transformer-based techniques.

---

## Dataset
- Source: Cleaned consumer complaints dataset (prepared in Milestone 1)
- Input: Email / complaint text
- Output: Category label
- Number of classes: 9

---

## Models Implemented

### 1. Baseline Machine Learning Models
Traditional NLP approach using TF-IDF features.

#### Techniques Used
- Text cleaning and preprocessing
- TF-IDF Vectorization (max features = 5000)
- Train–test split
- Model evaluation using accuracy and classification report

#### Models
- Logistic Regression (primary baseline model)
- Multinomial Naive Bayes (baseline comparison)

#### Results
- Logistic Regression Accuracy: ~76.8%
- Naive Bayes Accuracy: ~60%

Logistic Regression outperformed Naive Bayes and was selected as the best baseline model.

---

### 2. Transformer-Based Model (DistilBERT)
To improve contextual understanding, a transformer-based model was fine-tuned.

#### Model Used
- distilbert-base-uncased

#### Approach
- Tokenization using DistilBERT tokenizer
- Label encoding for multi-class classification
- Fine-tuning DistilBERT using Hugging Face Trainer API
- Evaluation on validation dataset

#### Training Configuration
- Epochs: 2
- Batch size: 8
- Learning rate: 2e-5
- Optimizer: AdamW
- Loss function: Cross-Entropy Loss

#### Evaluation Metrics
- Validation Loss (eval_loss): ~0.70  
This shows better semantic and contextual understanding compared to traditional ML models.

---

## Key Learnings
- Classical ML models provide strong baselines for text classification.
- Transformer-based models capture deeper contextual meaning.
- Fine-tuning pre-trained language models significantly improves performance on real-world text data.

---

## Conclusion
This project successfully demonstrates email classification using both traditional machine learning and transformer-based approaches.  
The DistilBERT model enhances contextual understanding and provides a scalable solution for enterprise-level email categorization.

---

## Future Enhancements
- Train DistilBERT for more epochs using GPU
- Add accuracy, precision, recall, and F1-score for transformer model
- Experiment with larger models like BERT or RoBERTa
- Deploy the model as a REST API or web application

## 🔹 Milestone 3: Urgency Detection & Scoring 

#### Objective
Implement an urgency detection module to identify and prioritize critical customer emails by assigning urgency levels.

#### Tasks Completed
- Trained an urgency classification model using machine learning techniques.
- Identified urgency signals using keyword-based rules (e.g., urgent, asap, not working).
- Combined machine learning predictions with rule-based keyword detection for improved accuracy.
- Generated a final urgency score by merging ML probability and keyword-based urgency signals.
- Validated urgency predictions using sample outputs and evaluation metrics.

#### Implementation Details
- Implemented urgency detection logic in `urgency_detection.ipynb`.
- Used ML probability scores along with keyword weighting to calculate the final urgency score.
- Created a final dataframe containing:
  - Email text  
  - Actual urgency  
  - ML probability  
  - Final urgency score  

#### Output
- Successfully assigned urgency levels (High / Medium / Low) to customer emails.
- The urgency detection module is ready for integration with classification and dashboard components.

**Milestone 3 has been successfully completed.**

































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

> *(You can add one screenshot image of your deployed web app)*

```markdown
![Smart Email Classifier UI](images/app_preview.png)
```

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


