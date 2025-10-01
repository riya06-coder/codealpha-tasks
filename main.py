# """variables"""

# # RiyaThakur = "student"   # pascal case (of variables)

# # riyaThakur = "student"   # camel case

# # riya_thakur = "student"  # snake case

# # a = 12        # int datatype
# # print(type(a))

# # b = 22/7      # float datatype
# # c = 6/3
# # print(type(b))
# # print(type(c))

# # v = 23j        # complex datatype
# # print(type(v))
# # g = 2j
# # print(type(g))

# # st = "hey 24 @#$ GHJ"   # string datatype ("stores anything 23@")
# # print(type(st))

# # m = True                # boolean datatype True or False
# # t = False
# # print(type(m))
# # print(type(t))

# # a = "A"
# # print(ord(a))    # shows unicodes of everthing
# # d = "#"
# # print(ord(d))

# # a = 65
# # print(chr(a))   # shows the character value of any unicode

# # a = "Riya Thakur"  # string indexing 
# # print(a[-5])
# # print(a[2],a[-5])

# # a = "Riya Thakur"    # string slicing   a[start:stop+1:steps]
# # print(a[0:4:1])
# # print(a[5:11:1])
# # print(a[5::1])

# # a = 12
# # print(type(a))


# #  # type conversion
# #  # explicit - user use build function to convert datatypes into one another.
# # a = 12          

# # a = str(a)

# # print(type(a))
# # a = float(a)
# # print(type(a))
# # print(a)

# # a = "345"
# # a = int(a)
# # print(type(a))
# # print(a)

# # a = bool(a)    # 7 falsy values of boolean are False, 0, 0.0, "", [], (), {}  these always gives false values others are true
# # print(a)

# # #implicit - in this python automatically converts data from one datatype to another.

# # a = 12
# # print(a/2) # ans in float 6.0

# # name = "Riya"
# # age = "21"

# # print(name,age)  # output

# # print("hello my name is",name,"and my age is",age)

# # # formatted string
# # print(f"my name is {name} and my age is {age}")
 
# # a = 2
# # b = 5
# # print(f"addition of numbers is {a+b} and subtraction of numbers is {a-b}")

# # #input

# # # age = int(input("hello what is your age"))

# # # print(age)


# # # exercise.1 accept number from user.

# # # number = int(input("hey type any number here : "))
# # # print(f"the number you typed is: {number}")

# # # exercise.2 accept age from user and print it.

# # # age = int(input("hey whats your age : "))
# # # print(f"Your age is : {age}")

# # # Operators
# # # 1. Arithmatic operators (7)

# # a = 10
# # b = 30

# # /


# # a = 9

# # if a > 10 :
# #     print("I will do Task A")

# # else:
# #     print("I will do Task B")


# # number = int(input("please enter any number"))

# # if number %2 ==0
# #     print("even")

# # else:
# #     print("odd")



# # money = int(input("please enter a number"))

# # if money==10:
# #     print("chocobar")

# # else:
# #     print("mango dolly")


# # money = int(input("please enter a number"))

# # if money==10:
# #     print("chocobar")

# # elif money==20:
# #     print("mango dolly")

# # else:
# #     print("cone")


# # number = int(input("PLease enter a Number"))

# # if number%2==0:
# #     print("It is EVEN NUMBER")

# # else:
# #     print("It is ODD NUMBER")


# #QUESTIONS

# # print("question 1: Accept 2 numbers and print the greatest between them")

# # a = int(input("Enter the first number"))
# # b = int(input("Enter the second number"))

# # if a>b:
# #     print(f"The greatest number is: {a}")

# # else:
# #     print(f"The greatest number is: {b}")


# # print("q2 Accept the gender from user in char and print the respective greeting messages")

# # # gen = input("please tell your gender as characters (M or F):-")

# # # if gen=="M" or gen=="m":
# # #     print("Hello SIR")

# # # elif gen=="F" or gen=="f":
# # #     print("Hello MA'AM")

# # # else:
# # #     print("unidentified gender")


# # # print("even odd question")

# # # num= int(input("enter the number"))

# # # if num%2==0:
# # #     print("even")

# # # else:
# # #     print("odd")


# # # print("Q4: accect name and age from the user. check if the user is a valid voter or not")

# # # name= input("Enter your Name here :- ")
# # # age= int(input("Enter your age here:- "))

# # # if age<18:
# # #     print(f"{name} is not valid for Voting")

# # # else:
# # #     print(f"{name} is valid for voting")


# # # print("q5: accept a year and check if it is a leap year or not")

# # # year = int(input("Enter a year here :- "))

# # # if year%100==0 and year%400==0:
# # #     print("This is a Leap Year")

# # # elif year %100 != 0 and year %4 ==0:
# # #     print("this is a Leap Year")    

# # # else:
# # #     print("This is not a Leap Year")



# # # print("Q4: accect name and age from the user. check if the user is a valid voter or not")

# # # name= input("Enter your Name here :- ")
# # # age= int(input("Enter your age here:- "))

# # # if age<18:
# # #     print(f"{name} is not valid for Voting, please wait for {18-age} years to vote.")

# # # else:
# # #     print(f"{name} is valid for voting")

# # # print("if- elif ladder")

# # # temp = int(input("Enter the temperature in celcius:- "))

# # # if temp<0:
# # #     print("Freezing cold")

# # # elif temp>=0 and temp<10:
# # #     print("Very cold")

# # # elif temp>=10 and temp<20:
# # #     print("Cold")

# # # elif temp>=20 and temp<30:
# # #     print("Pleasant")

# # # elif temp>=30 and temp<40:
# # #     print("Hot")

# # # else:
# # #     print("Very Hot")


# # ### Loops : python has 2 loops for loop and while loop.
# # # For loop works specifc number.
# # # While loop works for conditions.

# # # for loop
# # # a = range(1,21,1)

# # # for i in a:
# # #     print(i)

# # # for i in range(1,21,1):
# # #     print(i)

# # # for i in range(21):
# # #     print(i)

# # # for i in range(20,51):
# # #     print(i)

# # # for i in range(16,0,-1):
# # #     print(i)

# # # for i in range(-3,-16,-1):
# # #     print(i)

# # # print("lets print table of 5")

# # # for i in range(7,71,7):
# # #     print(i)

# # # print("lets print table of n")

# # # n = int(input("Enter a number to print its table : "))

# # # for i  in range(n,n*10+1,n):
# # #     print(i)

# # # a = "RIYA THAKUR"
# # # # print(a[0])
# # # for i in range(11):
# # #     print(a[i])  

# # # b = "123456 89"
# # # print(len(b))

# # a = "hey i am here to tell you string loop"
# # print(len(a))

# # for i in range(37):
# #     print(a[i])

# # a = "hey i am here to tell you string loop"

# # for i in range(len(a)):
# # #     print(a[i])

# # a = "riya is cool"

# # for i in a:
# #     print(i)


# # for i in range(1,21):
# #     if i==15:
# #         break
# #     print(i)

# # for i in range(1,21):
# #     if i==15:
# #         continue
# #     print(i)

# # for i in range(1,51):
# #     if 20<=i<=30:
# #         continue
# #     print(i)

# # for i in range(1,21):
# #     if i==34:
# #         print("break statement executed")
# #         break
# #     print(i)

# # else:
# #     print("break statement is not executed")


# # for i in range (1,21):
# #     if i>=21:
# #         print("break statement")
# #         break
# #     print(i)

# # else:
# #     print("break statement is not executed")

                
# #                       ######### QUESTIONS #########

# # print("Q1: accept an integer and print hello world n times")

# # a = int(input("Enter and integer to print hello world :- "))
# # for i in range(a):
# #     print("Hello World")

# # print("Q2- print natural numbers upto n")

# # n = int(input("enter a number to print natural numbers"))
# # for i in range(1,n+1):
# #     print(i)

# # print("Q3- reverse for loop. print n to 1")
# # n = int(input("enter a number to print revers loop: "))
# # for i in range(n,0,-1):
# #     print(i)

# # print("Q4- take a number as input and print its table")
# # a = int(input("Enter a number to print its table"))
# # for i  in range(a,a*10+1,a):
# #     print(i)

# # n = int(input("Which table you want to print"))

# # for i in range(1,11):
# #     print(f"{n}*{i}={n*i}")



# # print("Q5- sum upto n numbers")
# # n = int(input("Enter a number to sum upto it"))
# # for i in range(1,n,1):
# #     print(i)

# # n = int(input("enter number to print table"))
# # for i in range(1,11):
# #     print(f"{n} * {i} = {n*i}")

# # print("Q5-sum upto n terms")

# # n = int(input("enter a number"))
# # sum = 0
# # for i in range(1,n+1):
# #     sum = sum + i

# # print(f"Your sum of numbers upto {n} is = {sum}")

# # print("Q6- print factorial of a number")
# # n = int(input("Enter a number"))
# # factorial = 1
# # for i in range(1,n+1):
# #     factorial = factorial * i

# # print(f"factorial of number {n} is= {factorial}")

# # n = int(input("Enter a number:- "))

# # even = 0
# # odd = 0
# # for i in range(1,n+1):
# #     if i%2==0:
# #         even = even+i
# #     else:
# #         odd = odd + i

# # print(f"your even and odd sum are {even} , {odd} respectively")


# # n = int(input("Enter a number"))
# # even = 0
# # odd = 0
# # for i in range(1,n+1):
# #     if i%2==0:
# #         even= even+i
# #     else:
# #         odd= odd+i
# # print(f"Your sum of even and odd are {even}, {odd} respectively")

# # n = int(input("enter a number"))
# # for i in range(1,n+1):
# #     if n%i==0:
# # #         print(i)

# # n = int(input("enter a number"))
# # sum = 0
# # for i in range(1,n):
# #     if n%i==0:
# #         sum = sum + i

# # if sum == n:
# #         print("your number is a perfect number")

# # else:
# #         print("your number is not a perfect number")

        
# # n = int(input("Enter a number n"))
# # sum = 0
# # for i in range(1,n):
# #     if n%i==0:
# #      sum = sum+i

# # if sum == n:
# #    print(f"The number {n} is a perfect number")

# # else:
# #    print(f"The number {n} is not a perfect number")

# # n = int(input("check your number is prime or not:- "))
# # count=0
# # for i in range (1,n+1):
# #     if n%i==0:
# #         count = count +1

# # if count==2:
# #     print(f"The number {n} is prime number")

# # else:
# #     print(f"The number {n} is not prime")

# # a = "RIYA THAKUR"
# # b = ""
# # for i in range(len(a)-1,-1,-1):
# #     b = b + a[i]
    
# # print(b)    
# #                                                     Concatenate
# # a = "DELHI PUBLIC SCHOOL SAGAR"
# # b = ""
# # for i in range(len(a)-1,-1,-1):
# #     b = b + a[i]

# # print(b)


# # a = "RAGAS LOOHCS CILBUP IHLED"
# # b=""
# # for i in range(len(a)-1,-1,-1):
# #     b = b + a[i]
# # print(b)


# # print("check string is Pallindrome or not")

# # a = input("Enter the string to check Pallindrome :- ")
# # b = ""
# # for i in range(len(a)-1,-1,-1):
# #     b = b + a[i]

# # if b==a:
# #     print("This string is Pallindrome")

# # else:
# #     print("This string is not pallindrome")


# # a = "a#s$1^2d'S'34f"

# # char = 0
# # dig = 0
# # spchr = 0

# # for i in a:
# #     if i.isdigit():
# #         dig +=1
# #     elif i.isalpha():
# #         char +=1
# # #     else:
# # #         spchr +=1

# # # print(f"Your characters are {char}, digits are {dig}, special characters are {spchr}")  


# # str1 = "P@#yn26at^&i5ve"
# # char = 0
# # dig = 0
# # spchar = 0

# # for i in str1:
# #     if i.isalpha():
# #         char +=1
# #     elif i.isdigit():
# #         dig +=1
# #     else:
# #         spchar +=1

# # print(f"You have\n{char} Characters,\n{dig} Digits and\n{spchar} Special Characters")    


# # ############## print(dir(str))###############



# # While loop

# # a = 1

# # while a<=30:
# #     print(a)
# #     a=a+1

# # print("Q:- Separate each digit of a number and print it on new line.")

# # a  = 256

# # while a >0 :
# #     print(a%10)
# #     a=a//10
    
# # print("Q:- Separate each digit of a number and print it on new line.")

# # a= int(input("Enter the number here to separate the digits:- "))

# # # while a>0:
# # #     print(a%10)
# # #     a= a//10

# # print("Q:- Accept a number and print its reverse")

# # a = int(input("Enter a number to print its reverse:- "))

# # rev = 0

# # while a >0:
# #     rev = rev*10 + a%10
# #     a = a//10

# # print(rev)

# # print("Accept a number and print its reverse")

# # a = int(input("Enter a number to print its reverse here:- "))

# # rev = 0

# # while a>0:
# #     rev = rev*10 + a%10
# #     a=a//10
# # print(rev)

# # a = int(input("enter to find reverse:- "))
# # rev = 0

# # while a>0:
# #     rev = rev * 10 + a%10
# #     a= a//10
# # print(rev)

# # a = int (input("Enter a number to check pallindromic or not:- "))
# # b = a
# # rev = 0

# # while a>0:
# #     rev = rev*10 + a%10
# #     a= a//10

# # if b==rev:
# #     print(f"{b} is pallindromic number")

# # else:
# #     print(f"{b} is not pallindromic number")

# # print("Create a random number guessing game with python")

# # import random          ####### random is a library

# # num = random.randint(1,10)

# # print(num)


# # print("random number guessing game")

# # a = int(input("Guess a number between 1 to 10 :- "))

# # import random
# # num = random.randint(1,10)
# # if  a==num:
# #     print(f"Congrates you guessed the number {num} right")
# # else:
# #     print(f"Better luck next time.\nThe correct number was {num}")

                                            
#                                              # ####     Functions

# # user defined functions

# # def hello():
# #     print("this is hello function")

# # # hello()       # call it then only it runs

# # def sum(a,b):
# #     print(f"The sum of your numbers is {a+b}")

# # sum(12,12)
# # sum(22,32)
# # sum(23,23) # positional arguments

# # def hello(name,age):
# #     print(f"Your name is {name} and your age is {age}")
# # hello()


# # ##keyword argument
# # def hello(name,age)
# #     print(f"your name is {name} and age is {age}")

# # # default argument
# # def hello(a,b=20):
# #     print(f"the sum is {a+b}")

# # hello(12)


# # a = input("Enter a string here:- ")
# # while [a]>-1:
# #         b = b*10 + a%10
# #         a= a//10
# # if a==b:
# #         print("they are pallindromic")

# # else:
# #         print("they are not pallindromic")
# # # def pallindrom(a,b):

# # print("check if a string is pallindrom or not")

# # def pallindrome(st):
# #     rev = ""
# #     for i in range(len(st)-1,-1,-1):
# #         rev = rev + st[i]

# #     if rev == st:
# #         print("pallindrom")
# #     else:
# #         print("not a pallindrom")

# # pallindrome("naman")
# # pallindrome("bharat")
# # pallindrome("rrrr")

# # print("reverse of a string")

# # a = input("Enter a string to print its reverse:- ")
# # rev = ""
# # for i in range(len(a)-1,-1,-1):
# #     rev = rev + a[i]
# # print(rev)


# # print("string is pallindrom or not")

# # a = input("enter a string:- ")
# # rev = ""
# # for i in range(len(a)-1,-1,-1):
# #     rev = rev + a[i]

# # # if rev==a:
# # #     print("pallindrome")
# # # # else:
# # # #     print("not a pallindrome")

# # # print("string is pallindrom or not")

# # def pallindrome(string):
# #     rev = ""
# #     for i in range(len(string)-1,-1,-1):
# #         rev = rev + string[i]
# #     if rev == string:
# #         print()"Its pallindrome")
# #     else:
# #         print("its not pallindrom")

# # pallindrome("heyyy")
# # pallindrome("naman")
# # pallindrome("raja ")
# # pallindrome("    ")
# # pallindrome(".   ")

# # def hello():
# #     print("hello how are you")

# # hello()

# # def hello():
# #     return "hello how are you"

# # print(hello())

# # a = [12,13,14,15.65,21,12,True,print(),3]

# # print(a[2])
# # print(a[1:8:1])
# # print(a[0:4])
# # print(a[-3])

# # a[2]=4
# # print(a) #modifing the list.

# # a = [12,13,14,15,16,17.23]

# # # 1st way of list traverse using index 

# # for i in range(len(a)):
# #     print(i)

# # for i in range(len(a)):
# #     print(a[i])

# # 2nd way list traverse using direct values.

# # a = [12,13,14,15,16,17.23]

# # for i in a:
# #     print(i)

# # print(dir(list))
# # help(list)


# ######## methods
# l = [1,3,2,3,4,5]

# # # l.append(6)
# # # l.append(4)
# # # l.append(3.33)

# # l.insert(4,2)
# # l.remove(3)
# # l.extend([6,4,3,4])
# # popped_item = l.pop(2)
# # # popped_item = l.pop(0)
# # index = l.index(4)

# # # print(l)

# # # l = [1,2,3,4,5]
# # # # l[0]=10
# # # # print(l[0])


# # # ##### questions on list

# # # print("Q1:- print positive and negative elements of an list")
# # # a = input("enter a list of numbers:- ")
# # # positive = 0
# # # negative = 0
# # # for i in a:
# # #     if a[i]>0:
# # #         positive = positive+a[i]
# # #     else:
# # #         negative = negative+a[i]

# # # l = [1,2,-3,4,-12,-2,3,-123,2]

# # # print("positive elements are:- ")
# # # for i in l:
# # #     if i>=0:
# # #         print(i) 

# # # print("negative elements are:- ")
# # # for i in l :
# # #     if i<0:
# # # #         print(i) 

# # # l = [2.3,1,-3,4,-2,-2,4,2,-4]

# # # print("positive numbers are:- ")
# # # for i in l:
# # #     if i>=0:
# # #         print(i)

# # # # print("negative numbers are:- ")
# # # # for i in l:
# # # #     if i<0:
# # # #         print(i)

# # # print("print mean of the list")

# # # l = [2,3,4,6,21,56,3]
 
# # # sum = 0
# # # for i in l:
# # #     sum += i 

# # # mean = sum/len(l)

# # # print(mean)


# # print("Find the greatest element and print its index too.")

# # l = [2,3,4,5,12,6,7,8,3]

# # a = 0

# # for i in l:
# #     if i>a:
# #         a = i
        
# # print(f"the greatest element is {a} ")

# # l = [2,343,4,23,4,97,2,2,5,63]

# # largest = 0
# # index = 0

# # for i in range(len(l)):
# #     if l[i] > largest:
# #         largest = l[i]
# #         index = i

# # print(f"greatest number is {largest} and its index is {index}")


# # list =  [1,2,49,4,2,46,35,2,45]

# # largest = 0
# # index = 0

# # # for i in range(len(list)):
# # #     if list[i] > largest:
# # #         largest = list[i]
# # #         index = i
# # # print(f"largest number is {largest} and its index is {index}")

# # print("find the second greatest element")

# # l = [3,8,4,2,5,6,13,12]
# # largest = l[0]
# # sec_largest = l[0]

# # for i in l:
# #     if i> largest:
# #         sec_largest = largest
# #         largest = i
# #     elif i > sec_largest:
# #         sec_largest=i
        
# # print(sec_largest,largest)



# # print("Fint the second largest element")

# # l = [1,2,3,4,5,4,3,2,5,6,4,8,4,3,5,9]
# # largest = l[0]
# # sec_largest = l[0]

# # for i in l:
# #     if i> largest:
#           sec_largest = largest
# #         largest = i
# #     elif i > sec_largest:
# #         sec_largest = i

# # print(f"Second largest element is : {sec_largest}, and the largest element is {largest}")

# print("Fint the second largest element")

# l = [7,5,6,3,9,8]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i

# print(sec_largest,largest)

# print("check if list is sorted or not")

# l = [1,4,3,4]

# for i in range(len(l)-1):
#     if l[i] < l[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break

# else:
#     print("Your list is sorted")

                                       ################ tuple

# a = (1,2,3,4,5,2,3)
# b = [1,2,3,4,5,2,3]

# print(type(a))
# print(type(b))

# a[0] = 2
# b[0] = 2
# print(a,b)

# a = (1,2,3,4,3,3,3,3,5,2,3)
# print(a[2])

# for i in a:
#     print(i)

# for i in range(len(a)):
    # print(i)

# index = a.index(3)
# print(index)
# count = a.count(3)
# print(count)

# a,b,c,d = (1,2,4,2)

# print(a,b,c,d)
# print(d)

# a = (1,)

# print(type(a))

# s = {1,2,3,4,5,2,3}

# print(s[3])

# b = hash("H")
# print(b)

# c = hash((1,2,3,4))
# # print(c)

# a = {1,2,8,9,"hello",3,4,5}

# for i in a:
#     print(i)
 
              ############# set methods

# s = {1,2,3,4,5,6}

# s.add(9)
# s.add(7)
# s.add(0)

# s.remove(7)
# s.remove(1)

# s.discard(2)
# s.discard(11)

# popped_element = s.pop()
# s.clear()

# print(s)

# a = {1,2,3,4}
# b = {4,5,6,7}

# union_set = a.union(b)
# intersection_set = a.intersection(b)
# difference_set = a.difference(b)
# difference_set_2 = b.difference(a)
# symmetric_diff = a.symmetric_difference(b)
# symmetric_diff_2 = b.symmetric_difference(a)

# print(f"{union_set}\n{intersection_set}\n{difference_set}\n{difference_set_2}\n{symmetric_diff}\n{symmetric_diff_2}")

#  ##### shortcuts

# print(a | b) # union
# print(a & b)  # intersection
# print( a - b)  # difference
# print(a ^ b)    # symmetric difference



# a = {1,2,3,4}
# b = {4,5,6,7}

# b -= a
# a -= b

# print(a)
# print(b)

             ##### Dictionary  or Hash map
# dictionary have key and value pairs

# a = {}

# print(type(a))

# d = {1:"hello",2:21 , "hello":"hello"}

# print(type (d),d)

# d = {10:200, 20:300 ,30:400, 40:500}

# print(d[30])
# d[20] = 700
# print(d)

# d.update({5:50})  # updating
# d[2] = 200    # creating
# del d[30]   # deleting

# print(d)

# d = {10:200, 20:300 ,30:400, 40:500}

# for i in d.values():
#     print(i)

# help(dict)
# d.clear()


# a = [1,2,3,4,5]

# b = a.copy()

# b[0] = 100

# print(a)
# print(b)

# d = {10:200, 20:300 ,30:400, 40:500}

# d2 = d.copy()
# d2[10] = 100
# d2 = d.get(20)

# print(d.items())

  ### questions

# print("q1 - write a python script to merrge two python dictionaries.")

# d1 = {10:100,20:200,30:300,40:290}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)

# print("q2- print sum all the values in a dictionary.")

# d1 = {10:100,20:200,30:300,40:400}
# sum = 0

# for i in d1.values():
#     sum += i

# print(sum)

# print("count the frequency of each elements in a list")

# a = [1,1,1,1,1,1,1,2,2,2,1,2,3,3,3,4,4,4,5,3,3,3,4,3,2,4]

# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] +=1
#     else:
#         d[i]=1

# print(d)

# print("write to combine two dictionary by adding values for common keys.")

# d1 = {10:100,20:200,30:300,40:400}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]
# print(d1)