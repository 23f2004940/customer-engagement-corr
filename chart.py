# chart.py
# Author: 23f2004940@ds.study.iitm.ac.in
# Task: Generate a Seaborn heatmap correlation matrix for customer engagement metrics

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------------------
# 1. Generate synthetic data
# ------------------------------
np.random.seed(42)
n = 200

data = pd.DataFrame({
    "Website_Visits": np.random.normal(500, 120, n),
    "App_Usage": np.random.normal(300, 80, n),
    "Purchases": np.random.normal(50, 15, n),
    "Customer_Service_Interactions": np.random.normal(20, 5, n),
    "Marketing_Engagement": np.random.normal(70, 20, n),
})

# Introduce correlations (simulate realistic patterns)
data["App_Usage"] += 0.5 * data["Website_Visits"] / 10
data["Purchases"] += 0.3 * data["App_Usage"] / 10
data["Marketing_Engagement"] += 0.2 * data["Website_Visits"] / 10

# ------------------------------
# 2. Compute correlation matrix
# ------------------------------
corr = data.corr()

# ------------------------------
# 3. Create heatmap visualization
# ------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 8))  # 512x512 px at dpi=64
ax = sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="RdYlGn",
    center=0,
    square=True,
    cbar_kws={"shrink": .75},
    linewidths=0.5,
)

plt.title("Customer Engagement Correlation Matrix", fontsize=16, pad=20)

# ------------------------------
# 4. Save as PNG with exact size
# ------------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
