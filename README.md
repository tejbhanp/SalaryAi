# 💼 SalaryAi

**SalaryAi** is an AI-powered salary prediction web application built using FastAPI, Machine Learning, HTML, CSS, and JavaScript. It enables users to input professional details such as age, gender, education level, job title, and years of experience — and instantly get a predicted salary based on trained data.

> ⚠️ **Note:** This application is based on salary data from the **United States**. Predictions are aligned with typical U.S. salary ranges.

---

## 🚀 Features

* 🧠 Machine learning-powered salary predictions
* 🌐 Fast and lightweight API built with FastAPI
* 🎨 Responsive and user-friendly frontend interface
* ⬇️ Dynamic dropdowns populated directly from training dataset values
* 📦 Model and preprocessing pipeline stored using `joblib`

---

## 💠 Tech Stack

| Category         | Tools Used                           |
| ---------------- | ------------------------------------ |
| Backend          | Python, FastAPI                      |
| Frontend         | HTML, CSS, JavaScript                |
| Machine Learning | Pandas, Scikit-learn, Joblib         |
| API Testing      | FastAPI Docs (Swagger UI)            |
| Deployment       | Uvicorn (Locally) / Render           |

---

## 📊 Dataset Fields

* `Age` (Float)
* `Gender` (Dropdown: e.g., Male, Female, Other)
* `Education Level` (Dropdown: e.g., Bachelor's, Master's, PhD)
* `Job Title` (Dropdown: 190+ options from dataset)
* `Years of Experience` (Float)

---

## 🖼️ Screenshot

![SalaryAi Screenshot](screenshot.png) <!-- Replace with actual path to screenshot -->

---

## 🔧 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SalaryAi.git
cd SalaryAi
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
uvicorn main:app --reload
```

### 4. Access the Interface

* Visit the frontend page at: `http://localhost:8000`
* Or use the Swagger API at: `http://localhost:8000/docs`

---

## 📂 Project Structure

```
SalaryAi/
├── main.py                # FastAPI backend
├── predict_salary.pkl     # Trained ML pipeline      
├── static/
│   ├── index.html         # CSS styling, JavaScript logic
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 📌 Future Improvements

* Add more countries and currencies
* Authentication for user-specific history
* Visualize trends with graphs (experience vs salary, etc.)
* Host the model API on cloud

---

## 🧑‍💻 Author

**Anik Chand**
[LinkedIn](https://www.linkedin.com/in/anikchand) • [GitHub](https://github.com/yourusername)

---

## 📄 License

This project is licensed under the MIT License.
