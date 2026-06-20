# text="Ice-cream"
# print(text)
# print(text[1])
# print(text[0:3])
# print(text[4:9])
# print(text[:3])
# print(text[0:3:2])

# a="let's learn python"
# print(a)

# address='''1 Purple street
# new york
# usa'''
# print(address)


# s1="Hello"
# s2="World"
# print(s1+' '+s2)

# s="Total number oof states in India:"
# num=25
# print(s+num) #Error as string and numbers cant be added so convert number into string using str function 

# s="Total number oof states in India:"
# num=25
# print(s+str(num))

# #Exercise questions 
# # 1.Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
# street=input("Enter street Name:")
# city=input("Enter Cityy Name:")
# country=input("Enter Country Name:")
# add= street +'\n'+ city+'\n' + country
# print("Address using + operator: ",add)
# add=f'{street}\n{city}\n{country}\n'
# print("Address using f' operator:",add)


# # 2.Create a variable to store the string "Earth revolves around the sun"
# #  a.Print "revolves" using slice operator
# #  b.Print "sun" using negative index
# str="Earth revolves around the sun"
# print(str[6:14])
# print(str[-3:])

# # 3. Create two variables to store how many fruits and vegetables you eat in a day.
# # Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
# # Use python f string for this.
# fruits=int(input("Enter number of fruits eaten in one day:"))
# Veggiess=int(input("Enter number of Vegetables eaten in one day:"))
# print(f'I eat {Veggiess} veggies and {fruits} fruits daily')

# 4. I have a string variable called s='maine 200 banana khaye'. This of course is a
# wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.

s='maine 200 banana khaye'
s=s.replace('200','10')
s=s.replace('banana','samosa')
print(f'With two line replacing: {s}')

s='maine 200 banana khaye'
s=s.replace('200','10').replace('banana','samosa')
print(f'With one line replacing: {s}')


