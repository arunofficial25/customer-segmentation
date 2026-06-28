import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load data
df = pd.read_csv("data/Mall_Customers.csv")

# Select features for clustering
X = df[["Annual Income (k$)", "Spending Score (1-100)"]].copy()

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method — test K from 1 to 10
inertia = []
K_range = range(1, 11)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertia.append(km.inertia_)

# Plot the elbow curve
plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia, marker="o", color="#1B3A6B", linewidth=2, markersize=8)
plt.title("Elbow Method — Optimal K", fontsize=14, fontweight="bold")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.xticks(K_range)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("outputs/elbow_curve.png", dpi=150)
plt.show()
print("Elbow curve saved.")

# Run K-Means with optimal K=5
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Check cluster distribution
print("Customers per cluster:")
print(df["Cluster"].value_counts().sort_index())

# Plot the clusters
colors = ["#1B3A6B", "#0D6E6E", "#C9A84C", "#C0392B", "#6C3483"]

plt.figure(figsize=(9, 6))
for i in range(5):
    subset = df[df["Cluster"] == i]
    plt.scatter(subset["Annual Income (k$)"], subset["Spending Score (1-100)"],
                color=colors[i], label=f"Cluster {i}", s=80,
                edgecolors="white", alpha=0.9)

# Plot centroids
centroids = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centroids[:, 0], centroids[:, 1],
            color="black", marker="X", s=200, zorder=5, label="Centroids")

plt.title("Customer Segments — K-Means (K=5)", fontsize=14, fontweight="bold")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/clusters.png", dpi=150)
plt.show()
print("Cluster plot saved.")

# Assign segment names
segment_names = {
    0: "Standard Customers",
    1: "Premium Customers",
    2: "Impulsive Spenders",
    3: "Cautious Savers",
    4: "Budget Customers"
}
df["Segment"] = df["Cluster"].map(segment_names)

# Profile each segment
profile = df.groupby("Segment")[["Age", "Annual Income (k$)", "Spending Score (1-100)"]].mean().round(1)
profile["Count"] = df.groupby("Segment").size()
profile["Share (%)"] = (profile["Count"] / len(df) * 100).round(1)

print("\nSegment Profiles:")
print(profile.sort_values("Annual Income (k$)"))

# Save segmented data
df.to_csv("data/customers_segmented.csv", index=False)
print("\nSegmented data saved to data/customers_segmented.csv")