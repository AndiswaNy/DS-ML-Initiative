#Number 1

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


set = set1.intersection(set2)
print(set)
        

#Number 2
list_sca  = ['floyd2@hotmail.com', 'jb23forever@yahoo.com', 'adesade4@gmail.com', 'bimpeadeola@gmail.com','harunaik@yahoo.com', 
             'chikaoluchi@gmail.com', 'sweetheart4eva@hotmail.com', 'fionashrek@gmail.com', 
             'peace_goodness@hotmail.com', 'edmud@yaohoo.com']

def email_extractor(email_list = "list_sca", email_type = " "):
    group_email = email_type

    if email_type == "yahoo":
        print(" 'jb23forever@yahoo.com', 'harunaik@yahoo.com', 'edmud@yahoo.com' ")
    elif email_type == "hotmail":
        print(" 'joyfloyd2@hotmail.com', 'sweetheart4eva@hotmail.com', 'peace_goodness@hotmail.com' ")
    elif email_type == "gmail":
        print(" 'adesade4@gmail.com', 'bimpeadeola@gmail.com', 'chikaoluchi@gmail.com', 'fionashrek@gmail.com'") 
    else:
        print("Error")
        
email_extractor("list_sca", "gmail")


#Number 3
value1 = int(input("Enter value: "))
sign = input("Enter the sign: ")
value2 = int(input("Enter value: "))
if sign == "+":
    answer =  value1 + value2
    print(answer)
elif sign == "-":
    answer = value1 - value2
    print(answer)
elif sign == "*":
    answer =  value1 * value2
    print(answer)
elif sign == "/":
    answer = value1 / value2
    print(answer)
else:
    print("Error. Please check your sign")

    
#Number 4
def test_one ():
    test_list = [1, 4, 62, 78, 32, 23, 90, 24, 2, 34, 28, 18, 12, 64, 50, 11, -1, 0, 30]
    count = 0
    for n in test_list:
        if n > 30:
           count = count + 1
    print("The number of numbers greater than 30 are " + str(count))

    
test_one ()


#Number 5
def indicate(word = " "):

    word = input("Enter word:")
    word = word[-1::-1]
    print("Palindrome test results: " + word)

indicate("Andiswa")


#Question 6
name= input("Please enter your name: ")
number_of_red_scarf= int(input("How many red scarfs do you want? "))
number_of_blue_scarf= int(input("How many blue scarfs do you want? "))
number_of_white_scarf= int(input("How many white scarfs do you want? "))
date = input("Please enter today's date (dd/mm/yy): ")

cost_of_red_scarf= int(500)
cost_of_red_scarf= int(750)
cost_of_red_scarf= int(800)

total_cost = (cost_of_red_scarf * number_of_red_scarf) + (cost_of_red_scarf*number_of_blue_scarf) + (cost_of_red_scarf*number_of_white_scarf)

print("Invoice")
print("Name: " + name )
print("Red scarf: " + str(number_of_red_scarf))
print("Blue scarf: " + str(number_of_blue_scarf))
print("White scarf: " + str(number_of_white_scarf))
print("Order price: " + str(total_cost))
print("Date ordered: " + date)


# number 7
def generate_colours (colour_code = " ", number_of_coulours =" "):

  if colour_code == "rgb":
    import random

    r = random.randint (0,255)
    g = random.randint (0,255)
    b = random.randint (0,255)
    rgb = [r,g,b]
    
    if number_of_coulours == "1":
      print ([("rgb" + str(rgb))])
    elif number_of_coulours == "2":
      print(([("rgb" + str(rgb))]*2))
    elif number_of_coulours == "3":
      print(([("rgb" + str(rgb))]*3))
    else:
      print("Error")
        
  elif colour_code == "hexa":
    import random
    if number_of_coulours == "1":
      print(["#"+"".join([random.choice("abcdef0123456789") for i in range(6)])])
    elif number_of_coulours == "2":
      print(["#"+"".join([random.choice("abcdef0123456789") for i in range(6)])]*2)
    elif number_of_coulours == "3":
      print(["#"+"".join([random.choice("abcdef0123456789") for i in range(6)])]*3) 
    else:
      print("Error")
  else:
    print("Please enter colour_code or hexa")
        
generate_colours("rgb", "2")


#number 8
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list[::2])


#number 9
def fizzbuzzz(number = " "):
    if int(number) % 3 == 0 and int(number) % 5 == 0:
        result = "fizzbuzz"
        return result
    elif int(number) % 3 == 0:
        result = "fizz"
        return result
    elif int(number) % 5 == 0:
        result = "buzz"
        return result
    else:
        result = number
        return result 
        
results = fizzbuzzz("15")
print (results)


#number 10
s = int(input("Enter speed: "))
if s <= 70:
    print ("OK")
else:
    p = 0
    if s > 70:
        p = p + (s-75)//5 + 1
        print ("Points: " + str(p))
        if p>12:
            print("Licanse is suspended.")


#number 11
from functools import reduce
  
fibonacci  = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])
  
print(fibonacci(8))


#Number 121
class Person():
    def __init__(self, get_String):
        self.get_String = get_String

    def print_String(self):
        print(self.get_String)
        
userfeedback = Person("Andiswa")
userfeedback.print_String()

