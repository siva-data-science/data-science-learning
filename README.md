# Day 1 – Python Basics

 my Day 1 practice programs from my Data Science learning journey.

## Topics Learned
- Python introduction
- Variables
- Arithmetic operations
- User input
- Conditional statements (if-else)

## Programs
1. hello.py – Print a welcome message
2. addition.py – Add two numbers
3. square_number.py – Find square of a number
4. average_marks.py – Calculate average marks
5. student_marks.py – Check pass or fail
# 🚀 Day 2 – Python for Data Science

Welcome to **Day 2 of my Data Science with AI learning journey**.

Today I practiced important Python concepts used in **data analysis and machine learning**.

---

## 📚 Topics Covered

* ✅ If Statements
* ✅ If–Else Conditions
* ✅ Multiple Conditions (elif)
* ✅ For Loops
* ✅ Looping Through Lists
* ✅ Basic Data Processing

---

## 🧠 What I Learned

Today I learned how Python programs make **decisions** using conditions and how to **repeat tasks** using loops.

These concepts are important because in **Data Science** we often need to:

* Process large datasets
* Iterate through data
* Apply conditions to filter information

---

## 💻 Practice Tasks

### 1️⃣ Even or Odd Number

```python
num = 10

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

---

### 2️⃣ Print Numbers Using Loop

```python
for i in range(1,11):
    print(i)
```

---

### 3️⃣ Calculate Total Marks

```python
marks = [70,85,90,60,75]

total = 0
for m in marks:
    total = total + m

print("Total Marks:", total)
```

---

### 4️⃣ Find Maximum Number

```python
numbers = [4,7,2,9,5]

print(max(numbers))
```

---

## 🎯 Key Takeaways

* Learned how **conditions control program flow**
* Used **loops to process list data**
* Practiced **basic data calculations**
* Strengthened Python fundamentals for **data science**

---

## 📅 Next Step

➡️ **Day 3:**

* Python Functions
* Dictionaries
* First Mini Data Analysis Project

---


# 📅 Day 5 – Python Lists & Basic Data Analysis

## ⏰ Training Plan (3 Hours)

| Time   | Task                       |
| ------ | -------------------------- |
| 1 Hour | Understand list operations |
| 1 Hour | Practice loops with lists  |
| 1 Hour | Mini data analysis project |

---

# 🧠 Concept 1 — Working with Lists

A **list** stores multiple values in a single variable.

```python
marks = [70, 80, 90, 60, 85]
print(marks)
```

### Output

```
[70, 80, 90, 60, 85]
```

---

# 🧠 Access List Elements

List elements are accessed using **index numbers**.

```python
marks = [70, 80, 90, 60]

print(marks[0])
print(marks[2])
```

### Output

```
70
90
```

⚡ **Note:** Python list indexing starts from **0**.

---

# 🧠 Concept 2 — Loop Through a List

We can use a **for loop** to iterate through list elements.

```python
marks = [70, 80, 90]

for m in marks:
    print(m)
```

### Output

```
70
80
90
```

📊 This technique is widely used in **data analysis**.

---

# 🧠 Concept 3 — Calculate Total Marks

```python
marks = [70, 80, 90, 60]

total = 0

for m in marks:
    total = total + m

print("Total:", total)
```

### Output

```
Total: 300
```

---

# 🧠 Concept 4 — Find Average

Average Formula:

```
Average = Total / Number of values
```

### Example

```python
marks = [70, 80, 90, 60]

total = sum(marks)

average = total / len(marks)

print("Average:", average)
```

### Output

```
Average: 75
```

---

# 💻 Practice Programs

## Program 1 — Find Maximum Marks

```python
marks = [65, 80, 92, 75]

print("Highest marks:", max(marks))
```

### Output

```
Highest marks: 92
```

---

## Program 2 — Count Students

```python
marks = [65, 80, 92, 75]

print("Total students:", len(marks))
```

### Output

```
Total students: 4
```

---

# 🧠 Mini Project — Student Marks Analysis

This is your **first small data analysis task**.

```python
marks = [75, 82, 90, 60, 88]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
```

### Output

```
Total: 395
Average: 79
Highest: 90
Lowest: 60
```

📊 These are **basic statistics operations used in data science**.

---

# 🎯 Day 5 Goals

By the end of today you should know:

✔ Loop through lists
✔ Calculate total
✔ Calculate average
✔ Find highest and lowest values

These are **core data analysis concepts** used in real datasets.

---


## Tools Used
- Python
- Anaconda
- Jupyter Notebook

## Learning Goal
I am learning Python as the first step toward becoming a **Data Scientist with AI**.

## Author
Siva Kumar
