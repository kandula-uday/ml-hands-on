# 🏡 Toronto Housing Price Prediction (GTA Real Estate)

This project demonstrates a complete end-to-end Machine Learning pipeline to predict house prices in the Greater Toronto Area using real-world housing data. The goal is to build and continuously improve a price prediction model based on minimal but meaningful property features.

---

## 📁 Dataset Overview

The raw dataset was gathered from multiple region-specific real estate listings and contains:

- `address`: Full address of the property
- `price`: Listing price in CAD (**target variable**)
- `details`: Raw text containing:
  - Bedrooms
  - Bathrooms
  - Category (e.g., House, Condo, Townhouse)
- `city`: City/region where the property is located

---

## 🧠 Key Steps in ML Pipeline

### ✅ 1. Feature Extraction
- Parsed the `details` column to extract:
  - `bedrooms`
  - `bathrooms`
  - `category` (property type: House, Condo, Townhouse)
- Extracted `city` from address
- Cleaned and structured messy or missing entries

### ✅ 2. Data Preprocessing
- Dropped entries with invalid prices
- Imputed missing values using:
  - Median for numeric fields (`bedrooms`, `bathrooms`)
  - Most frequent value for categorical fields
- One-Hot Encoding for categorical columns
- Standard Scaling for numeric columns
- Used **`ColumnTransformer`** and **`Pipeline`** for reproducible transformation

### ✅ 3. Exploratory Data Analysis (EDA)
- Visualized price distribution per category
- Plotted scatter charts (price vs. bedrooms)
- Correlation heatmaps to detect feature relationships
- Identified potential outliers (not removed yet)

### ✅ 4. Model Training
- Used **Linear Regression** as a baseline model
- Dataset split using stratified sampling
- Train/Test: 80/20 split
- Evaluation Results:
  - ✅ **RMSE**: ~737,000 CAD
  - ✅ **MAE**: ~503,000 CAD
  - ✅ **R² Score**: ~0.44

---

## 📊 Planned Improvements (v1.1+)

- ✅ Add geolocation features (longitude/latitude)
- ❌ Outlier detection and removal
- ✅ Include `area_sqft` if derivable from raw data
- 🔁 Cross-validation for more robust results
- ⚙️ Try other models: RandomForest, XGBoost, LightGBM
- 🔍 Hyperparameter tuning with `GridSearchCV`
- 📁 Model serialization with `joblib` or `pickle`

---

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **IDE**: VS Code, Jupyter Notebook
- **Data format**: CSVs + `.npy` files (numpy)
- **Platform**: MacOS + Anaconda (can run on Google Colab)

---

## 💻 How to Run This Project

### Option 1: Run Locally
```bash
git clone 
cd house-ml-pipeline
jupyter notebook
