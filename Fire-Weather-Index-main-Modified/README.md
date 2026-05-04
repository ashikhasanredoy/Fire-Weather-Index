# 🔥 Fire Weather Index (FWI) Predictor

A machine learning-powered web application that predicts the **Fire Weather Index (FWI)** based on meteorological data. The project uses a trained **Linear Regression** model to provide real-time risk assessments for wildfire occurrence.

## 🚀 Features

- **Real-time Prediction**: Instantly calculate the FWI score from 9 weather parameters.
- **Dynamic UI**: A premium, fire-themed interface with glassmorphism, animations, and a risk indicator meter.
- **Responsive Design**: Fully optimized for mobile, tablet, and desktop views.
- **Accurate Insights**: Leveraging a high-performance ML model trained on the Algerian Forest Fires dataset.

## 🧠 Machine Learning Model

The backend is powered by a **Multiple Linear Regression** model.

### Model Performance
- **Algorithm**: Linear Regression (`sklearn.linear_model.LinearRegression`)
- **R² Score**: **98.47%** (The model explains ~98.5% of the variance in the data)
- **Mean Absolute Error (MAE)**: **0.547**
- **Dataset**: Algerian Forest Fires Dataset (Cleaned & Preprocessed)

### Input Parameters
1. **Temperature**: Air temperature in °C.
2. **RH (Relative Humidity)**: Relative humidity in %.
3. **Ws (Wind Speed)**: Wind speed in km/h.
4. **Rain**: Daily rainfall accumulation in mm.
5. **FFMC (Fine Fuel Moisture Code)**: Rating of the moisture content of litter and other fine fuels.
6. **DMC (Duff Moisture Code)**: Rating of the average moisture content of loosely compacted organic layers.
7. **ISI (Initial Spread Index)**: Numerical rating of the relative rate of fire spread.
8. **Classes**: Fire occurrence (0 = No Fire, 1 = Fire).
9. **Region**: Geographic region (0 = Bejaia, 1 = Sidi-Bel Abbes).

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript (Particle system & animations)
- **ML Framework**: Scikit-learn, NumPy, Pandas
- **Development**: Python 3.9+

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Fire-Weather-Index-main
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
   Open your browser and navigate to `http://127.0.0.1:5001`.

## 📂 Project Structure

```text
├── application.py      # Main Flask application entry point
├── models/             # Contains trained model (linear.pkl) and scaler (scaler.pkl)
├── templates/          # HTML templates (Home & Prediction pages)
├── notebook/           # Jupyter notebooks for EDA and model training
├── requirements.txt    # List of required Python packages
└── README.md           # Project documentation
```

---
*Created with ❤️ for Forest Fire Prevention and Machine Learning Research.*
