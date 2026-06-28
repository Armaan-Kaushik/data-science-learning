#Addressbook
book={}
book["tom"]={
    "name":"tom",
    "address":"1 red street,NY",
    "phone":98989898
}

book["bob"]={
    "name":"bob",
    "address":"1 green street,NY",
    "phone":24424234
}


import json
s=json.dumps(book)
print(s)

book=json.loads(s) # loads book as dictionary type
print(book)
print(type(book))

print(book["bob"])
print(book["bob"]["phone"])


for person in book:
    print(book[person])


#Studentbook
students={}
students["Armaan"]={
    "name":"Armaan",
    "age":19,
    "course":"Data Science",
    "marks":98
}

students["Sonia"]={
    "name":"Sonia",
    "age":19,
    "course":"Finance",
    "marks":71
}

students["Adarsh"]={
    "name":"Adarsh",
    "age":18,
    "course":"Maths",
    "marks":81
}

import json
s=json.dumps(students)
print(s)
print(type(s))

stud=json.loads(s)
print(stud)
print(type(stud))

print(students["Sonia"])
print(students["Adarsh"]["course"])

for name, details in students.items():
    print(name)
    print(details)


def topper():
    highest_marks=0
    topper=""
    for student in students:
        marks=students[student]["marks"]
        if marks>highest_marks:
            highest_marks=marks
            topper=student
    print(topper)
    print(highest_marks)
topper()

for student in students:
    print(student)

for k in students:
    print(f'{k} -> {students[k]["marks"]}')


"""
==========================
JSON & Dictionary Notes
==========================

1. JSON (JavaScript Object Notation)
------------------------------------
JSON is a lightweight data-interchange format used to store and exchange data.
It is language-independent and is widely used in APIs, web applications,
configuration files, and Data Science.

Python dictionaries and JSON objects have almost the same structure.

------------------------------------------------------------

2. Dictionary
-------------
A dictionary stores data as key-value pairs.

Syntax:
    dictionary = {
        "key": value
    }

Values are accessed using their keys, not indexes.

Example:
    student["name"]

------------------------------------------------------------

3. Nested Dictionary
--------------------
A dictionary can contain another dictionary as its value.

Example:
    students["Armaan"]["marks"]

This first accesses the dictionary stored under "Armaan",
then retrieves the value associated with the key "marks".

------------------------------------------------------------

4. JSON Module
--------------
Python provides the built-in 'json' module for converting
between Python objects and JSON strings.

Import using:
    import json

------------------------------------------------------------

5. json.dumps()
---------------
Converts a Python object (dictionary, list, etc.)
into a JSON formatted string.

Python Object
      |
      | json.dumps()
      V
JSON String

The returned object is of type 'str'.

------------------------------------------------------------

6. json.loads()
---------------
Converts a JSON formatted string back into a Python object.

JSON String
      |
      | json.loads()
      V
Python Dictionary/List

The returned object can be accessed like any normal dictionary.

------------------------------------------------------------

7. Dictionary Traversal
-----------------------
Iterating over a dictionary using:

    for key in dictionary:

returns only the keys.

To access values:

    dictionary[key]

------------------------------------------------------------

8. items()
----------
The items() method returns both keys and values together.

Syntax:
    for key, value in dictionary.items():

Here,
    key   -> Dictionary key
    value -> Corresponding dictionary value

------------------------------------------------------------

9. keys()
---------
Returns only the keys of the dictionary.

Syntax:
    dictionary.keys()

------------------------------------------------------------

10. values()
------------
Returns only the values of the dictionary.

Syntax:
    dictionary.values()

------------------------------------------------------------

11. Finding Maximum Value
-------------------------
A common programming pattern.

Algorithm:
1. Assume the maximum value is the smallest possible.
2. Traverse through all elements.
3. Compare each value with the current maximum.
4. If larger, update the maximum.
5. Continue until the loop ends.

Example:
Finding the student with the highest marks.

------------------------------------------------------------

12. Dictionary vs List
----------------------

List:
- Ordered collection.
- Access elements using indexes.
- Example:
      fruits[0]

Dictionary:
- Key-value collection.
- Access values using keys.
- Example:
      student["name"]

Dictionaries do not support indexing directly.

------------------------------------------------------------

13. Important Concepts Learned
------------------------------
• Creating dictionaries.
• Creating nested dictionaries.
• Accessing nested values.
• Converting Dictionary → JSON (dumps).
• Converting JSON → Dictionary (loads).
• Looping through dictionaries.
• Using keys(), values(), and items().
• Solving problems using loops and dictionaries.
• Finding maximum values (Topper problem).

------------------------------------------------------------

14. Applications in Data Science
--------------------------------
JSON is extensively used in:
• REST APIs
• Configuration files
• Data exchange between applications
• Web scraping
• Machine Learning projects
• Reading datasets
• Cloud services
• MongoDB databases

Understanding dictionaries and JSON is essential before learning:
    - Requests
    - APIs
    - Pandas
    - NumPy
    - Machine Learning
"""