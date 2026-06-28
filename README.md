# 🎯 Customer Segmentation Model

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python)
![Domain](https://img.shields.io/badge/Domain-Retail_&%20%20Consumer_Behaviour_Analytics-navy?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

</div>
> Unsupervised Machine Learning | K-Means Clustering | Python · Scikit-learn · Excel

---

## 📌 Project Overview

Applied **K-Means clustering** to segment 200 mall customers based on
Annual Income and Spending Score. The model identified **5 distinct segments**
with clear behavioural patterns and actionable marketing recommendations.

**Dataset:** Mall Customer Segmentation Data (Kaggle)  
**Techniques:** EDA · Feature Scaling · K-Means · Elbow Method  
**Tools:** Python · Scikit-learn · Pandas · Matplotlib · Seaborn · OpenPyXL  

---

## 📊 The 5 Segments

| Segment | Count | Avg Income | Avg Spending | Strategy |
|---|---|---|---|---|
| 🏆 Premium Customers | 39 | $86.5k | 82.1 | Retain & Upsell |
| ⚡ Impulsive Spenders | 22 | $25.7k | 79.4 | Flash Sales |
| 🔵 Standard Customers | 81 | $55.3k | 49.5 | Loyalty Programme |
| 💰 Cautious Savers | 35 | $88.2k | 17.4 | Build Trust |
| 🟣 Budget Customers | 23 | $26.3k | 20.9 | Value Offers |

---

## 📁 Project Structure

```
├── data/
│ ├── Mall_Customers.csv ← Original Kaggle dataset
│ └── customers_segmented.csv ← Customers with segment labels
├── scripts/
│ ├── eda.py ← Exploratory data analysis
│ ├── kmeans.py ← K-Means model + visualisations
│ └── excel_report.py ← Excel workbook builder
├── outputs/
│ ├── distributions.png
│ ├── income_vs_spending.png
│ ├── elbow_curve.png
│ ├── clusters.png
│ └── Customer_Segmentation_Report.xlsx
└── README.md
```

---

## 🚀 How to Run

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl

# Step 1 — EDA
python scripts/eda.py

# Step 2 — K-Means Model
python scripts/_kmeans.py

# Step 3 — Excel Report
python scripts/excel_report.py
```

---

## 📈 Key Insights

- **Elbow at K=5** confirmed visually and mathematically
- **Premium Customers** are only 19.5% of base but highest value
- **Cautious Savers** have high income but low spend — biggest untapped opportunity
- **Standard Customers** at 40.5% are the volume base — loyalty programmes key

---

## 👤 Author

### **Arun** 

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=flat-square&logo=github)](https://github.com/arunofficial25)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/arunofficial25)

---

<div align="center">
<i>Not every customer wants the same thing — the ones who figure that out first, win.</i>
</div>