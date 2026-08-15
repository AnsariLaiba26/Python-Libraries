import pandas as pd

# ============================================================
# 1. MERGING DATASETS
# ============================================================

employees = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha"]
})

scores = pd.DataFrame({
    "ID": [2, 3, 4, 5],
    "Score": [85, 90, 95, 88]
})

# Inner Merge (Keeps only IDs present in both DataFrames)
inner_merge = pd.merge(employees, scores, on="ID", how="inner")
print("INNER MERGE")
print(inner_merge)

# Left Merge (Keeps all rows from the left DataFrame)
left_merge = pd.merge(employees, scores, on="ID", how="left")
print("\nLEFT MERGE")
print(left_merge)

# Right Merge (Keeps all rows from the right DataFrame)
right_merge = pd.merge(employees, scores, on="ID", how="right")
print("\nRIGHT MERGE")
print(right_merge)

# Outer Merge (Keeps all IDs from both DataFrames)
outer_merge = pd.merge(employees, scores, on="ID", how="outer")
print("\nOUTER MERGE")
print(outer_merge)

# ============================================================
# 2. JOINING DATASETS
# ============================================================

employee_data = pd.DataFrame({
    "Department": ["IT", "HR", "Finance"],
    "Salary": [70000, 65000, 80000]
}, index=[1, 2, 3])

employee_names = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed"]
}, index=[1, 2, 3])

# Join using the index
joined_data = employee_names.join(employee_data)
print("\nJOIN")
print(joined_data)

# ============================================================
# 3. CONCATENATING DATASETS
# ============================================================

sales_january = pd.DataFrame({
    "Product": ["Laptop", "Mouse"],
    "Sales": [10, 25]
})

sales_february = pd.DataFrame({
    "Product": ["Keyboard", "Monitor"],
    "Sales": [15, 8]
})

# axis=0 → combine rows
sales_rows = pd.concat([sales_january, sales_february], axis=0, ignore_index=True)
print("\nCONCATENATE ROWS")
print(sales_rows)

# Concatenating columns
prices = pd.DataFrame({
    "Price": [900, 25, 50, 200]
})

sales_with_prices = pd.concat([sales_rows, prices], axis=1)
print("\nCONCATENATE COLUMNS")
print(sales_with_prices)

# ============================================================
# 4. TIME SERIES DATA
# ============================================================

dates = pd.date_range(
    start="2026-01-01",
    periods=60,
    freq="D"
)

sales = pd.DataFrame({
    "Date": dates,
    "Sales": range(100, 160)
})

# Convert Date column to datetime
sales["Date"] = pd.to_datetime(sales["Date"])

# Extract useful time information
sales["Month"] = sales["Date"].dt.month
sales["Month_Name"] = sales["Date"].dt.month_name()
sales["Day"] = sales["Date"].dt.day
sales["Day_Name"] = sales["Date"].dt.day_name()

print("\nTIME SERIES DATA")
print(sales.head())

# Grouping sales by month
monthly_sales = sales.groupby("Month")["Sales"].agg(["mean", "sum", "max", "min"])
print("\nMONTHLY SALES SUMMARY")
print(monthly_sales)

# ============================================================
# 5. MELT
# ============================================================

student_scores = pd.DataFrame({
    "Student": ["Ali", "Sara", "Ahmed"],
    "Math": [85, 90, 78],
    "Python": [88, 95, 82],
    "Statistics": [80, 92, 85]
})

# Convert wide format into long format
melted_scores = pd.melt(
    student_scores,
    id_vars=["Student"],
    var_name="Subject",
    value_name="Score"
)
print("\nMELTED DATA")
print(melted_scores)

# ============================================================
# 6. STACK
# ============================================================

stacked_scores = student_scores.set_index("Student").stack()
print("\nSTACKED DATA")
print(stacked_scores)

# ============================================================
# 7. UNSTACK
# ============================================================

unstacked_scores = stacked_scores.unstack()
print("\nUNSTACKED DATA")
print(unstacked_scores)

# ============================================================
# 8. PIVOT
# ============================================================

pivot_data = pd.DataFrame({
    "Student": ["Ali", "Ali", "Sara", "Sara"],
    "Subject": ["Math", "Python", "Math", "Python"],
    "Score": [85, 88, 90, 95]
})

pivot_result = pivot_data.pivot(
    index="Student",
    columns="Subject",
    values="Score"
)

print("\nPIVOT")
print(pivot_result)

# ============================================================
# 9. PIVOT TABLE
# ============================================================

sales_data = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
    "Employee": ["Ali", "Ahmed", "Sara", "Ayesha", "Usman", "Noor"],
    "Salary": [70000, 80000, 65000, 72000, 90000, 85000]
})

pivot_table_result = pd.pivot_table(
    sales_data,
    values="Salary",
    index="Department",
    aggfunc=["mean", "sum", "max"]
)

print("\nPIVOT TABLE")
print(pivot_table_result)