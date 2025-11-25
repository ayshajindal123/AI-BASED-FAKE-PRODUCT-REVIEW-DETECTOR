# 🛍️ AI-Based Fake Product Review Detection System  
An intelligent machine-learning powered system that analyzes product reviews and classifies them as **Genuine** or **Fake**, helping users, e-commerce platforms, and brands maintain trust and transparency.

## 🔰 Quick Start (Important for Users)
➡️ **Start the project by running:**  
```bash
python app/app.py

➡️ Frontend loads automatically from:
templates/index.html

## 🚀 Features  
- 🔍 **Real-time review analysis**  
- 🧠 **ML/NLP based classification model**  
- 🌐 **Flask-based backend API**  
- 🖼️ Beautiful **frontend UI** for entering product links  
- 📊 **Review grading**, confidence score, and summary  
- 📄 Auto-generated **PDF report** of analyzed reviews  
- 🧹 Preprocessing: cleaning, stopwords, stemming, lemmatization  
- 📈 Model training using Logistic Regression   

---

## 📂 Project Structure  
project-folder/
AI-BASED-FAKE-PRODUCT-REVIEW-DETECTOR/
│
│── backend/
│    ├── app.py
│    ├── auth.py
│    ├── scraper.py
│    ├── predict.py
│    ├── routes/
│    │     ├── analyze_route.py
│    │     ├── auth_route.py
│    │
│    ├── utils/
│          ├── preprocessing.py
│          ├── pdf_generator.py
│
│
│── frontend/
│    ├── templates/
│    │     ├── index.html
│    │     ├── login.html
│    │     ├── result.html
│    ├── static/
│          ├── css/
│          ├── js/
│          ├── images/
│
│
│── ml/
│    ├── models/
│    │     ├── model.pkl
│    │     ├── vectorizer.pkl
│    ├── training/
│          ├── train_model.py
│          ├── dataset.csv
│
│
│── scripts/
│     ├── scrape_reviews.py
│     ├── generate_pdf.py
│
│── requirements.txt
│── README.md
│── LICENSE
│── .gitignore

> **Note:** Large model files should be uploaded using GitHub Releases or Git LFS.

---

## 🧠 How It Works  
The system follows this pipeline:

1. **Input Review / Product URL**  
2. **Scraping Module** extracts product reviews  
3. **Preprocessing**  
   - Remove HTML  
   - Lowercase  
   - Stopword removal  
   - Stemming / Lemmatization  
4. **Vectorization (TF-IDF)**  
5. **Machine Learning model prediction**  
6. **Output**  
   - Fake / Genuine  
   - Confidence score  
   - Grade (A, B, C...)  
   - PDF report(downloading file after analayse data)

---

## 🛠️ Installation  

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/AI-BASED-FAKE-PRODUCT-REVIEW-DETECTOR.git
cd ai-fake-review-detector

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run Flask server
python app/app.py

4️⃣Open the UI
http://127.0.0.1:5000

🖼️ Screenshots
[Login Page]<img width="1031" height="702" alt="Screenshot 2025-11-24 021544" src="https://github.com/user-attachments/assets/cc8434c8-f6b2-4f92-84fa-c63eda1776ec" />
[Home Page]<img width="1508" height="625" alt="Screenshot 2025-11-24 041140" src="https://github.com/user-attachments/assets/dff038df-2291-49a4-b4a4-877b0b7b4b32" />
[Prediction_Output]<img width="1270" height="712" alt="Screenshot 2025-11-21 213637" src="https://github.com/user-attachments/assets/0f48d1af-9ae0-4900-9ebf-289875a8e77a" />
[Pdf Download]<img width="612" height="523" alt="Screenshot 2025-11-21 213718" src="https://github.com/user-attachments/assets/7dcf5896-c530-49ac-abb1-4a7c383b758c" />


📄 API Endpoints
POST /analyze
Input:
{
  "review": "This product is amazing!"
}
Output:
{
  "prediction": "Genuine",
  "confidence": 0.92,
  "grade": "A"
}

📊 Model Details
Model Type: (Logistic Regression)
Vectorizer: TF-IDF
Dataset: Amazon / Flipkart / Custom-collected dataset
Evaluation Metrics:
Accuracy
Precision
Recall
F1-score

📄 PDF Report Includes
Original review text
Prediction (Fake/Genuine)
Confidence percentage
Summary table
Detailed analysis

🤝 Contribution
Pull requests are welcome!
For major changes, please open an issue before submitting.

📜 License
This project is licensed under the MIT License — you are free to use, modify, and distribute it.

⭐ Support
If you like this project, please ⭐ star this repository!


