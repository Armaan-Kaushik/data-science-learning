#examples of single error handling

try:
    x=int(input("Enter num1:"))
    y=int(input("Enter num2:"))
    z=x/y
except ZeroDivisionError:
    print("Cannot divide by zero")
    z=None
print("Value after Division is:",z)

#Example of Multiple Exception Handling    
try:
    x = int(input("Enter number1: "))
    y = int(input("Enter number2: "))

    z = x / y
    print("Result:", z)

except ZeroDivisionError:
    print("Division by zero occurred.")

except ValueError:
    print("Please enter valid integers.")
# except Exception as e:
#     print("Exception type:",type(e).__name__)
#     z=None     #Used to find the name of exception (here=ValueError is exceptn name )

#TRY-EXCEPT-ELSE Block
try:
    x=int(input("Enter number_1: "))
    y=int(input("Enter number_2: "))
    z=x/y
except ZeroDivisionError:
    print("Can't divide by Zero")
except ValueError:
    print("Enter a valid number")
else:
    print("Division is successfull")
    print("Result is:",z)

#TRY-EXCEPT-ELSE-FINALLY Block
try:
    x=int(input("Enter number_1: "))
    y=int(input("Enter number_2: "))
    z=x/y
except ZeroDivisionError:
    print("Can't divide by Zero")
except ValueError:
    print("Enter a valid number")
else:
    print("Division is successfull")
    print("Result is:",z)
finally:
    print("Thank you for using the calculator.")

#Raise an exception 
try:
    age=int(input("Enter age: "))
    if age<0:
        raise ValueError("Age can't be negative") 
except ValueError as e:
    print("Error Occurred:",e)
else:
    print("Age Excepted")


#Custom Exception
class NegativeSalaryError(Exception):
    pass
try:
    sal=int(input("Enter the salary:- "))
    if sal<0:
        raise NegativeSalaryError("Salary can't be negative")
except NegativeSalaryError as e:
    print("Error occurred:",e)
else:
    print("Salary Accepted")


"""
===========================
CUSTOM EXCEPTIONS IN PYTHON
===========================

1. What is a Custom Exception?
------------------------------
A custom exception is a user-defined exception created when the built-in
exceptions (ValueError, TypeError, etc.) are not specific enough for our
application.

-------------------------------------------------

2. Why use Custom Exceptions?
-----------------------------
- Makes code more readable.
- Gives meaningful error names.
- Helps identify the exact problem.

Example:
    NegativeSalaryError
    InvalidStudentIDError
    InsufficientBalanceError

-------------------------------------------------

3. How to Create a Custom Exception
-----------------------------------

Syntax:

class MyException(Exception):
    pass

Explanation:
- Exception is the parent class.
- 'pass' means no additional functionality.

-------------------------------------------------

4. Raising a Custom Exception
-----------------------------

Syntax:

raise MyException("Error Message")

Example:

if salary < 0:
    raise NegativeSalaryError("Salary can't be negative")

The 'raise' keyword manually throws an exception.

-------------------------------------------------

5. Handling a Custom Exception
------------------------------

Syntax:

try:
    ...
except MyException as e:
    print(e)

-------------------------------------------------

6. Program Flow
---------------

try
 │
 ├── Valid Data
 │      │
 │      ▼
 │    else
 │
 └── Invalid Data
        │
        ▼
raise Custom Exception
        │
        ▼
except

-------------------------------------------------

7. Difference Between ValueError and Custom Exception
-----------------------------------------------------

ValueError:
------------
Used for general invalid values.

Example:
raise ValueError("Invalid Marks")

Custom Exception:
-----------------
Used for application-specific errors.

Example:
raise NegativeSalaryError("Salary can't be negative")

-------------------------------------------------

8. Quick Revision
-----------------

class MyException(Exception):
    pass

raise MyException("Message")

except MyException as e:
    print(e)

-------------------------------------------------

Key Points
----------

✓ Inherit from Exception to create a custom exception.
✓ Use raise to generate the exception.
✓ Handle it using except.
✓ Mostly used in large applications.
✓ Rarely required in Data Science but good to know.

"""