#1
#prints personal info
personal_info=("bio-informatica")
print(personal_info)
print("//////////////////////////////////////////////////////////////////////////////////////")

#2
#calculates 23% of the input and then prints it
sales = input("Enter sales: ")
profit=float(sales) * float("0.23")
print("Printing Profit")
print(profit)
print("//////////////////////////////////////////////////////////////////////////////////////")

#4
#asks for prices of the items 
item1 = input("enter price of item 1: ")
item2 = input("enter price of item 2: ")
item3 = input("enter price of item 3: ")
item4 = input("enter price of item 4: ")
item5 = input("enter price of item 5: ")
#calculates tax for every item
Item1=float(item1) * float("0.07")
Item2=float(item2) * float("0.07")
Item3=float(item3) * float("0.07")
Item4=float(item4) * float("0.07")
Item5=float(item5) * float("0.07")
#calculates the sum of all the items together and prints it
subtotal= float(item1) + float(item2) + float(item3) + float(item4) + float(item5)
print("subtotal")
print(subtotal)
#calculates the sum of all the taxes and prints it
tax= float(Item1) + float(Item2) + float(Item3) + float(Item4) + float(Item5)
print("tax")
print(tax)
print("______________________________________")
#claculates the sum of tax and subtotal all items and prints it
Subtotal= float(tax) + float(subtotal)
print("total")
print(Subtotal)
print("//////////////////////////////////////////////////////////////////////////////////////")

#5
#asks for inputs
speed= input("enter Mph: ")
time= input("enter amount of time traveled in hours: ")
#multiplies the inputs with each other to calculate distance and prints it
distance= float(speed) * float(time)
print(distance,"Miles")
#calculates and prints some standards
print("distance traveled at 70 miles per hour")
      
print("distance traveled after 6 hours")      
I= float("70") * float("6")
print(I)
      
print("distance traveled after 10 hours")     
II= float("70") * float("10")
print(II)
      
print("distance traveled after 15 hours")     
III= float("70") * float("15")
print(III)
print("//////////////////////////////////////////////////////////////////////////////////////")
      
#7
#asks for inputs
MD=input("enter miles droven: ")
GG=input("enter gallons of gas used: ")
#divides the inputs with eachother to calculate MPG and prints it
MPG= float(MD) / float(GG)
print("Miles per Gallon")
print(MPG)
print("//////////////////////////////////////////////////////////////////////////////////////")

#10
#asks for amount of cookies you want
cookie= input("Amount of cookies you want to make: ")
#divides the ingredients for 48 cookies so it is for 1 cookie
butter= float("1") / float("48")
sugar= float("1.5") / float("48")
flour= float("2.75") / float("48")
#multiplies amount of cookies with the amount of ingredients you need for 1 cookie
SU= float(sugar) * float(cookie)
BU= float(butter) * float(cookie)
FL= float(flour) * float(cookie)
#prints how much you will need for your amount of cookies
print("Amount of cups of sugar needed for your amount of cookies")
print(SU)
print("Amount of cups of butter needed for your amount of cookies")
print(BU)
print("Amount of cups of flour needed for your amount of cookies")
print(FL)
