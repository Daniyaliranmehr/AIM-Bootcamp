# AIM Academy | Python Calculator | Group Project

Welcome to our collaborative Python Calculator project! The goal of this project is to practice Python functions, Git, GitHub, and collaborative development while building a working calculator together.

Each student is responsible for implementing one specific function. All functions will be integrated into the main application, which will be developed and maintained by the project manager.

## 1. Project Team

**Project Manager:** Daniyal Iran Mehr

The project manager is responsible for:
- Developing and maintaining `src/main.py`.
- Defining the project structure and function interfaces.
- Integrating the functions implemented by students.
Each student is responsible for implementing only their assigned function in `src/functions.py`.

## 2. Project Structure

The project has the following structure:

```text
calculator/
├── README.md
└── src/
    ├── main.py
    └── functions.py
```

### `src/main.py`

This file contains the main application logic. It receives the user's mathematical expression, identifies the operator, calls the corresponding function, and displays the result.

**This file is maintained exclusively by the project manager, Daniyal Iran Mehr. Students must not modify or commit changes to this file.**

### `src/functions.py`

This file contains all mathematical functions implemented by the students.

**Students must make changes only to their own assigned function in this file.** Do not modify other students' functions, imports, comments, or any other part of the file.

## 3. General Rules

Every student must follow these rules:

1. Implement only the function assigned to them in the assignment list below.
2. Use the exact function name and parameter names specified in the assignment.
3. Return the calculated result using `return`. Do not use `print()` inside your function to display the result.
4. Return the specified error message when an exception condition occurs. Do not print the error message.
5. Do not call your function inside `functions.py`. The main application will call it.
6. Do not add an `input()` statement to your function.
7. Do not modify any file other than `src/functions.py`.
8. Do not modify or delete another student's function.
9. Do not change the function signatures, parameter order, or return-value requirements.
10. Follow Conventional Commits for every commit.

### Example

The following functions are already provided as examples in `src/functions.py`:

```python
def add(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2
```

These examples demonstrate the expected coding style.

A function should calculate its result and return it. The main application is responsible for displaying the result.

## 4. Function Assignments

Each student must implement the function assigned to them below. Function names, parameter names, parameter order, and return requirements are part of the project interface and must not be changed.

### Student 1: Maryam Khorsandi

**Function name:** `subtract`

**Parameters:**
- `num1`: a number (`int` or `float`)
- `num2`: a number (`int` or `float`)

**Operation:** Subtract `num2` from `num1`.

**Return value:** The result of `num1 - num2`.

**Example:**

```python
subtract(10, 3)  # Returns 7
subtract(3, 10)  # Returns -7
```

### Student 2: Aliasghar Raeisian

**Function name:** `divide`

**Parameters:**
- `num1`: a number (`int` or `float`)
- `num2`: a number (`int` or `float`)

**Operation:** Divide `num1` by `num2`.

**Exception:** If `num2` is zero, return the string `Error! Denominator cannot be zero.`

**Return value:** The division result or the specified error string.

**Example:**

```python
divide(10, 2)  # Returns 5.0
divide(10, 0)  # Returns "Error! Denominator cannot be zero."
```

### Student 3: Fateme Allah Bakhshi

**Function name:** `power`

**Parameters:**
- `base`: a number (`int` or `float`)
- `exponent`: a number (`int` or `float`)

**Operation:** Raise `base` to the power of `exponent`.

**Exception:** If `base` is zero and `exponent` is negative, return `Error! Zero cannot be raised to a negative power.`

**Return value:** The calculated power or the specified error string.

**Example:**

```python
power(2, 3)   # Returns 8
power(5, 2)   # Returns 25
power(0, -1)  # Returns "Error! Zero cannot be raised to a negative power."
```

### Student 4: Hanieh Khoddami

**Function name:** `modulo`

**Parameters:**
- `num1`: a number (`int` or `float`)
- `num2`: a number (`int` or `float`)

**Operation:** Calculate the remainder when `num1` is divided by `num2`.

**Exception:** If `num2` is zero, return `Error! Denominator cannot be zero.`

**Return value:** The remainder or the specified error string.

**Example:**

```python
modulo(10, 3)  # Returns 1
modulo(12, 5)  # Returns 2
modulo(10, 0)  # Returns "Error! Denominator cannot be zero."
```

### Student 5: Parham Hayati

**Function name:** `floor_divide`

**Parameters:**
- `num1`: a number (`int` or `float`)
- `num2`: a number (`int` or `float`)

**Operation:** Perform floor division of `num1` by `num2`.

**Exception:** If `num2` is zero, return `Error! Denominator cannot be zero.`

**Return value:** The floor-division result or the specified error string.

**Example:**

```python
floor_divide(10, 3)   # Returns 3
floor_divide(10, 2)   # Returns 5
floor_divide(10, 0)   # Returns "Error! Denominator cannot be zero."
```

### Student 6: Yeganeh Safari

**Function name:** `square_root`

**Parameters:**
- `num`: a number (`int` or `float`)

**Operation:** Calculate the square root of `num`.

**Exception:** If `num` is negative, return `Error! Cannot calculate the square root of a negative number.`

**Return value:** The square root or the specified error string.

**Example:**

```python
square_root(25)   # Returns 5.0
square_root(2)    # Returns approximately 1.41421356237
square_root(-4)   # Returns "Error! Cannot calculate the square root of a negative number."
```

### Student 7: Armita Jafari

**Function name:** `percentage`

**Parameters:**
- `num`: a number (`int` or `float`)
- `percent`: a number (`int` or `float`)

**Operation:** Calculate the specified percentage of a number.

**Return value:** The result of `num * percent / 100`.

**Example:**

```python
percentage(200, 10)  # Returns 20.0
percentage(80, 25)   # Returns 20.0
percentage(150, 50)  # Returns 75.0
```

### Student 8: Aysal Ahmadi

**Function name:** `average`

**Parameters:**
- `*args`: any number of numeric positional arguments

**Operation:** Calculate the arithmetic mean of all provided numbers.

**Exception:** If no numbers are provided, return `Error! At least one number is required.`

**Return value:** The arithmetic mean or the specified error string.

**Example:**

```python
average(10, 20)       # Returns 15.0
average(1, 2, 3, 4)   # Returns 2.5
average(5)            # Returns 5.0
average()             # Returns "Error! At least one number is required."
```

### Student 9: Hanane Ahmadizade

**Function name:** `factorial`

**Parameters:**
- `num`: a non-negative integer

**Operation:** Calculate the factorial of `num`.

**Exception:** If `num` is negative or is not an integer, return `Error! Factorial requires a non-negative integer.`

**Return value:** The factorial or the specified error string.

**Example:**

```python
factorial(0)    # Returns 1
factorial(5)    # Returns 120
factorial(7)    # Returns 5040
factorial(-3)   # Returns "Error! Factorial requires a non-negative integer."
factorial(2.5)  # Returns "Error! Factorial requires a non-negative integer."
```

### Student 10: Seyed Hamed Peighambardoust

**Function name:** `logarithm`

**Parameters:**
- `base`: a number (`int` or `float`)
- `num`: a number (`int` or `float`)

**Operation:** Calculate the logarithm of `num` with the specified `base`.

**Exceptions:**
- If `base` is less than or equal to zero, or `base` equals one, return `Error! Base must be positive and cannot be 1.`
- If `num` is less than or equal to zero, return `Error! Number must be positive.`

**Return value:** The logarithm or the applicable error string.

**Example:**

```python
logarithm(2, 8)    # Returns 3.0
logarithm(10, 100) # Returns 2.0
logarithm(1, 10)   # Returns "Error! Base must be positive and cannot be 1."
logarithm(2, 0)    # Returns "Error! Number must be positive."
```

### Student 11: Alireza Ghalyaei

**Function name:** `absolute`

**Parameters:**
- `num`: a number (`int` or `float`)

**Operation:** Calculate the absolute value of `num`.

**Return value:** The absolute value.

**Example:**

```python
absolute(-10)  # Returns 10
absolute(5)    # Returns 5
absolute(0)    # Returns 0
```

### Student 12: Mona Mohamadi

**Function name:** `maximum`

**Parameters:**
- `num1`: a number (`int` or `float`)
- `num2`: a number (`int` or `float`)

**Operation:** Find the greater of the two numbers.

**Return value:** The larger number. If both numbers are equal, return that number.

**Example:**

```python
maximum(10, 5)  # Returns 10
maximum(3, 8)   # Returns 8
maximum(4, 4)   # Returns 4
```

### Student 13: Negin Taji

**Function name:** `minimum`

**Parameters:**
- `num1`: a number (`int` or `float`)
- `num2`: a number (`int` or `float`)

**Operation:** Find the smaller of the two numbers.

**Return value:** The smaller number. If both numbers are equal, return that number.

**Example:**

```python
minimum(10, 5)  # Returns 5
minimum(3, 8)   # Returns 3
minimum(4, 4)   # Returns 4
```

### Student 14: Fateme Khodabakhshi

**Function name:** `sine`

**Parameters:**
- `angle`: a number (`int` or `float`) representing an angle in radians

**Operation:** Calculate the sine of `angle`.

**Return value:** The sine of the angle as a number.

**Example:**

```python
sine(0)         # Returns 0.0
sine(1.5707963267948966)  # Returns approximately 1.0
```

**Important:** The angle must be expressed in radians, not degrees.

### Student 15: Madihe Khorzani

**Function name:** `cosine`

**Parameters:**
- `angle`: a number (`int` or `float`) representing an angle in radians

**Operation:** Calculate the cosine of `angle`.

**Return value:** The cosine of the angle as a number.

**Example:**

```python
cosine(0)         # Returns 1.0
cosine(1.5707963267948966)  # Returns approximately 0.0
```

**Important:** The angle must be expressed in radians, not degrees.

## 5. Important Rules for Function Implementation

### Function signatures

Use the exact function signature assigned to you. For example:

```python
def divide(num1, num2):
    ...
```

Do not rename `divide`, change `num1` or `num2`, or change the order of the parameters.

The main application will call these functions using their agreed names and parameters.

### Return values and error handling

Functions must return their results instead of printing them.

When an assignment specifies an error message, return that exact string, including capitalization and punctuation.

For example:

```python
def divide(num1, num2):
    if num2 == 0:
        return "Error! Denominator cannot be zero."

    return num1 / num2
```

Do not replace the required error string with a different message.

### Imports

If your function requires a standard-library module, such as `math`, coordinate with the project manager before adding imports. Do not modify the import section or other parts of `functions.py` without permission.

### Testing

You may test your function locally by calling it with different arguments. However, remove all testing calls, `input()` statements, and unnecessary `print()` statements before committing your changes.

Only your assigned function should be added or modified in `src/functions.py`.

## 6. Git and GitHub Workflow

Follow these steps when contributing to the project.

### Step 1: Clone the repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/Daniyaliranmehr/AIM-Bootcamp-Calculator
```

### Step 2: Create a branch

Create a separate branch for your work. Use a descriptive name:

```bash
git switch -c feat/your-function-name
```

For example:

```bash
git switch -c feat/divide
```

### Step 3: Implement your function

Open `src/functions.py` and implement only your assigned function.

Do not modify `src/main.py` or any other student's function.

### Step 4: Review your changes

Before committing, check which files and lines you have changed:

```bash
git status
git diff
```

Make sure your changes are limited to your assigned function in `src/functions.py`.

### Step 5: Commit using Conventional Commits

Every commit must follow the Conventional Commits format:

```text
<type>(<scope>): <description>
```

For this project, use the `feat` type when implementing your function.

Examples:

```text
feat(divide): implement division function
feat(square-root): implement square root function
feat(logarithm): implement logarithm function
```

Commit your changes:

```bash
git add src/functions.py
git commit -m "feat(divide): implement division function"
```

Do not use vague commit messages such as `update`, `changes`, `my code`, or `done`.

### Step 6: Push your branch

```bash
git push -u origin feat/divide
```

Replace the branch name with your own branch name.

### Step 7: Open a Pull Request

Open a Pull Request on GitHub from your branch to the project's target branch.

In the Pull Request description:
- Mention your assigned function.
- Briefly explain what you implemented.
- Confirm that you tested the function.
- Confirm that you changed only your assigned function in `src/functions.py`.

The project manager will review your contribution before it is merged.

## 7. Conventional Commits

Conventional Commits provide a consistent way to describe changes in Git history.

The general format is:

```text
<type>(<scope>): <description>
```

Examples:

| Type | Purpose | Example |
|---|---|---|
| `feat` | Introduce a new feature | `feat(divide): implement division function` |
| `fix` | Fix a bug | `fix(divide): handle zero denominator` |
| `docs` | Update documentation | `docs(readme): clarify contribution rules` |
| `refactor` | Improve code structure without changing behavior | `refactor(average): simplify calculation` |
| `test` | Add or update tests | `test(square-root): cover negative inputs` |

For the initial implementation of your assigned function, use `feat`.

## 8. Contribution Checklist

Before opening a Pull Request, verify the following:

1.  I implemented only my assigned function.
2. I used the exact function name and parameter names.
3. I returned the result instead of printing it.
4. I handled all required exceptions.
5. I used the exact required error messages.
6. I removed testing calls and unnecessary code.
7. I did not modify `src/main.py`.
8. I did not modify another student's function.
9. I followed Conventional Commits.
10. I tested my function with normal and edge-case inputs.
11. I opened a Pull Request for review.

## 9. Final Notes

This project is a collaborative effort. Each function is a small but important part of the final calculator.

The main application will be written and maintained by Daniyal Iran Mehr. Students should focus on implementing their assigned functions according to the agreed interfaces and project rules.

If you have questions about your assignment, function parameters, expected return values, or Git workflow, contact the project manager on the provided Telegram group for your class before making changes outside your assigned function.