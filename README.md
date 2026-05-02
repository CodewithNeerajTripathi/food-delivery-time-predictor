# Food Delivery Time Predictor

> An end-to-end Machine Learning project that predicts food delivery time based on real-world factors like distance, traffic, weather, and courier experience.

---

## Project Overview

This project uses a **Random Forest Regressor** model trained on real delivery data to predict how long a food delivery will take. The model is served through a **Flask REST API** and connected to a clean **HTML/CSS/JS frontend**.

---

## Model Performance

| Metric | Score |
|--------|-------|
| MAE | 6.91 minutes |
| RMSE | 9.89 |
| R² Score | 0.78 |

---

## Features Used

| Feature | Description |
|---------|-------------|
| Distance (km) | Distance from restaurant to delivery location |
| Traffic Level | Low / Medium / High |
| Weather Condition | Clear / Foggy / Windy / Rainy / Snowy |
| Courier Experience | Years of experience of delivery person |
| Vehicle Type | Bike / Car / Scooter |
| Time of Day | Morning / Afternoon / Evening / Night |
| Preparation Time | Time taken to prepare the food |

---

## Tech Stack

**Machine Learning**
- Python
- Scikit-learn (Random Forest Regressor)
- Pandas, NumPy
- Matplotlib, Seaborn

**Backend**
- Flask
- Flask-CORS
- Pickle

**Frontend**
- HTML5
- CSS3
- JavaScript (Fetch API)

---

## Project Structure

```
food-delivery-time-predictor/
├── 📁 backend/
│   ├── app.py              # Flask REST API
│   └── requirements.txt    # Python dependencies
├── 📁 data/
│   └── Food_Delivery_Times.csv   # Dataset
├── 📁 model/
│   └── model.pkl           # Trained ML model
├── 📁 src/
│   └── eda_model.ipynb     # EDA + Model training notebook
├── index.html              # Frontend UI
└── README.md
```

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/CodewithNeerajTripathi/food-delivery-time-predictor.git
cd food-delivery-time-predictor
```

### 2. Install dependencies
```bash
pip install -r backend/requirements.txt
```

### 3. Run the Flask API
```bash
cd backend
python app.py
```

### 4. Open the frontend
Open `index.html` in your browser

---

##  Key Highlights

- ✅ Complete end-to-end ML pipeline
- ✅ Smart feature engineering (traffic-distance, bad weather flag, experience-distance ratio)
- ✅ REST API with error handling
- ✅ Clean and responsive frontend UI
- ✅ Input validation on both frontend and backend

---

## Author

**Neeraj Kumar**
- GitHub: [@CodewithNeerajTripathi](https://github.com/CodewithNeerajTripathi)
- LinkedIn: https://www.linkedin.com/in/neeraj-kumar-baaa44295/?locale=en

---
