# 📘 The Machine Learning Landscape – Summary Notes

## 1️⃣ What is Machine Learning?
Machine Learning (ML) is the field of computer science that enables systems to **learn from data** instead of being explicitly programmed.
The goal is to discover patterns and make predictions or decisions automatically.

---

## 2️⃣ Types of Learning

### 🟢 **Supervised Learning**
- The model learns from **labeled data** (each input has a known correct output).
- Goal: predict outputs for new, unseen inputs.
- Examples:  
  - Predicting house prices (Regression)  
  - Classifying emails as spam/not-spam (Classification)

### 🔵 **Unsupervised Learning**
- The data has **no labels**; the model finds structure or patterns on its own.
- Examples:  
  - Customer segmentation using clustering  
  - Dimensionality reduction with PCA

### 🟣 **Semi-Supervised Learning**
- Uses a **small amount of labeled data + large amount of unlabeled data**.
- Common in image or speech datasets where labeling is expensive.

### 🟠 **Self-Supervised Learning**
- A modern form where the model **creates its own labels** from the data.
- Example: Masked-word prediction in BERT — the model predicts missing words from sentences.

### 🔴 **Reinforcement Learning**
- An **agent** learns by interacting with an environment.
- It receives **rewards or penalties** and learns to maximize cumulative reward.
- Used in robotics, gaming, and autonomous driving.

---

## 3️⃣ Instance-Based vs Model-Based Learning

| Type | Description | Example |
|------|--------------|----------|
| **Instance-Based** | Memorizes training examples and compares new data to them (pattern matching). | k-Nearest Neighbors (KNN) |
| **Model-Based** | Learns a general model (equation or rule) that summarizes the data. | Linear Regression, Neural Networks |

---

## 4️⃣ Training, Validation, and Testing

- **Training Set:** Used to teach the model (fit parameters).  
- **Validation Set:** Used for **tuning hyperparameters** and preventing overfitting.  
- **Test Set:** Used **once at the end** to evaluate final performance on unseen data.  

💡 *Never tune the model using the test set; that leaks information.*

---

## 5️⃣ Overfitting vs Underfitting

| Concept | Description | Result |
|----------|--------------|--------|
| **Underfitting** | Model is too simple; cannot capture patterns in data. | High error on both train & test data |
| **Overfitting** | Model is too complex; memorizes training data. | Very low training error, high test error |
| **Goal** | Find the “sweet spot” where the model generalizes well. | Balanced error |

---

## 6️⃣ Model Parameters vs Hyperparameters

| Type | Who Sets It | Example |
|------|--------------|---------|
| **Parameters** | Learned by the model during training. | Weights and biases in regression or neural nets |
| **Hyperparameters** | Set by you before training; control learning process. | Learning rate, tree depth, number of neighbors |

---

## 7️⃣ Data Quality Issues

- **Unrepresentative Data:** Training data doesn’t reflect real-world conditions → poor generalization.  
- **Biased Data:** Historical or sampling bias leads to unfair predictions.  
- **Noisy Data:** Random errors or irrelevant features confuse the model.  
- **Data Leakage:** Information from test set accidentally used during training → unrealistically good performance.

---

## 8️⃣ Model Evaluation Metrics (Quick Overview)
- **Regression:** Mean Squared Error (MSE), RMSE, R²  
- **Classification:** Accuracy, Precision, Recall, F1-Score, ROC-AUC  

---

## 9️⃣ The ML Workflow (High-Level)
1. Define the problem & collect data  
2. Explore & clean the data  
3. Split into training/validation/test sets  
4. Choose a model  
5. Train the model (fit parameters)  
6. Evaluate using validation data  
7. Tune hyperparameters  
8. Test on unseen data  
9. Deploy and monitor in production  

---

## 🧭 Key Intuition Summary
- **Learning = minimizing error** between predicted and actual outputs.  
- **Line or curve** = the model’s learned relationship between input & output.  
- **More flexible ≠ better** — the right balance gives good generalization.  
- **PolynomialFeatures** help when relationships are curved, not straight.  

---

