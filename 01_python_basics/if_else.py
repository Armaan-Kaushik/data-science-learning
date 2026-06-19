#program that ask user to enter a number.Program should thenn tell if number is even or odd
num=int(input("Enter a number: "))
if(num%2==0):
    print(f'{num} is even number')
else:
    print(f'{num} is odd number')

# to check dish is in which cuisine
indian=["samosa","dal","naan"]
chinese=["egg roll","pot sticker","fried rice"]
italian=["pizza","pasta","risotto"]


dish=input("Enter a dish name: ")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("Not in our menu")

#Exercise
# 1.Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]


# i)Write a program that asks user to enter a city name and it should tell which country the city belongs to
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city=input("Enter the city name: ")
if city in india:
    print("It is an indian city")
elif city in pakistan:
    print("It is an Pakistani city")  
elif city in bangladesh:
    print("It is an Bangladeshi city")
else:
    print("The city does not belong to our country list")


# ii) Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
c1=input("Enter the city 1 name: ").lower() #To convert input into lower case as items in list are in lower case
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

c2=input("Enter the city 2 name: ").lower()
if c1 in india and c2 in india:
    print("Both are Indian cities")
elif c1 in pakistan and c2 in pakistan:
    print("Both are Pakistani cities")
elif c1 in bangladesh and c2 in bangladesh:
    print("Both are Bangladeshi cities")
else:
    print("They don't belong to the same country")



# Exercise: Python If Condition
# 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#     1. Ask user to enter his fasting sugar level
#     2. If it is below 80 to 100 range then print that sugar is low
#     3. If it is above 100 then print that it is high otherwise print that it is normal
sugar=input("Please enter your fasting sugar level:")
sugar=float(sugar)
if sugar<80:
    print("Your sugar is low, go eat some jalebi :)")
elif sugar>100:
    print("Your sugar is high, stop eating all mithais..!")
else:
    print("Your sugar is normal, relax and enjoy your life!")