- number : 1234, 456, 3.14 , 3 + 4j, 0b111, decimal, fraction
- string : 'spam' , "bob", b'z\x01c'
- list : [1, [2,'three'], 4.5], list(range(10))
- tuple :(1, 'spam' , 4 , 'U'), tuple('spam'), namedtuple
- dictionary : {'food',:spam }, dict(hours = 10)
- set : set('abc'), {'a','b','c'}
file
- Boolean : true and false
- none : none
- functions, modules, classes
advance decorators, generators, iterators



### Python Inner Working:

1. **Source Code:**
   - Python starts with your source code, which is written in human-readable form. This code is usually stored in a file with a `.py` extension.

2. **Lexical Analysis (Tokenization):**
   - The first step is lexical analysis, where Python breaks down your source code into a sequence of tokens. Tokens are the smallest units of the language, like keywords, identifiers, and operators.

   ```python
   # Example Code
   def greet(name):
       print("Hello, " + name)
   ```

3. **Abstract Syntax Tree (AST):**
   - Python then generates an Abstract Syntax Tree (AST) from the tokens. The AST represents the grammatical structure of your code.

   

4. **Bytecode Compilation:**
   - The AST is then translated into bytecode. Bytecode is a low-level representation of your code that is not machine-specific and can be executed by the Python Virtual Machine (PVM).

   ```python
   # Bytecode Example (simplified)
   1   LOAD_CONST   0 (None)
   2   LOAD_FAST    0 (name)
   3   BUILD_STRING 2
   4   PRINT_ITEM
   5   PRINT_NEWLINE
   6   LOAD_CONST   0 (None)
   7   RETURN_VALUE
   ```

5. **Python Virtual Machine (PVM):**
   - The PVM is responsible for executing the bytecode. It is an interpreter that reads and executes the bytecode instruction by instruction.

6. **Dynamic Typing:**
   - Python is dynamically typed, meaning the type of a variable is interpreted at runtime. This allows for more flexibility but may lead to certain runtime errors.

   ```python
   x = 5
   x = "Hello"
   ```

7. **Memory Management:**
   - Python manages memory automatically through a process called garbage collection. When objects are no longer referenced, the memory they occupy is reclaimed.

   ```python
   # Example with garbage collection
   def create_objects():
       a = [1, 2, 3]
       b = a  # Both a and b refer to the same list
   ```

8. **C Extension Modules:**
   - Python can use C extension modules for performance-critical tasks. These modules allow Python to interface with C libraries, providing a bridge between the high-level Python code and low-level system functionality.

   ```python
   # Using a C extension module
   import math
   result = math.sqrt(25)
   ```

9. **Global Interpreter Lock (GIL):**
   - Python has a Global Interpreter Lock (GIL) that ensures only one thread executes Python bytecode at a time. While this simplifies memory management, it can impact the performance of multi-threaded programs.

   ```python
   # Example of GIL impact
   def count_up():
       global counter
       for _ in range(1000000):
           counter += 1
   ```



### Python in the Shell:

- **Interactive Shell (REPL):**
  - The Python shell allows for interactive programming. You can execute code line by line and see immediate results.
  - Access the Python shell by typing `python` or `python3` in the terminal.

  ```python
  # Example in the Python shell
  >>> print("Hello, Python!")
  Hello, Python!
  ```

### Immutable and Mutable Objects in Python:

- **Immutable Objects:**
  - Immutable objects cannot be modified after creation.
  - Example: int

  ```python
  x = 5
  y = x  # y references the same value as x
  x = 10  # x is reassigned to a new value
  print(y)  # Output: 5 (y still references the original value)
  ```

- **Mutable Objects:**
  - Mutable objects can be modified after creation.
  - Example: list

  ```python
  list1 = [1, 2, 3]
  list2 = list1  # Both list1 and list2 reference the same list
  list1.append(4)  # Modifying the list
  print(list2)  # Output: [1, 2, 3, 4] (both lists are modified)
  ```

### Python Data Types - Big Picture:

- **Numeric Types:**
  - int, float, complex
  - Example:

    ```python
    x = 5
    y = 2.5
    z = complex(3, 2)
    ```

- **Sequence Types:**
  - str, list, tuple
  - Example:

    ```python
    text = "Hello, Python!"
    numbers = [1, 2, 3]
    coordinates = (4, 5)
    ```

- **Set Types:**
  - set, frozenset
  - Example:

    ```python
    set1 = {1, 2, 3}
    frozenset1 = frozenset([4, 5, 6])
    ```

- **Mapping Type:**
  - dict
  - Example:

    ```python
    user = {"name": "John", "age": 25}
    ```

- **Boolean Type:**
  - bool
  - Example:

    ```python
    is_python_fun = True
    ```

- **None Type:**
  - NoneType
  - Example:

    ```python
    result = None
    ```

### Internal Working of Python:

- **Copy:**
  - Shallow copy creates a new object but does not create copies of nested objects.
  - Deep copy creates a new object and recursively creates copies of nested objects.

  ```python
  import copy

  list1 = [1, [2, 3], 4]
  shallow_copy = copy.copy(list1)
  deep_copy = copy.deepcopy(list1)
  ```

- **Reference Counts:**
  - Python uses reference counting to manage memory.
  - The `sys.getrefcount()` function can be used to get the reference count of an object.

  ```python
  import sys

  x = [1, 2, 3]
  ref_count = sys.getrefcount(x)
  ```

- **Slicing:**
  - Slicing allows you to access a portion of a sequence.

  ```python
  numbers = [0, 1, 2, 3, 4, 5]
  sliced_numbers = numbers[2:5]
  ```

- **Numbers in Depth:**
  - Python supports integers (`int`), floating-point numbers (`float`), and complex numbers (`complex`).
  - Numeric operations include addition, subtraction, multiplication, division, and more.

  ```python
  a = 5
  b = 2.5
  c = complex(3, 2)
  result = a + b * c
  ```



### Integers (`int`):

#### Integer Representation:
- Integers in Python have arbitrary precision, meaning they can be as large as the available memory allows.
- Python automatically switches between regular integers and long integers as needed.

#### Example:
```python
x = 1234567890123456789012345678901234567890
```

#### Operations:
```python
a = 10
b = 3
result_add = a + b  # 13
result_sub = a - b  # 7
result_mul = a * b  # 30
result_div = a / b  # 3.3333333333333335
result_floor_div = a // b  # 3
result_mod = a % b  # 1
result_exp = a ** b  # 1000
```

### Floating-Point Numbers (`float`):

#### Floating-Point Representation:
- Floating-point numbers in Python follow the IEEE 754 standard.
- Python uses 64 bits to represent a float.

#### Example:
```python
y = 3.141592653589793
```

#### Operations:
```python
c = 2.5
d = 1.2
result_add_float = c + d  # 3.7
result_div_float = c / d  # 2.0833333333333335
```

#### Floating-Point Precision Issues:
- Due to the binary nature of computers, certain decimal fractions cannot be precisely represented.

```python
decimal_fraction = 1.1 + 2.2  # Result may not be exactly 3.3
```

### Complex Numbers (`complex`):

#### Complex Number Representation:
- Complex numbers have both a real and an imaginary part.

#### Example:
```python
z = complex(2, 3)
```

#### Operations:
```python
complex1 = complex(2, 3)
complex2 = complex(1, 2)
result_add_complex = complex1 + complex2  # (3+5j)
result_mul_complex = complex1 * complex2  # (-4+7j)
```

#### Accessing Real and Imaginary Parts:
```python
real_part = complex1.real  # 2.0
imag_part = complex1.imag  # 3.0
```

### Numeric Type Conversion:

#### Conversion Functions:
- Python provides functions to convert between different numeric types.

```python
num_str = "10"
num_int = int(num_str)
num_float = float(num_str)
num_complex = complex(num_str, 5)
```

### Mathematical Functions (Using `math` module):

#### Example:
```python
import math

square_root = math.sqrt(25)  # 5.0
sine_value = math.sin(math.radians(30))  # 0.49999999999999994
logarithm_base_10 = math.log10(100)  # 2.0
```

### Numeric Comparisons:

#### Comparison Operators:
- Python supports various comparison operators for numeric types.

```python
a = 10
b = 5
is_greater = a > b  # True
is_equal = a == b  # False
```

### Important Considerations:

#### Floating-Point Precision:

- Be cautious of precision issues in floating-point arithmetic. Use the `decimal` module for more precise decimal arithmetic.

```python
from decimal import Decimal

decimal_fraction = Decimal('1.1') + Decimal('2.2')  # Decimal('3.3')
```

#### Complex Number Attributes:

- Access the real and imaginary parts of complex numbers using `.real` and `.imag`.

```python
complex_num = complex(2, 3)
real_part = complex_num.real  # 2.0
imag_part = complex_num.imag  # 3.0
```

Certainly! Let's break it down in simpler terms:

### `repr()`

- **What it does:**
  - `repr()` is like a secret code for objects. It gives a detailed and exact description of an object that a computer could understand.
- **Example:**
  ```python
  x = 10
  print(repr(x))  # Output: '10'
  ```
- **Use case:**
  - When you want a detailed and unambiguous description of an object, like for debugging.

### `str()`

- **What it does:**
  - `str()` is like explaining something to a friend. It gives a simpler, human-friendly version of an object.
- **Example:**
  ```python
  y = 3.14
  print(str(y))  # Output: '3.14'
  ```
- **Use case:**
  - When you want to create a message or output that's easy for people to read.

### `print()`

- **What it does:**
  - `print()` is like showing something on the screen. It takes one or more things and displays them for you to see.
- **Example:**
  ```python
  name = "John"
  print("Hello, " + name)  # Output: Hello, John
  ```
- **Use case:**
  - Whenever you want to display information or results to the user.

### Bringing it Together:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={repr(self.name)}, age={repr(self.age)})"

    def __str__(self):
        return f"{self.name}, {self.age} years old"

person_obj = Person("Alice", 30)

# Using repr and str explicitly
repr_result = repr(person_obj)
str_result = str(person_obj)

# Using print to display the object
print(person_obj)  # Output: Alice, 30 years old
```

In this example:
- `repr` gives a detailed, computer-friendly description of the object.
- `str` provides a simpler, human-readable version.
- `print` simply shows the object in a way that's easy for you to see.

Think of it like telling a computer exactly what something is (`repr`), explaining it to a friend in a simpler way (`str`), and just showing it on a screen (`print`). Each has its own purpose!


