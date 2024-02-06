

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


