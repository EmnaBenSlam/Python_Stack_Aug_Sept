num1 = 42 #variable declaration primitives data types Numbers initialize
num2 = 2.3 #variable declaration primitives data types decimal Numbers initialize
boolean = True #variable declaration primitives data types boolean initialize
string = 'Hello World' #variable declaration primitives data types string initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration Data Types Composite list initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration Data Types Composite dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration Data Types Composite tuples initialize
print(type(fruit)) #log statement tulpes check
print(pizza_toppings[1]) #  log statement access value list
pizza_toppings.append('Mushrooms') # add value list
print(person['name']) # log statement access value dictionary
person['name'] = 'George' #change value dictionary
person['eye_color'] = 'blue' # change value dictionary
print(fruit[2]) # log statement acces value tulpes

if num1 > 45: #conditional if
    print("It's greater") #log statement 
else: #conditional else
    print("It's lower") #log statement 

if len(string) < 5:#conditional if
    print("It's a short word!") #log statement 
elif len(string) > 15: #conditional elif
    print("It's a long word!")#log statement 
else:#conditional else
    print("Just right!")#log statement 

for x in range(5): #for loop s
    print(x) #log statement 
for x in range(2,5): # for loop  start,stop
    print(x) #log statement 
for x in range(2,10,3): # for loop  start stop increment
    print(x) #log statement 
x = 0 # variable declaration 
while(x < 5): #While loop 
    print(x) #log statement 
    x += 1 #While loop increment

pizza_toppings.pop() #delete the last value of list
pizza_toppings.pop(1)# delete the second value of list 

print(person) # log statement dictionary
person.pop('eye_color') # delete value  dictionary
print(person) #log statement dictionary

for topping in pizza_toppings: #for loop list
    if topping == 'Pepperoni': # conditional if
        continue # for loop continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional if
        break#  for loop break

def print_hello_ten_times(): # define function 
    for num in range(10): #for loop 
        print('Hello') #log statement 

print_hello_ten_times() # Call function

def print_hello_x_times(x): # define function ,parameter
    for num in range(x): #for loop sequence
        print('Hello') #log statement 

print_hello_x_times(4) #call function 

def print_hello_x_or_ten_times(x = 10): #function argument
    for num in range(x):  #for loop sequence
        print('Hello')

print_hello_x_or_ten_times() #log statement 
print_hello_x_or_ten_times(4) #log statement 


"""  # multiline comment
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry' 
# print(person['favorite_team']) 
# print(pizza_toppings[7]) 
#   print(boolean)
# fruit.append('raspberry') 
# fruit.pop(1) 



