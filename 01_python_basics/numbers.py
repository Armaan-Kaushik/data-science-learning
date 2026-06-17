# Calculating Total distance fron nyc to baltimore and then baltimore to pitsburg.
nyc_balt=188
balt_pits=247 
total_dist=nyc_balt+balt_pits
print("Total dist:",total_dist)


#Calculating time taken to cover a certain distance at a certain speed and rounding off it to 2 digits.
mph=65
time=total_dist/mph
print("Time Taken:",round(time,2)) 

# Practice Questions
# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
length=92
width=48.8
Total_area=length*width
print("Total_area: ",round(Total_area,2))

# 2.You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
pkts=9
pkt_cost=1.49
amt_paid=20
total_cost=pkts*pkt_cost
amt_return=(amt_paid-total_cost)
print("Amount to be returned: ",amt_return)

# 3.You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
len_tile=5.5
area_tile=len_tile**2
print("Total area: ",area_tile)
cost_persqft=500
total_cost=area_tile*cost_persqft
print("Total Cost:",total_cost)

# 4.Print binary representation of number 17
num=17
print("Binary of num 17 is:",format(num,'b'))
print("Octal of num 17 is:",format(num,'o'))
