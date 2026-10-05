# NumPy Data Analysis Challenge

## Super30 Work & Learn Portal

This project is part of the **Euron Super30 Work & Learn Portal**. The objective of this project is to build strong fundamentals in **NumPy arrays, indexing, filtering, reshaping, mathematical operations, statistical analysis, sorting, and matrix operations**.

The project contains 12 exercises designed to demonstrate how NumPy can be used efficiently for numerical computation and data analysis.

---

## 📌 Project Name

**super30-numpy-task-1**

---

## 🎯 Objective

The main objective of this project is to understand and practice:

* NumPy array creation
* Array indexing
* Array slicing
* Conditional filtering
* Array reshaping
* Mathematical operations
* Statistical calculations
* Sorting
* Finding unique values
* Two-dimensional arrays
* Matrix operations
* Random number generation
* Numerical data analysis

---

## 🛠️ Technologies Used

* **Python 3**
* **NumPy**
* **Git**
* **GitHub**

---

## 📁 Project Structure

```text
super30-numpy-task-1/
│
├── README.md
│
├── array_creation.py
├── student_marks_analysis.py
├── filtering.py
├── reshaping.py
├── two_dimensional_array.py
├── mathematical_operations.py
├── statistical_analysis.py
├── sorting.py
├── unique_values.py
├── matrix_operations.py
├── salary_analysis.py
└── challenge.py
```

> File names can be changed according to the actual files in the repository.

---

# 📚 Problems Covered

## 1. Array Creation

Three NumPy arrays are created:

### Numbers 1–50

```python
np.arange(1, 51)
```

### Even Numbers 2–100

```python
np.arange(2, 101, 2)
```

### Odd Numbers 1–99

```python
np.arange(1, 100, 2)
```

### Concepts Demonstrated

* `np.array()`
* `np.arange()`
* Array creation
* Numerical sequences

---

# 2. Student Marks Analysis

The following student marks are stored in a NumPy array:

```python
marks = np.array([
    78, 85, 92, 67, 88,
    73, 95, 60, 84, 91
])
```

The following calculations are performed:

* Total marks
* Average marks
* Maximum marks
* Minimum marks
* Median marks

### NumPy Functions Used

```python
np.sum()
np.mean()
np.max()
np.min()
np.median()
```

### Example

```python
total = np.sum(marks)
average = np.mean(marks)
maximum = np.max(marks)
minimum = np.min(marks)
median = np.median(marks)
```

This demonstrates how NumPy can perform numerical calculations efficiently on an entire array.

---

# 3. Filtering

The student marks array is filtered using conditions.

The project identifies students who scored:

* Above 90
* Above the average
* Below 70

### Example

```python
above_90 = marks[marks > 90]

above_average = marks[marks > np.mean(marks)]

below_70 = marks[marks < 70]
```

### Concepts Demonstrated

* Boolean conditions
* Boolean indexing
* Array filtering
* Conditional selection

NumPy allows us to select elements from an array without using traditional loops.

---

# 4. Reshaping

Numbers from 1 to 20 are created and reshaped into a **4 × 5 matrix**.

### Original Array

```text
1  2  3  4  5  6  7  8  9  10
11 12 13 14 15 16 17 18 19 20
```

### Reshaped Array

```python
numbers = np.arange(1, 21)

matrix = numbers.reshape(4, 5)
```

The resulting structure contains:

* 4 rows
* 5 columns

### Concept Demonstrated

```python
reshape()
```

Reshaping changes the structure of an array without changing the underlying values.

---

# 5. Two-Dimensional Array

A **3 × 3 NumPy matrix** is created.

Example:

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```

The project demonstrates:

### Row Selection

```python
matrix[0]
```

Returns the first row.

### Column Selection

```python
matrix[:, 1]
```

Returns the second column.

### Individual Element Selection

```python
matrix[1, 2]
```

Returns the element located at:

* Row index: `1`
* Column index: `2`

### Concepts Demonstrated

* 2D arrays
* Row indexing
* Column indexing
* Element indexing
* Slicing

---

# 6. Mathematical Operations

Two NumPy arrays are created:

```python
a = np.array([10, 20, 30, 40, 50])

b = np.array([5, 10, 15, 20, 25])
```

The following operations are performed:

### Addition

```python
a + b
```

### Subtraction

```python
a - b
```

### Multiplication

```python
a * b
```

### Division

```python
a / b
```

NumPy performs these operations element by element.

For example:

```text
10 + 5  = 15
20 + 10 = 30
30 + 15 = 45
```

---

# 7. Statistical Analysis

The project generates **100 random numbers** and performs statistical calculations.

The following values are calculated:

* Mean
* Median
* Standard deviation
* Variance

Example:

```python
random_values = np.random.rand(100)

mean = np.mean(random_values)
median = np.median(random_values)
standard_deviation = np.std(random_values)
variance = np.var(random_values)
```

### NumPy Functions Used

```python
np.mean()
np.median()
np.std()
np.var()
```

### Concepts Demonstrated

* Random number generation
* Mean
* Median
* Standard deviation
* Variance

Because random numbers are generated, the exact output may be different each time the program runs.

---

# 8. Sorting

An unsorted NumPy array is created and sorted in both ascending and descending order.

Example:

```python
numbers = np.array([45, 12, 78, 23, 9, 56])
```

### Ascending Order

```python
ascending = np.sort(numbers)
```

### Descending Order

```python
descending = np.sort(numbers)[::-1]
```

### Concepts Demonstrated

* `np.sort()`
* Array slicing
* Reverse ordering

---

# 9. Unique Values

The following array is used:

```python
numbers = np.array([
    1, 2, 2, 3, 3,
    3, 4, 5, 5, 6
])
```

Unique values are obtained using:

```python
unique_values = np.unique(numbers)
```

### Expected Result

```text
[1 2 3 4 5 6]
```

### Concept Demonstrated

`np.unique()` removes duplicate values and returns the unique elements.

---

# 10. Matrix Operations

Two **3 × 3 matrices** are created.

Example:

```python
matrix_a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix_b = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])
```

The following operations are performed.

### Matrix Addition

```python
matrix_a + matrix_b
```

### Matrix Subtraction

```python
matrix_a - matrix_b
```

### Element-wise Multiplication

```python
matrix_a * matrix_b
```

### Matrix Multiplication

```python
matrix_a @ matrix_b
```

or:

```python
np.matmul(matrix_a, matrix_b)
```

### Important Difference

Element-wise multiplication:

```python
matrix_a * matrix_b
```

multiplies corresponding elements.

Matrix multiplication:

```python
matrix_a @ matrix_b
```

follows the mathematical rules of matrix multiplication.

---

# 11. Salary Analysis

Salary information for **15 employees** is stored in a NumPy array.

Example:

```python
salaries = np.array([
    35000, 42000, 50000, 38000, 62000,
    45000, 55000, 48000, 70000, 39000,
    58000, 46000, 75000, 52000, 41000
])
```

The following analysis is performed:

### Highest Salary

```python
np.max(salaries)
```

### Lowest Salary

```python
np.min(salaries)
```

### Average Salary

```python
np.mean(salaries)
```

### Employees Earning Above Average

```python
above_average = salaries[salaries > np.mean(salaries)]
```

### Concepts Demonstrated

* Numerical analysis
* Aggregation
* Conditional filtering
* Statistical calculations

---

# 12. Challenge – Random Integer Matrix

A **5 × 5 random integer matrix** is generated using NumPy.

Example:

```python
matrix = np.random.randint(1, 101, size=(5, 5))
```

The project determines:

* Maximum value
* Minimum value
* Row-wise sum
* Column-wise sum
* Overall average

### Maximum

```python
np.max(matrix)
```

### Minimum

```python
np.min(matrix)
```

### Row-wise Sum

```python
np.sum(matrix, axis=1)
```

### Column-wise Sum

```python
np.sum(matrix, axis=0)
```

### Overall Average

```python
np.mean(matrix)
```

### Understanding `axis`

For a 2D array:

```python
axis=1
```

calculates across columns for each row and produces **row-wise results**.

```python
axis=0
```

calculates down the rows for each column and produces **column-wise results**.

---

# 📊 NumPy Functions Used

| Function              | Purpose                         |
| --------------------- | ------------------------------- |
| `np.array()`          | Creates a NumPy array           |
| `np.arange()`         | Creates a sequence of numbers   |
| `np.sum()`            | Calculates total                |
| `np.mean()`           | Calculates average              |
| `np.max()`            | Finds maximum                   |
| `np.min()`            | Finds minimum                   |
| `np.median()`         | Calculates median               |
| `np.std()`            | Calculates standard deviation   |
| `np.var()`            | Calculates variance             |
| `np.sort()`           | Sorts an array                  |
| `np.unique()`         | Finds unique values             |
| `np.reshape()`        | Changes array shape             |
| `np.random.rand()`    | Generates random decimal values |
| `np.random.randint()` | Generates random integers       |
| `np.matmul()`         | Performs matrix multiplication  |

---

# 🔍 Key NumPy Concepts Learned

## 1. Array

A NumPy array is a data structure used to store numerical data efficiently.

Example:

```python
arr = np.array([10, 20, 30, 40])
```

## 2. Indexing

Array elements can be accessed using their index.

```python
arr[0]
```

Python uses zero-based indexing, so the first element has index `0`.

## 3. Slicing

A portion of an array can be selected using slicing.

```python
arr[1:4]
```

## 4. Boolean Filtering

Conditions can be used to filter values.

```python
arr[arr > 20]
```

## 5. Reshaping

An array can be converted into a different shape.

```python
arr.reshape(2, 2)
```

## 6. Vectorized Operations

NumPy allows calculations to be performed directly on arrays.

```python
a + b
```

instead of manually processing every element using a loop.

---

# 🚀 How to Run the Project

## Step 1: Install Python

Make sure Python 3 is installed.

Check the version:

```bash
python --version
```

or:

```bash
py --version
```

---

## Step 2: Install NumPy

Install NumPy using:

```bash
pip install numpy
```

If you are using a specific Python version:

```bash
python -m pip install numpy
```

---

## Step 3: Clone the Repository

```bash
git clone <your-github-repository-url>
```

Navigate into the project:

```bash
cd super30-numpy-task-1
```

---

## Step 4: Run the Programs

For example:

```bash
python array_creation.py
```

You can execute each Python file separately.

---

# 📂 Repository Structure

The repository is organized so that each problem can be easily understood and executed independently.

```text
super30-numpy-task-1
│
├── README.md
│
├── array_creation.py
├── student_marks_analysis.py
├── filtering.py
├── reshaping.py
├── two_dimensional_array.py
├── mathematical_operations.py
├── statistical_analysis.py
├── sorting.py
├── unique_values.py
├── matrix_operations.py
├── salary_analysis.py
└── challenge.py
```

---

# 🎥 YouTube Demonstration

The YouTube video demonstrates the major concepts covered in this project.

The video explains:

* NumPy array creation
* Array indexing
* Filtering
* Reshaping
* Mathematical operations
* Statistical operations
* Sorting
* Unique values
* Matrix operations
* Random number generation
* Salary analysis

The programs are executed during the demonstration and the outputs are explained rather than simply reading the code.

**YouTube Video:**
`<Add YouTube video link here>`

---

# 🔗 GitHub Repository

**Repository Name:**

`super30-numpy-task-1`

**GitHub Repository:**

`<Add GitHub repository link here>`

---

# 🎓 Learning Outcome

After completing this project, I gained practical understanding of how NumPy can be used for numerical data processing.

The project helped me understand:

* How to create and manipulate NumPy arrays
* How to access elements using indexing
* How to filter data using conditions
* How to reshape arrays
* How to perform vectorized mathematical operations
* How to calculate statistical values
* How to sort numerical data
* How to identify unique values
* How to work with two-dimensional arrays
* How to perform matrix operations
* How to analyze real-world-style numerical data

---

# ✅ Conclusion

This project provided hands-on practice with the fundamental features of **NumPy**. By completing the 12 exercises, I developed a stronger foundation in array manipulation, numerical calculations, filtering, statistics, and matrix operations.

These concepts form an important foundation for further learning in:

* Data Analysis
* Data Science
* Machine Learning
* Data Engineering
* Artificial Intelligence

---



Euron Super30 – Work & Learn Portal

**Project:** NumPy Data Analysis Challenge
