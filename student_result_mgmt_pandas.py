import csv
import pandas as pd
students = [
    {"student_id": "S001", "name": "Ravi", "age": 21, "city": "Hyderabad", "python_marks": 85, "sql_marks": 78, "pandas_marks": 82, "attendance": 92},
    {"student_id": "S002", "name": "Anu", "age": 22, "city": "Chennai", "python_marks": 90, "sql_marks": 88, "pandas_marks": 91, "attendance": 95},
    {"student_id": "S003", "name": "Kiran", "age": 20, "city": "Bangalore", "python_marks": 76, "sql_marks": 81, "pandas_marks": 79, "attendance": 89},
    {"student_id": "S004", "name": "Priya", "age": 21, "city": "Mumbai", "python_marks": 88, "sql_marks": 84, "pandas_marks": 86, "attendance": 94},
    {"student_id": "S005", "name": "Arjun", "age": 23, "city": "Pune", "python_marks": 72, "sql_marks": 75, "pandas_marks": 70, "attendance": 85},
    {"student_id": "S006", "name": "Sneha", "age": 20, "city": "Delhi", "python_marks": 95, "sql_marks": 91, "pandas_marks": 93, "attendance": 97},
    {"student_id": "S007", "name": "Vijay", "age": 22, "city": "Hyderabad", "python_marks": 68, "sql_marks": 74, "pandas_marks": 71, "attendance": 82},
    {"student_id": "S008", "name": "Meena", "age": 21, "city": "Kolkata", "python_marks": 84, "sql_marks": 80, "pandas_marks": 85, "attendance": 91},
    {"student_id": "S009", "name": "Rahul", "age": 24, "city": "Bangalore", "python_marks": 79, "sql_marks": 83, "pandas_marks": 77, "attendance": 88},
    {"student_id": "S010", "name": "Divya", "age": 22, "city": "Chennai", "python_marks": 92, "sql_marks": 89, "pandas_marks": 94, "attendance": 96},
    {"student_id": "S011", "name": "Suresh", "age": 23, "city": "Mumbai", "python_marks": 65, "sql_marks": 70, "pandas_marks": 68, "attendance": 80},
    {"student_id": "S012", "name": "Pooja", "age": 20, "city": "Pune", "python_marks": 87, "sql_marks": 85, "pandas_marks": 89, "attendance": 93},
    {"student_id": "S013", "name": "Amit", "age": 21, "city": "Delhi", "python_marks": 74, "sql_marks": 79, "pandas_marks": 76, "attendance": 86},
    {"student_id": "S014", "name": "Lakshmi", "age": 22, "city": "Hyderabad", "python_marks": 91, "sql_marks": 93, "pandas_marks": 90, "attendance": 98},
    {"student_id": "S015", "name": "Nikhil", "age": 23, "city": "Kolkata", "python_marks": 81, "sql_marks": 77, "pandas_marks": 80, "attendance": 90},
    {"student_id": "S016", "name": "Swathi", "age": 21, "city": "Bangalore", "python_marks": 89, "sql_marks": 86, "pandas_marks": 88, "attendance": 94},
    {"student_id": "S017", "name": "Manoj", "age": 24, "city": "Chennai", "python_marks": 70, "sql_marks": 73, "pandas_marks": 75, "attendance": 84},
    {"student_id": "S018", "name": "Harika", "age": 20, "city": "Hyderabad", "python_marks": 94, "sql_marks": 90, "pandas_marks": 92, "attendance": 97},
    {"student_id": "S019", "name": "Rohit", "age": 22, "city": "Mumbai", "python_marks": 78, "sql_marks": 82, "pandas_marks": 79, "attendance": 87},
    {"student_id": "S020", "name": "Neha", "age": 21, "city": "Pune", "python_marks": 86, "sql_marks": 88, "pandas_marks": 84, "attendance": 92},
    {"student_id": "S021", "name": "Varun", "age": 23, "city": "Delhi", "python_marks": 73, "sql_marks": 69, "pandas_marks": 72, "attendance": 81},
    {"student_id": "S022", "name": "Kavya", "age": 20, "city": "Kolkata", "python_marks": 90, "sql_marks": 92, "pandas_marks": 91, "attendance": 96},
    {"student_id": "S023", "name": "Ajay", "age": 22, "city": "Bangalore", "python_marks": 82, "sql_marks": 79, "pandas_marks": 83, "attendance": 89},
    {"student_id": "S024", "name": "Deepika", "age": 21, "city": "Chennai", "python_marks": 96, "sql_marks": 94, "pandas_marks": 95, "attendance": 99},
    {"student_id": "S025", "name": "Mohan", "age": 23, "city": "Hyderabad", "python_marks": 77, "sql_marks": 80, "pandas_marks": 78, "attendance": 86}
]

with open("students.csv" ,"w" ,newline="") as file:
    writer=csv.DictWriter(file,fieldnames=students[0].keys())
    writer.writeheader()
    writer.writerows(students)
print("CSV file created successfully")


#read_csv
df=pd.read_csv("students.csv")
print(df)

#head
print(df.head())

#tail
print(df.tail())

#shape
print(df.shape)

#columns
print(df.columns)

#datatypes
print(df.dtypes)

#info
print(df.info())

#describe
print(df.describe())

#avg_python_marks
avg_python=df["python_marks"].mean()
avg_sql=df["sql_marks"].mean()
avg_pandas=df["pandas_marks"].mean()
print(f"Average python_marks:{avg_python:.2f}")
print(f"Average sql_marks:{avg_sql:.2f}")
print(f"Average pandas_marks:{avg_pandas:.2f}")

#max,min_marks

max=df[["pandas_marks","python_marks","sql_marks"]].max().max()
min=df[["pandas_marks","python_marks","sql_marks"]].min().min()
print(f"Max marks:{max}")
print(f"Min marks:{min}")

#sort students 
print(df.sort_values("python_marks")["name"])
print(df.sort_values("python_marks")["attendance"])


#Filter students having Python marks greater than 80.
print(df[df["python_marks"]>80]["name"])

#Filter students having attendance greater than 75.
print(df[df["attendance"]>75]["name"])

#Select only name, python_marks, and pandas_marks.
print(df[["name" , "python_marks" , "pandas_marks"]])

#Add a new column called total_marks.
df["total_marks"]=df[["python_marks" , "sql_marks" , "pandas_marks"]].sum(axis=1)
print(df)

#Add another column called average_marks.
df["avg_marks"]=df[["python_marks" , "sql_marks" , "pandas_marks"]].mean(axis=1)
df["avg_marks"]=df["avg_marks"].round(2)
print(df)

#Save the processed dataset into
df.to_csv("student_results.csv", index=False)
print("CSV created successfully")


