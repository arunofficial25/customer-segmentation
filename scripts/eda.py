import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/Mall_Customers.csv")

# Basic exploration
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDescriptive Statistics:")
print(df.describe())

# Plot distributions
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Feature Distributions", fontsize=14, fontweight="bold")

axes[0].hist(df["Age"], bins=20, color="#1B3A6B", edgecolor="white")
axes[0].set_title("Age Distribution")
axes[0].set_xlabel("Age")

axes[1].hist(df["Annual Income (k$)"], bins=20, color="#0D6E6E", edgecolor="white")
axes[1].set_title("Annual Income Distribution")
axes[1].set_xlabel("Income (k$)")

axes[2].hist(df["Spending Score (1-100)"], bins=20, color="#C9A84C", edgecolor="white")
axes[2].set_title("Spending Score Distribution")
axes[2].set_xlabel("Spending Score")

plt.tight_layout()
plt.savefig("outputs/distributions.png", dpi=150)
plt.show()
print("Plot saved to outputs/")

# Scatter plot: Income vs Spending Score
plt.figure(figsize=(8, 6))
plt.scatter(df["Annual Income (k$)"], df["Spending Score (1-100)"],
            color="#1B3A6B", alpha=0.6, edgecolors="white", s=80)
plt.title("Annual Income vs Spending Score", fontsize=14, fontweight="bold")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.tight_layout()
plt.savefig("outputs/income_vs_spending.png", dpi=150)
plt.show()
print("Scatter plot saved.")