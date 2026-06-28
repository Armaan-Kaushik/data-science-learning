# # #Dictionary
# # d={"Tom":7234567890,"rob":2345678901,"joe":1234567890}
# # print(d)
# # print(d["Tom"])
# # d["sam"]=2354679810
# # print(d)
# # del d["sam"]
# # print(d)

# # for key in d:
# #     print("key:",key,"value:",d[key])

# # for k,v in d.items():
# #     print("key:",k,"value:",v)


# # print("Tom" in d)

# #Tuple
# # p=(5,9)
# # print(p[1])

# #Exercise

# # Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them
import math

def circle_calc(radius):
    area=math.pi*(radius**2)
    circumference=2*math.pi*radius
    diameter=2*radius
    return area, circumference,diameter

if __name__=="__main__":
    r=input("Enter a radius:")
    r=float(r)
    area, c, d = circle_calc(r)
    print(f"area {area}, circumference {c}, diameter {d}")



# # We have following information on countries and their population (population is in crores),

# # Country	Population
# # China	    143
# # India 	136
# # USA	    32
# # Pakistan	21
# # Using above create a dictionary of countries and its population
# # Write a program that asks user for three type of inputs,
# # print: if user enter print then it should print all countries with their population in this format,
# # china==>143
# # india==>136
# # usa==>32
# # pakistan==>21
# # add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
# # remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
# # query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country


population={"china":143,"india":136,"usa":32,"pakistan":21}

def add():
    country=input("Enter the country name: ")
    country=country.lower()
    if country in population:
        print("Country already exist in our dataset. Terminating the search.")
        return
    p=float(input(f"Enter the population for {country}"))
    population[country]=p
    print_all()


def remove():
    country=input("Enter the country name: ")
    country=country.lower()
    if country  not in population:
        print("Country does not exist in our dataset. Terminating the search.")
        return
    del population[country]
    print_all()

def query():
    country=input("Enter the country name to query: ")
    country=country.lower()
    if country  not in population:
        print("Country does not exist in our dataset. Terminating the search.")
        return
    print(f"population of {country} is: {population[country]}")
    print_all()
          

def print_all():
    for country,p in population.items():
         print(f'{country}==>{p}')


def main():
    op=input("Enter operation(add, remove, query, print): ")
    if op.lower()=='add':
        add()
    if op.lower()=='remove':
        remove()
    if op.lower()=="query":
        query()
    if op.lower()=="print":
        print_all()

if __name__=="__main__":
    main()

# You are given following list of stocks and their prices in last 3 days,
# Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]
# Write a program that asks user for operation. Value of operations could be,
# print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33
# add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.
import statistics
stocks = {
    'info': [600,630,620],
    'ril': [1430,1490,1567],
    'mtl': [234,180,160]
}

def print_all():
    for stock,price_list in stocks.items():
        avg= statistics.mean(price_list)
        print(f"{stock}==>{price_list}==>avg: round(avg,2))",round(avg,2))

def add():
    s=input("Enter a stock ticker to add:")
    p=input("Enter the price of stock")
    if s in stocks:
        stocks[s].append(p)
    else:
        stocks[s]=[p]
    print_all
    
def main():
    op=input("Enter operation (print, add or append):")
    if op.lower() == 'print':
        print_all()
    elif op.lower() == 'add':
        add()
    else:
        print("Unsupported operation:",op)

if __name__ == '__main__':
    main()


