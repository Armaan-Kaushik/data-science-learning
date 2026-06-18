#Concatenation function
first_name = "Armaan"
last_name = "Kaushik"
full_name = first_name + " " + last_name
print(full_name)

#Uppercase function
name="Armaan"
print(name.upper())

#Lowercase function
name="ARMAAN"
print(name.lower())

#Replace function
s='maine 200 banana khaye'
s=s.replace('200','10').replace('banana','samosa')
print(f'With one line replacing: {s}')

#Find function: Returns index of first occurrence
text="Data Science"
print(text.find("a"))

#Count function: Returns number of occurrence of an element
text = "Data Science"
print(text.count("a"))

#Length function: Returns length of element 
text="Data Science"
print(len(text))

#Startswith function
text = "Python Programming"
print(text.startswith("Python"))

# Endswith function
text = "report.pdf"
print(text.endswith(".pdf"))

#Split Function
sentence = "Apple Mango Banana"
print(sentence.split())

#Join function
fruits = ["Apple", "Mango", "Banana"]
print(" ".join(fruits))

#Strip Function- to remove extra space
name = "   Armaan   "
print(name.strip()) 