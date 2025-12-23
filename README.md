# Smart Email Classifier

## Smart Email Classification – Milestone 2

## Objective
Build an NLP-based machine learning model to classify customer emails into predefined categories.

## Steps Implemented
- Loaded cleaned dataset generated in Milestone 1
- Converted email text into numerical features using TF-IDF Vectorizer
- Split the dataset into training and testing sets
- Trained baseline classification models
- Evaluated models using accuracy and classification report

## Models Used
- Logistic Regression (Primary model)
- Multinomial Naive Bayes (Baseline comparison)
- TF-IDF features (max_features = 5000)

## Results
- Logistic Regression Accuracy: ~76.8%
- Naive Bayes Accuracy: ~60%

Logistic Regression outperformed Naive Bayes and was selected as the final model for Milestone 2.  
The model shows stable and generalized performance across most categories.

## Files
- notebooks/data_preprocessing.ipynb
- notebooks/email_classification.ipynb

