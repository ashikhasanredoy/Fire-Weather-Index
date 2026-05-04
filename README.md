# 🔥 Fire Weather Index (FWI) Predictor

A machine learning-powered web application that predicts the **Fire Weather Index (FWI)** based on meteorological data. This project leverages a **Linear Regression** model to provide real-time risk assessments for wildfire occurrence with a beautiful, premium user interface.

## 🚀 Features

- **Real-time Prediction**: Instantly calculate the FWI score from 9 meteorological parameters.
- **Premium UI/UX**: A stunning, fire-themed dark interface featuring:
  - **Animated Fire Particles**: A dynamic background that brings the app to life.
  - **Glassmorphism Design**: Sleek, translucent cards for a modern aesthetic.
  - **Visual Risk Meter**: An animated gauge that color-codes the risk level (Low, Moderate, High, Extreme).
- **Responsive Layout**: Fully optimized for mobile, tablet, and desktop devices.
- **Data-Driven Insights**: Trained on the Algerian Forest Fires dataset for high reliability.

## 🧠 Machine Learning Model

The core of the application is a **Multiple Linear Regression** model.

### Model Performance
- **Algorithm**: Linear Regression (`sklearn.linear_model.LinearRegression`)
- **R² Score**: **98.47%** (High predictive accuracy)
- **Mean Absolute Error (MAE)**: **0.547**
- **Dataset**: Algerian Forest Fires Dataset (Cleaned & Preprocessed)

### Input Parameters
1. **Temperature**: Air temperature in °C.
2. **RH (Relative Humidity)**: Humidity percentage.
3. **Ws (Wind Speed)**: Wind speed in km/h.
4. **Rain**: 24h rainfall accumulation in mm.
5. **FFMC (Fine Fuel Moisture Code)**: Moisture content of fine fuels.
6. **DMC (Duff Moisture Code)**: Moisture content of organic layers.
7. **ISI (Initial Spread Index)**: Rate of fire spread rating.
8. **Classes**: Fire occurrence (0 = No Fire, 1 = Fire).
9. **Region**: 0 = Bejaia, 1 = Sidi-Bel Abbes.

## 🛠️ Technology Stack

- **Backend**: Flask (Python 3.9)
- **Frontend**: HTML5, Vanilla CSS3, JavaScript (Canvas API for animations)
- **Data Science**: Scikit-learn, NumPy, Pandas, Pickle

## ⚙️ Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ashikhasanredoy/Fire-Weather-Index.git
   cd Fire-Weather-Index
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python application.py
   ```

4. **Access the App**:
   Navigate to `http://127.0.0.1:5001` in your web browser.

---
*Developed for Forest Fire Prevention and AI Research.*
