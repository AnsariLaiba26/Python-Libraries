import pandas as pd

# Create a Dataset
employees = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha", "Hassan", "Fatima", "Usman", "Noor"],
    "Department": ["IT","HR","Finance","Marketing","IT","Sales","Finance","HR"],
    "Salary": [ 65000, 72000, 68000, 850000, 70000, 69000, 71000, 34000],
    "Experience": [2, 4, 3, 15, 5, 2, 4, 20]
}

# Creating the DataFrame
df = pd.DataFrame(employees)
print("=========ORIGINAL DATASET=========")
print(df)

# Detecting Outliers using Range Method
df["Range"] = df["Salary"].apply(lambda salary: "Outlier" if salary < 65000 or salary > 80000 else "Normal")

# Detecting Outliers using Z-Score 
df["Z-Score"] = (df["Salary"] - df["Salary"].mean()) / df["Salary"].std()
df["Z-Score"] = df["Z-Score"].apply(lambda value: "Outlier" if value < -2 or value > 2 else "Normal")

# Detecting Outliers using IQR Method
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
df["IQR"] = df["Salary"].apply(lambda salary: "Outlier" if salary < lower_limit or salary > upper_limit else "Normal")

# Detecting Anomalies using Isolation Forest
from sklearn.ensemble import IsolationForest as IS
model = IS(contamination="auto", random_state=42)
df["Isolation_Forest"] = model.fit_predict(df[["Salary"]])
df["Isolation_Forest"] = df["Isolation_Forest"].replace({1: "Normal", -1: "Anomaly"})

# Displaying the final DataFrame with outlier detection results
print("\n=========DATASET WITH OUTLIER AND ANOMALY DETECTION=========")
print(df[["Name", "Salary", "Range", "Z-Score", "IQR", "Isolation_Forest"]])

### Handling Outliers

# Removing Outliers 
cleaned_df = df.query("Salary >= 65000 and Salary <= 80000")
print("\n=========DATASET AFTER REMOVING OUTLIERS=========")
print(cleaned_df)

# Correcting Outliers 
df["corrected_salary"] = df["Salary"].apply(lambda salary: min(salary, 80000))
print("\n=========DATASET AFTER CORRECTING OUTLIERS=========")
print(df[["Name", "Salary", "corrected_salary"]])