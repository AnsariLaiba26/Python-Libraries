import pandas as pd
students = {
    "Name": ["Maha", "Aimen", "Mariyam", "Mirha", "Sana"],
    "Age": [20, 21, 19, 22, 20],
    "Department":["Computer Science", "Mathematics", "Artificial Intelligence", "Data Science", "Software Engineering"],
    "GPA": [3.5, 3.8, 3.9, 3.7, 3.6]}
# create a DataFrame
df = pd.DataFrame(students)
print("------DataFrame------\n")
print(df)
print("\n")

#selecting a single column(Series)
series = df["GPA"]
print("------Series------\n")
print(series)
print("\n")

print("Type of DataFrame:", type(df))
print("Type of Series:", type(series))
