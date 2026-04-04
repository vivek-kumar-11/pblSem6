# pblSem6
# 🚀 Wellness & Productivity Predictor

A machine learning web application that predicts **stress level**, **mental wellness**, and **productivity** using lifestyle and screen-time data.

---

## 📌 Overview

This project uses a **multi-output regression model** to analyze user habits and predict:

- 🧠 Stress Level (0–10)
- 💙 Mental Wellness (0–100)
- ⚡ Productivity (0–100)

The system is deployed as a **Flask web application** and allows users to input daily and weekly habits to get real-time predictions.

---

## 🧠 Features

- Multi-output ML model (Random Forest)
- Real-time predictions via web interface
- Clean and responsive UI
- Automatic calculation of total screen time
- Input validation and user-friendly design
- Deployed on cloud (Render)

---

## 🛠️ Tech Stack

**Frontend**
- HTML
- CSS

**Backend**
- Flask (Python)

**Machine Learning**
- Scikit-learn
- Pandas
- NumPy

**Deployment**
- Gunicorn
- Render

---

## 📊 Input Features

| Feature | Unit |
|--------|------|
| Age | Years |
| Gender | Categorical |
| Occupation | Categorical |
| Work Mode | Remote / Hybrid / In-person |
| Work Screen Time | Hours/day |
| Leisure Screen Time | Hours/day |
| Sleep | Hours/day |
| Sleep Quality | 1–5 |
| Exercise | Minutes/week |
| Social Time | Hours/week |

👉 Total screen time is automatically calculated:
```
screen_time = work + leisure
```

---

## 📈 Model Details

- Algorithm: **Random Forest Regressor**
- Type: **Multi-output regression**
- Targets:
  - Stress Level
  - Mental Wellness Index
  - Productivity Score

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run the app
```
python app.py
```

### 4. Open in browser
```
http://localhost:10000
```

---

## ☁️ Deployment (Render)

- Add `Procfile`:
```
web: gunicorn app:app
```

- Add `runtime.txt`:
```
python-3.11.9
```

- Deploy using Render Web Service

---

## 📂 Project Structure

```
project/
│
├── app.py
├── model2.pkl
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
...
```

---

## 🎯 Key Improvements

- Removed redundant **total screen time input**
- Improved UI clarity with **day/week units**
- Enhanced prediction accuracy using **multi-output learning**
- Cleaned dataset and optimized feature engineering

---

## 🎓 Learning Outcomes

- Multi-output machine learning
- Data preprocessing & feature engineering
- Flask web development
- Model deployment on cloud
- UI/UX improvement for ML apps

---

## 📌 Future Enhancements

- Add personalized health recommendations
- Add visualization dashboard
- Improve model accuracy with advanced algorithms
- Add user authentication & history tracking

---

## 👨‍💻 Author

**Vivek Kumar Ray**  
B.Tech CSE | Bharati Vidyapeeth College of Engineering, Pune  

---

## ⭐ If you like this project
Give it a ⭐ on GitHub!
