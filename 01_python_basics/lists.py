items=["bread","pasta","fruits","veggies"]
print(items)

# # To access the element at certain index or a range of elements
# print(items[0])
# print(items[1])
# print(items[0:4:2])
# print(items[-1])

# # Modify the element in list
# items[1]="chips"
# print(items)

# Add a new element to the list
a=items.append("butter")
print(items)

# Remove an element from the list 
items.remove("butter")
print(items)

# Insert an item to a given index
items.insert(1,"butter")
print(items)

# Joining two lists
foods=["bread","pasta","fruits","veggies"]
bath=["shampoo","soap"]
items=foods+bath
print(items)

# Length of the list
print(len(items))

# To check element in list
print("bread" in items)
print("coke" in items)



#Exercise Questions
# You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))  #1
heros.append("black panther")#2
print(heros) 
heros.remove("black panther") #3
print(heros) 
print(heros.insert(3,"black panther"))
heros[1:3]=['doctor strange'] #4
print(heros)
heros.sort() #5
print(heros)


#2# Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#   3. March - 2600
#   4. April - 2130
#   5. May - 2190
# Create a list to store these monthly expenses and using that find out,

exp = [2200,2350,2600,2130,2190]
# 1. In Feb, how many dollars you spent extra compare to January?
spd_extra=exp[1]-exp[0]
print(f'The extra amt spend in feb as compared to jan is : {spd_extra} $')

# 2. Find out your total expense in first quarter (first three months) of the year
print(f'total expense in first quarter (first three months) of the year is: {exp[0]+exp[1]+exp[2]} $')

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month? ", 2000 in exp)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print(exp)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3]=exp[3]-200
print(f'Expenses after 200$ return in April: {exp}')