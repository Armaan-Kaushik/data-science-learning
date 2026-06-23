#1) calculating total using Function
def calc_total(exp): #func argument
    total=0
    for item in exp:
        total+=item
    return total  #return value


tom_exp_list=[2100,3400,3500]
joe_exp_list=[200,500,700]

toms_total=calc_total(tom_exp_list)
joes_total=calc_total(joe_exp_list)

print("Tom's total expense:",toms_total)
print("joe's total expense:",joes_total)

#2) Total of two numbers
def sum(a,b):
    #This function takes 2 args which are integers and it willl return sum of them as an output 
    total=a+b
    return total


n=sum(5,6)
print("Total:",n)

x=sum(b=3,a=2)
print("Total:",x)

#Exercise
# 1)  Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print
# *
# **
# ***
# ****

def print_pattern(n):
    # This is a function which takes integer as a parameter and print the pattern as given above for the input integer
    for i in range(n):
        s=''
        for j in range(i+1):
            s +='*'
        print(s)
        

n=print_pattern(3)
n=print_pattern(4)

# 2) Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is, area = (1/2)*base*height

def calculate_area(b,h):
    #This function takes 2 arguments- base and height which is used to calculate the value of rectangle's area and return it 
    area = (1/2)*b*h
    return area

base=int(input("Enter the base: "))
height=int(input("Enter the height: "))
print("Total area:",calculate_area(base,height))


# 3) Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,rectangle area=length*width

def calculate_area(d1, d2, shape='triangle'):
    #This function is the modified version of above function which checks the shape and calculate area accordingly after taking 3 args d,d2,shape and if shape does not matches it returns invalid shape
    if shape == "triangle":
        area = 0.5 * d1 * d2
        return area

    elif shape == "rectangle":
        area = d1 * d2
        return area

    else:
        return "Invalid shape"

    return area
    

d1=int(input("Enter the d1: "))
d2=int(input("Enter the d2: "))
shape=input("Enter the shape: ")
print("Total area:",calculate_area(d1,d2,shape))