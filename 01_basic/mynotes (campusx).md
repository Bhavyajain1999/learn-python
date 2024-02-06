

---

**Session 1: Python Basics**

**1. DSMP (Data Science and Machine Learning Program)**

DSMP (Data Science and Machine Learning Program) is a comprehensive program designed to provide individuals with a deep understanding of data science and machine learning concepts. It covers a wide range of topics, including data analysis, machine learning algorithms, and practical applications, all taught using the Python programming language.

**2. About Python**

Python is a versatile, high-level programming language known for its readability and simplicity. It supports various programming paradigms, including procedural, object-oriented, and functional programming.

**3. Python Output/Print Function**

The `print()` function in Python is used to display output. For example:

```python
print("Hello, Python!")  # Output: Hello, Python!
```

This code uses the `print()` function to display the string "Hello, Python!" on the console.

**4. Python Data Types**

Python has several data types, including:

- **Integers (`int`):** Whole numbers without a fractional component.
  ```python
  age = 25
  ```

- **Floats (`float`):** Numbers with a decimal point.
  ```python
  height = 5.8
  ```

- **Strings (`str`):** Ordered sequences of characters.
  ```python
  greeting = "Hello, Python!"
  ```

- **Booleans (`bool`):** Represents either True or False.
  ```python
  is_python_fun = True
  ```

**5. Python Variables**

Variables are used to store and manage data. In Python, there's no need to explicitly declare the variable type; Python dynamically assigns it.

```python
x = 5
y = "Hello"
```

Here, `x` is assigned the integer value `5`, and `y` is assigned the string value `"Hello"`.

**6. Python Comments**

Comments provide explanations within the code and are not executed. Single-line comments start with `#`, and multi-line comments use triple quotes (`'''` or `"""`).

```python
# This is a single-line comment
  
"""
This is a
multi-line comment
"""
```

**7. Python Keywords and Identifiers**

Keywords are reserved words with special meanings in Python, while identifiers are names given to entities like variables or functions. Identifiers must follow certain rules.

```python
# Keywords
if_example = True
else_example = False

# Identifiers
user_name = "John"
```

Here, `if` and `else` are keywords, and `user_name` is an identifier.

**8. Python User Input**

The `input()` function is used to take user input. By default, the input is treated as a string.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
```

This code prompts the user to enter their name and age, converting the age input to an integer using `int()`.

**9. Python Type Conversion**

Conversion functions like `int()`, `float()`, and `str()` are used to convert between data types.

```python
num_str = "10"
num_int = int(num_str)
```

This code converts the string `"10"` to an integer using `int()`.

**10. Python Literals**

Literals are constants representing fixed values in Python. Examples include numeric literals (`10`, `3.14`), string literals (`'hello'`, `"world"`), and boolean literals (`True`, `False`).

---

Session 2

- Arithmetic operators
-> + ,- , * ,/ ,// (integer divison) (5//2 = 2) basically for getting quotient

- Relational operators
-> >, <, = , >= , <=, != , ==

- Logical operators
-> And, or , !

- Bitwise operators
-> & (and) ,  | (OR)

Membership operators in Python are used to test whether a value is a member of a sequence (like a string, list, or tuple). There are two membership operators: `in` and `not in`.

### `in` Operator:

The `in` operator checks if a value exists in a sequence. The basic syntax is:

```python
element in sequence
```

Here's an example:

```python
fruits = ["apple", "banana", "orange"]

# Check if "banana" is in the list
if "banana" in fruits:
    print("Yes, 'banana' is in the list.")
else:
    print("No, 'banana' is not in the list.")
```

Output:
```
Yes, 'banana' is in the list.
```

### `not in` Operator:

The `not in` operator checks if a value does not exist in a sequence. The basic syntax is:

```python
element not in sequence
```

Example:

```python
fruits = ["apple", "banana", "orange"]

# Check if "grape" is not in the list
if "grape" not in fruits:
    print("Yes, 'grape' is not in the list.")
else:
    print("No, 'grape' is in the list.")
```

Output:
```
Yes, 'grape' is not in the list.
```

These operators are handy when you need to check whether a specific element is present or absent in a sequence. They work well with strings, lists, tuples, and other iterable data types in Python.

Certainly! In Python, `if`, `else`, and loops are control flow statements that allow you to execute different blocks of code based on certain conditions or repeatedly execute a block of code. Let me explain each of them in detail with examples.

### `if` Statement:
The `if` statement is used to make decisions in your code based on a condition. If the condition is true, the indented code block under the `if` statement is executed.

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

In this example, the `print` statement will be executed because the condition `x > 5` is true.

### `else` Statement:
The `else` statement is used to define a block of code that will be executed if the condition specified in the `if` statement is false.

```python
x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

In this example, since the condition `x > 5` is false, the code block under the `else` statement will be executed.

### `elif` Statement:
The `elif` statement allows you to check for multiple conditions in a series. It comes after an `if` statement and before the `else` statement. If the condition in the `if` statement is false, it checks the condition in the `elif` statement.

```python
x = 7

if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but not greater than 10")
else:
    print("x is 5 or less")
```

In this example, the first condition (`x > 10`) is false, so it moves to the `elif` statement. The condition `x > 5` is true, so the corresponding code block is executed.

### Loops:

#### `for` Loop:
The `for` loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

This loop will iterate over the elements of the `fruits` list and print each fruit.

#### `while` Loop:
The `while` loop is used to repeatedly execute a block of code as long as the specified condition is true.

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

This loop will print numbers from 0 to 4, as long as the `count` is less than 5.

These are the basic concepts of `if`, `else`, `elif`, and loops in Python. They are fundamental for making decisions and performing repetitive tasks in your code.
In Python, a module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py`. Modules allow you to organize your Python code into separate files and reuse code across multiple programs. You can use the `import` statement to include the functionality of a module in your program. Let me provide an example and discuss some modules important for data science.

### Example of Importing a Module:

Let's say you have a module named `my_module.py`:

```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

def square(x):
    return x ** 2
```

You can import and use this module in another Python script:

```python
# main.py
import my_module

print(my_module.greet("Alice"))
print(my_module.square(5))
```

In this example, the `import my_module` statement makes the functions `greet` and `square` from `my_module` available in the `main.py` script.

### Important Modules for Data Science:

1. **NumPy:**
   - NumPy is a powerful library for numerical and mathematical operations in Python.
   - It provides support for large, multi-dimensional arrays and matrices, along with mathematical functions to operate on these elements.
   - Example: `import numpy as np`

2. **Pandas:**
   - Pandas is a library for data manipulation and analysis. It provides data structures like Series and DataFrame for efficient data handling.
   - Example: `import pandas as pd`

3. **Matplotlib:**
   - Matplotlib is a 2D plotting library for creating static, animated, and interactive visualizations in Python.
   - Example: `import matplotlib.pyplot as plt`

4. **Seaborn:**
   - Seaborn is a statistical data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
   - Example: `import seaborn as sns`

5. **Scikit-learn:**
   - Scikit-learn is a machine learning library that provides simple and efficient tools for data mining and data analysis.
   - Example: `from sklearn import dataset`

6. **SciPy:**
   - SciPy is an open-source library for mathematics, science, and engineering. It builds on NumPy and provides additional functionality.
   - Example: `import scipy`

These modules are widely used in the field of data science for tasks such as data manipulation, analysis, visualization, and machine learning. Importing them into your Python scripts or notebooks allows you to leverage their functionality for your data-related tasks.

In addition to the modules mentioned earlier, there are several other commonly used modules in Python that cover a wide range of functionalities. Here are some more essential and commonly used modules:

1. **datetime:**
   - Provides classes for working with dates and times.
   - Example: `import datetime`

2. **os:**
   - Allows interaction with the operating system, providing functions to perform tasks like file and directory manipulation.
   - Example: `import os`

3. **sys:**
   - Provides access to some variables used or maintained by the Python interpreter and functions that interact strongly with the interpreter.
   - Example: `import sys`

4. **random:**
   - Implements pseudo-random number generators for various distributions.
   - Example: `import random`

5. **re:**
   - Provides regular expression matching operations.
   - Example: `import re`

6. **json:**
   - Enables encoding and decoding JSON data.
   - Example: `import json`

7. **requests:**
   - Simplifies sending HTTP requests and handling responses.
   - Example: `import requests`

8. **math:**
   - Offers mathematical functions beyond what is available in the basic arithmetic operations.
   - Example: `import math`

9. **collections:**
   - Provides alternatives to built-in types like dictionaries, lists, and tuples, with additional functionality.
   - Example: `from collections import Counter`

10. **time:**
    - Includes functions for working with time, measuring code execution time, and creating delays.
    - Example: `import time`

11. **csv:**
    - Simplifies reading and writing CSV (Comma Separated Values) files.
    - Example: `import csv`

12. **pickle:**
    - Implements a fundamental, but efficient, binary format for serializing and de-serializing Python objects.
    - Example: `import pickle`

These modules cover a broad spectrum of tasks, including working with dates, interacting with the file system, handling regular expressions, making HTTP requests, performing mathematical operations, and more. Depending on your specific needs and the nature of your projects, you may find these modules helpful in various situations.

