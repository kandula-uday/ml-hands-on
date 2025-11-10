# 🖊️ MNIST Digit Classification Portfolio Project

This project demonstrates digit classification using the MNIST dataset, following best practices from "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow".  
It is designed as a portfolio-quality notebook, showcasing key machine learning concepts and model evaluation techniques.

---

## 📦 Project Overview

- **Goal:** Classify handwritten digits (0–9) from the MNIST dataset.
- **Techniques:** Binary and multiclass classification, precision-recall and ROC curves, model comparison.
- **Models Used:**  
  - `SGDClassifier` (Stochastic Gradient Descent)  
  - `RandomForestClassifier`  
  - `DummyClassifier` (baseline)

---

## 🚀 Workflow

1. **Data Loading & Exploration**
   - Load MNIST using `fetch_openml`.
   - Visualize sample digits.

2. **Binary Classification**
   - Train an `SGDClassifier` to detect the digit "5".
   - Evaluate using accuracy, cross-validation, and confusion matrix.

3. **Precision/Recall & Thresholds**
   - Use decision scores to plot precision-recall curves.
   - Adjust thresholds for desired precision/recall trade-off.
   - Demonstrate use of `argmax` to select optimal points.

4. **ROC Curve Analysis**
   - Plot ROC curve for `SGDClassifier`.
   - Calculate ROC AUC score for model performance.

5. **RandomForest Comparison**
   - Train a `RandomForestClassifier` for the same task.
   - Compare precision-recall curves and F1 scores with `SGDClassifier`.
   - Evaluate ROC AUC for Random Forest.



---

## 📊 Key Concepts Demonstrated

- **Model Training & Evaluation:**  
  Efficient use of scikit-learn for training, cross-validation, and scoring.
- **Precision/Recall Trade-Off:**  
  Visualize and control classifier performance using decision thresholds.
- **ROC Curve & AUC:**  
  Compare models using ROC curves and AUC metrics.
- **Model Comparison:**  
  Direct comparison of linear and ensemble methods.


---

## 🛠️ Technologies Used

- Python 3
- scikit-learn
- matplotlib
- numpy

---

## 📈 Results

- Both `SGDClassifier` and `RandomForestClassifier` are evaluated and compared using robust metrics.
- Visualizations provide clear insights into model strengths and weaknesses.
- All code and explanations follow best practices for reproducibility and clarity.

---

## 💡 Portfolio Value

This notebook is structured for clarity and completeness, making it ideal for showcasing your machine learning skills.  
It covers essential concepts, demonstrates thoughtful model evaluation, and provides professional-quality visualizations and explanations.

---

## 📚 References

- [Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/)
- [scikit-learn documentation](https://scikit-learn.org/stable/)

---