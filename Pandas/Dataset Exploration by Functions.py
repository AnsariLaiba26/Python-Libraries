import pandas as pt

# employee dataset
employees = {
    "Employee ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Ali","Sara","Ahmed","Maha","Ayesha","Hamza","Fatima","Usman"],
    "Department": ["IT","HR","Finance","Data Science","Marketing","IT","Data Science","Finance"],
    "Experience": [2, 5, 3, 1, 4, 6, 2, 7],
    "Salary": [55000, 72000, 68000, 50000, 75000, 81000, 60000, 85000]
}

# create a DataFrame
df = pt.DataFrame(employees)
print("-----DataFrame-----")
print(df)

# explore the dataset
print("\n=====Exploring the Dataset=====")

print("=> First 5 Rows")
print(df.head())
print("\n=> Last 3 Rows")
print(df.tail(3))
print("\n=> Shape of the DataFrame")
print(df.shape)
print("\n=> Column Names")
print(df.columns)
print("\n=> Data Types of Each Column")
print(df.dtypes)
print("\n=> Information About the DataFrame")
print(df.info())
print("\n=> Summary Statistics of the DataFrame")
print(df.describe())

# sorting the dataset
print("\n=> Sort by Salary in Descending Order")
print(df.sort_values(by="Salary", ascending=False))

# Query
print("\n=> Employees with salary greater than 60000")
print(df.query("Salary > 60000"))

# unique values
print("\n=> Unique Departments")
print(df["Department"].unique())
print("\n=> Count of Unique Departments")
print(df["Department"].nunique())

# groupby
print("\n=> Average Salary by Department")
print(df.groupby("Department")["Salary"].mean())
