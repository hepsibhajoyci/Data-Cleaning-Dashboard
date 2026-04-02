import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# STEP 1: CREATE MESSY DATASET
# -----------------------------
data = {
    "Name": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Age": [25, np.nan, 30, 22, 200, 28, None, 35],
    "Salary": [50000, 60000, None, 45000, 1000000, 52000, 48000, None],
    "Join_Date": ["2020-01-01", "not available", "2021/03/15", None,
                  "2019-07-10", "2022-12-01", "wrong", "2020-05-20"]
}

df = pd.DataFrame(data)

# Save messy dataset
df.to_excel("messy_dataset.xlsx", index=False)

print("✅ Messy dataset created")

# -----------------------------
# STEP 2: HANDLE NULL VALUES
# -----------------------------
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# -----------------------------
# STEP 3: DATA TYPE CONVERSION
# -----------------------------
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")

# -----------------------------
# STEP 4: OUTLIER DETECTION (IQR)
# -----------------------------
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

median_salary = df["Salary"].median()

df["Salary"] = np.where(
    (df["Salary"] < lower) | (df["Salary"] > upper),
    median_salary,
    df["Salary"]
)

# -----------------------------
# STEP 5: SAVE CLEANED DATA
# -----------------------------
df.to_excel("cleaned_dataset.xlsx", index=False)

print("✅ Cleaned dataset saved")

# -----------------------------
# STEP 6: DASHBOARD
# -----------------------------
plt.style.use("dark_background")

plt.figure(figsize=(12, 8))

# 1. Age Histogram
plt.subplot(2, 2, 1)
plt.hist(df["Age"], bins=5)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")

# 2. Salary Histogram
plt.subplot(2, 2, 2)
plt.hist(df["Salary"], bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Count")

# 3. Salary Boxplot (Outliers)
plt.subplot(2, 2, 3)
plt.boxplot(df["Salary"])
plt.title("Salary Outliers")

# 4. Age Trend
plt.subplot(2, 2, 4)
plt.plot(df["Age"], marker='o')
plt.title("Age Trend")
plt.xlabel("Index")
plt.ylabel("Age")

plt.tight_layout()

# Save dashboard image
plt.savefig("data_cleaning_dashboard.png")

# Show dashboard
plt.show()

print("✅ Dashboard created successfully")