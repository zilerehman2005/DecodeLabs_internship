# Project 2 — Data Classification Using AI
**DecodeLabs Industrial Training Kit | Batch 2026**

## 📌 Overview
This project moves from the rule-based logic of Project 1 into **Supervised
Learning**. The goal is to build, train, and validate a basic classification
model that learns patterns from historical data (rather than hand-written
`if/then` rules) and uses them to categorize new, unseen data.

**Dataset used:** Iris flower dataset (built into scikit-learn — no download
needed)
- 150 samples, 3 classes (*Setosa*, *Versicolor*, *Virginica*), 4 features
  (sepal length, sepal width, petal length, petal width)

**Algorithm used:** K-Nearest Neighbors (KNN)

## 🎯 Key Requirements Covered
- [x] Load and understand a dataset
- [x] Split data into training and testing sets
- [x] Scale features (`StandardScaler`)
- [x] Apply a simple classification algorithm (KNN)
- [x] Tune the model (choosing the best K via an error-rate curve)
- [x] Evaluate with a confusion matrix, precision/recall, and F1 score

## 🗂️ Files
| File | Description |
|---|---|
| `Project2_Data_Classification_Iris.ipynb` | Full Colab-ready notebook with all code, plots, and explanations |
| `README.md` | This file |

## ▶️ How to Run in Google Colab
1. Go to [colab.research.google.com](https://colab.research.google.com).
2. Click **File → Upload notebook** and select
   `Project2_Data_Classification_Iris.ipynb`.
3. Click **Runtime → Run all**.
4. No dataset upload or API key is needed — the Iris dataset loads directly
   from `sklearn.datasets`.

All required libraries (`numpy`, `pandas`, `matplotlib`, `seaborn`,
`scikit-learn`) are pre-installed in Colab by default.

## 🧠 Pipeline (IPO Framework)

```
INPUT                       PROCESS                      OUTPUT
─────                       ───────                      ──────
Iris dataset          →     Train/Test Split       →     Confusion Matrix
Feature Scaling        →    KNN Algorithm           →     F1 Score
```

1. **Load & explore** the Iris dataset with pandas, and visualize feature
   relationships with a Seaborn pairplot.
2. **Scale features** with `StandardScaler` (fit on train, transform on
   both train and test — no data leakage).
3. **Split** into training (80%) and testing (20%) sets, stratified by
   class to keep the split balanced.
4. **Tune K** by scanning K = 1 to 30 and plotting the error rate to find
   the "elbow" (optimal K).
5. **Train** the final `KNeighborsClassifier` using the scikit-learn
   `instantiate → fit → predict` workflow.
6. **Validate** using accuracy, a weighted F1 score, a full classification
   report, and a plotted confusion matrix.
7. **Try it yourself** — predict the species of a custom flower
   measurement you enter.

## 📊 Why F1 Score, Not Just Accuracy?
On imbalanced datasets, a model can score high accuracy while still
performing poorly on minority classes (the "accuracy mirage"). The
confusion matrix breaks predictions into **True Positives, False
Positives, False Negatives, and True Negatives**, and the F1 score
balances **precision** (trustworthiness of positive predictions) against
**recall** (how many actual positives were caught) — important in
contexts like medical diagnosis or spam filtering.

## 🔜 Suggested Extensions (Optional, for Deeper Learning)
- Swap in another small dataset (`load_wine()` or `load_breast_cancer()`
  from `sklearn.datasets`) and re-run the same pipeline.
- Compare KNN's performance against Logistic Regression or a Decision Tree
  on the same split.
- Experiment with different `test_size` values or a different scaler
  (`MinMaxScaler`) and observe how results change.

---
*Submitted as part of the DecodeLabs Industrial Training Kit, Batch 2026.*
