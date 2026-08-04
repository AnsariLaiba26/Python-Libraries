import pandas as pd

# create a DataSet with missing values
students = {
    "Student_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Maha", "Aimen", "Mariyam", "Mirha", "Sana", "Hania"],
    "Age": [20, None, 19, 22, None, 21],
    "Department": [
        "Computer Science",
        "Mathematics",
        "Artificial Intelligence",
        "Data Science",
        None,
        "Software Engineering"
    ],
    "CGPA": [3.5, 3.8, None, 3.7, 3.6, None]
}
# create a DataFrame
df = pd.DataFrame(students)
print("========= Original DataFrame =========\n")
print(df)

# checking for missing values
print("\n========= Checking for Missing Values =========\n")
print("Does the Dataset contain any missing values? ")
print(df.isnull().values.any())
print("\nLocation of missing values in the Dataset: ")
print(df.isnull())
print("\nTotal number of missing values in the Dataset: ")
print(df.isnull().sum().sum())
print("\nTotal number of missing values per column in the Dataset: ")
print(df.isnull().sum())
print("\nWhich columns contain missing values? ")
print(df.isnull().any(axis=0))
print("\nWhich rows contain missing values? ")
print(df.isnull().any(axis=1))

# Removing missing values
print("\n========= Removing Missing Values =========\n")
print("Removing rows with any missing values: ")
print(df.dropna(axis=0, how='any'))
print("\nRemoving columns with any missing values: ")
print(df.dropna(axis=1, how='any'))
print("\nRemove rows where age is missing: ")
print(df[df["Age"].notnull()])

# Fill missing values
print("\n========= Filling Missing Values =========\n")
# create a copy of the original DataFrame 
filled_df = df.copy()
filled_df["Age"]= filled_df["Age"].fillna(filled_df["Age"].mean())
filled_df["Department"]= filled_df["Department"].fillna("Unknown")
filled_df["CGPA"]= filled_df["CGPA"].fillna(filled_df["CGPA"].median())
print("========= DataFrame after filling missing values =========\n")
print(filled_df)

# Forward fill and backward fill
print("\n========= Forward Fill (Age Column) =========\n")
print(df["Age"].ffill())
print("\n========= Backward Fill (Age Column) =========\n")
print(df["Age"].bfill())

# Interpolate missing values
print("\n========= Interpolating Missing Values (Age Column) =========\n")
print(df["Age"].interpolate())

# Result after Cleaning the DataFrame
print("\n========= Result after Cleaning the DataFrame =========")
print("\nDoes the cleaned DataFrame contain any missing values? ")D
print(filled_df.isnull().values.any())
