# Spam Detection using Naive Bayes and Count Vectorizer 📧

Welcome to my **Spam Detection** project, where I've implemented a machine learning model to classify messages as spam or not spam. The model uses the **Naive Bayes classifier** along with the **Count Vectorizer** for text feature extraction. This project demonstrates the power of natural language processing (NLP) in automating text classification tasks. Spam_checker.ipynb contains the notebook for the main processing and training of the model.
app.py contains the streamlit integration.
---

## 🎯 Project Goals

- Build a machine learning model to classify text messages as **spam** or **not spam**.
- Use **Naive Bayes** as the classification algorithm and **Count Vectorizer** for text feature extraction.
- Preprocess text data by removing stopwords, punctuation, and applying tokenization and lemmatization.

---

## 📊 How the Model Works

1. **Data Preprocessing**  
   - The dataset is first cleaned by removing unnecessary characters, stopwords, and punctuation.
   - The text data is then tokenized and lemmatized to reduce words to their base form.

2. **Feature Extraction**  
   - The **Count Vectorizer** is used to convert text into numerical features, creating a bag-of-words model.

3. **Model Training**  
   - The **Naive Bayes classifier** is trained on the processed dataset to classify messages as spam or not spam.

4. **Model Evaluation**  
   - The performance of the model is evaluated using accuracy, precision, recall, and F1-score metrics.

---

## 🛠️ How to Use

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/ThisIsFarhan/SPAM-CHECKER.git
