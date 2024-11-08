#SUM OF N NATURAL NUMBER
#n=int(input("Enter the limit n: "))
#sum=0
#for x in range(1,n+1):
#    sum=sum+x
#print(sum)  
  
#ARMSTRONG NUMBER
#num=int(input("ENTER A NUMBER: "))
#order=len(str(num))
#if num==sum(int(i)**order for i in str(num)):
#    print("armstrong number")
#else:
#    ("print not armstrong")   
 
 #num=int(input("Enter the your number: "))
#temp=num
#sum=0
#power=len(str(num))
#while temp>0:
 #   a=temp%10
 #   b=a**power
 #   sum+=b
 #   temp//=10
#if sum==num:
#    print(f"the {num} is armstrong number")
#else:
#    print("the given number is not a armstrong number")        


#MULTIPLE OF 2                                                       
# num=int(input("ENTER A NUMBER: "))
# list=[x**2 for x in range(num)]
# print(list)  

 
#DIVISORS
# low=int(input("Enter the lower limit: "))
# up=int(input("Enter the up limit: "))
# num=int(input("Enter the number to be check: "))
# list=[x for x in range(up+1) if x%num==0]
# print(list)

#ASCII VALUE
# char=(input("Enter the char: "))
# print("the ASCII value of", char, "is", ord(char))

#HCF
# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# div1=[x for x in range(1,num1+1) if num1%x==0]
# print(div1)       
# div2=[y for y in range(1,num1+1) if num2%y==0]
# print(div2)
# hcf=max(div1 and div2)
# print(hcf)
         
#LARGEST NUMBER
# num1,num2=map(int,input("Enter two no. seperated by space: ").split())
# div1=[x for x in range(1,num1+1) if num1%x==0]       
# div2=[y for y in range(1,num1+1) if num2%y==0]
# hcf=max(div1 and div2)
# print(f"the hcf of {num1} and {num2} is",hcf)

# a=int(input("no.:" ))
# if a>0:
#     print("positive")
# elif a<0:
#     print("negative")        
# else:
#         print("0")    

#AREA OF A TRIANGLE
# dimensions=("Enter the dimensionns of a triange")
# base=float(input( "Base: "))
# height=float(input( "Height: "))
# side=float(input( "3rd side if have: "))
# area=1/2*base*height
# type=input("is it right angle angled triangle (y/n): ")
# if type=="n":
#     s=base+height+side
#     x=(s-base)+(s-height)+(s-base)
#     area=(s*x)**(1/2) 
#     print(area)
# else:
#     print(1/2*base*height)    


#CALCULATOR
# while True:
    
#     num1=int(input("Enter 1st Number:"))
#     operator=input("Enter oprator:")
#     num2=int(input("Enter 2nd Number:"))
#     if num1==00:
#         break
    
#     elif operator=="+":
#         print(num1+num2)
        
#     elif operator=="-":
#         print(num1-num2)
#     elif operator=="*":
#         print(num1*num2) 
#     elif operator=="/":
#         print(num1/num2)
    
    
# COMPUND INTERST

# import time 
# principle=float(input("Enter the principle amount:"))
# Rate=int(input("Enter the rate:"))
# Time=int(input("Enter the time period:"))
# R1=Rate/100
# R2=1+R1
# R3=R2**Time
# result2=R3*principle
# if principle <=0:
#         print("Principle amount cannot be less than 0 ")
# else:
#             print(result2)
            
#DASH REMOVER
# phone_number=input("Enter the phone number")
# for i in phone_number:
#     if i=="-":
#         continue
#     print(i,end="")    
    
#SWAPPING
# #a=float(input("Enter number a: "))
# #b=float(input("Enter number b: "))
# #c=a
# #a=b
# #b=c
# #print(f"a: {a} and b: {b}")

# #a=float(input("Enter number a: "))
# #b=float(input("Enter number b: "))
# #a=a-b
# #b=a+b
# #a=a-b
# #a=a*-1
# #print(f"a: {a} and b: {b}")

# a=float(input("Enter number a: "))
# b=float(input("Enter number b: "))
# a,b=b,a
# print(f"a: {a} and b: {b}")

#SQUREROOT
# import math
# a=float(input("Enter your number: "))
# b=math.sqrt(a)
# print(f"Square root of {a} is {b}")

# #**************************************

# num=float(input("Enter the numnber: "))
# squareroot=num**(1/2)
# print(f"the square root of {num} is: {squareroot}")

    
#SQURE PATTERN
# rows=int(input("Enter the number of rows:"))
# columns=int(input("Enter the number of columns:"))
# symbol=input("Enter the symbol you want to use in making pattern:")
# for i in range(rows):
#     for j in range(columns):
#         print(symbol,end="")
#     print() 
# phone_number=input("Enter the phone number")
    
#RANDOM NUMBER
# import random
# num=random.randint(10,100)
# print(num)

#PRIME NO IN RANGE
# a=int(input("Enter your lower a: "))
# b=int(input("Enter your upper b: "))
# for i in range(a,b+1):
#     if i==1:
#         print("1 is not a prime no.")
#     if i>1:
#         for x in range(2,i):
#             if i%x==0:
#                 break
#         else:
#             print(f"{i}")

#PRIME NUMBER
# a=int(input("Enter your a: "))
# total=1
# for x in range(2,a+1):
#     b=a%x
#     if b==0:
#        total+=1
# if total==2:
#     print(f"{a} is prime number")
# else:
#     print("not prime")    

#ODDEVEN
# a=int(input("Enter your no.: "))
# if a%2==0:
#     print("even")
# else:
#     print("odd")    

#LEAP YEAR
# a=int(input("Enter your year: "))
# if (a%4==0 and a%100!=0) or a%400==0:
#     print("leap yaer")
# else:
#     print("not a laep year")    

#FACTORIAL
# a=int(input("Enter your number a: "))
# if a<0:
#     print(f"factorial of {a} does not exist")
# else:
#     factorial=1
#     for i in range(1,a+1):
#         factorial*=i
#     print(factorial)        

#FIBONACCHI 
# num=int(input("Enter your number: "))
# a=0
# b=1
# if num==1:
#     print(a)    
# else:
#     print(a)
#     print(b)
#     for i in range(0,num+1):
#         c=a+b
#         print(c)
#         a=b
#         b=c

#        MULTIPLE INPUTS

# inputs = input("Enter integers and strings separated by space: ").split()
# integers = [int(x) for x in inputs if x.isdigit()]
# strings = [x for x in inputs if not x.isdigit()]
# print("Integers:", integers)
# print("Strings:", strings)

#BILLING ORDER
# menu={"pizza":200,
# "chips":30,"wet corn":70,
# "popcorn":500,"soda":100,
# "samosa":70}
# cart=[] 
# total=0
# print("--------MENU--------")
# for keys, values in menu.items():
#     print(f"{keys:10}: ${values:.2f}")
# print("--------------------")    
# while True:
#     order=input("Enter your order(press q to quit):").lower()
#     if order=="q":
#         break
#     elif menu.get(order) is not None:
#             cart.append(order)
# print("--------------")    
# for order in cart:
#     total=total+menu.get(order)
#     print(f"{order:8}"+":$"+str(f"{menu.get(order):.2f}"))
# print("--------------")        
# print(f"Total   :${total:.2f}")
# print()
# print("****Thank You****")
    
#ROCK PAPER SCISSORS
# import random
# options=("rock","paper","scissors")
# player=None
# computer=random.choice(options)
# print("***** Rock Paper Scissors *****")
# print("        👊    👋     ✌")
# print()
# print("#Let's Play")
# print()



# while True:
#     player=None
#     computer=random.choice(options)
#     while player not in options:
#         player=input("Enter your choice:")
#     print("-----------------------")    
    
    
#     print(f"player choice  : {player}")
#     print(f"computer choice: {computer}")
#     if  player==computer:
#         print("it's a tie!")
#     elif player=="paper" and computer=="rock":
#         print("you win!")
#     elif player=="scissors" and computer=="paper":
#         print("you win!")
#     elif player=="rock" and computer=="scissors":
#         print("you win!")
#     else:
#         print("you lose! \a")
    
#     play_again=0
#     ooo=("y","n")    
#     while play_again not in ooo:
#         play_again=input("Do you want to play again(y/n):")
#     if play_again=="y":
#         print("--------------------------------")
#         print()
#         continue
#     elif play_again=="n":
        
#         print("""***Thanks for playing***""")         
#         break
           

#BINARY CONVERSION
# decimal=int(input("Enter your number: "))
# print("the conversion of ", decimal,"number is:  ")
# print(bin(decimal)," in binary")
# print(oct(decimal)," in octal")
# print(hex(decimal)," in hexadecimal")


#FACTORS OF A NUMBER
# num=int(input("Enter your number: "))
# factors=[x for x in range(1,num+1) if num%x==0]
# print(factors)

#PALINDROME NUMBER
# string=input("Enter your string: ")
# # list=list(string)
# # rev=list[::-1]
# if list(string)==list(string)[::-1]:
#     print("The given string is palindrome:",string)
# else:
#     print("The given string is not palindrome:",string)


# string=input("Enter your string: ")
# if string==string[::-1]:
#     print("The given string is palindrome:",string)
# else:
#     print("The given string is not palindrome:",string)

#REMOVING PUNCTUATION
# string=input("Enter your string: ")
# # list=list(string)
# # rev=list[::-1]
# if list(string)==list(string)[::-1]:
#     print("The given string is palindrome:",string)
# else:
#     print("The given string is not palindrome:",string)


# string=input("Enter your string: ")
# if string==string[::-1]:
#     print("The given string is palindrome:",string)
# else:
#     print("The given string is not palindrome:",string)



#SORT WORDS IN ALPHABETICAL ORDER
# list=["zubiya","nihal","kadar","numair","maaz","moeez"]
# print(sorted(list))

# str=input("Enter your string: ")
# ord=[x for x in sorted(str.split())]
# print(' '.join(ord))


    
 
    
        

