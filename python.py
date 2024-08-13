# rows=4
# num=1
# for i in range(1,rows+1):
#     for j in range(i):
#      print("*",end=" ")
#     num+=1
#     print()    

# for i in range(0,4):
#     print(' ' *(4-i-1) +'*'*(2*i+1))
    
# for i in range (4-2,-1,-1):
#     print(' ' * (4-i-1)+'*' * (2*i+1))  
    
# for i in range (1,6):
#     for j in range(1,6-i):
#         print(" ",end=" ")
#     for j in range(1,(2*1-1) +1):
#         print("*",end=" ")     
#     print()    
# for i in range(5,0,-1):
#     for j in range(1,6-i):
#         print(" ",end=" ")
#     for i in range(1,i+1):
#         print("*" ,end=" ")
#     print() 
#     n=4
#     for i in range(1,n+1):
#         num+1
# n=5
# fact = 1
# i=1
# while i <=n:
#     fact *= i
#     i+=1
#     print("total fact =",fact)
#     def calc_sum(a,b):
#         sum = a+b
#         print(sum)
#         return sum
    # calc_sum(5,10)
    # calc_sum(6,10)
    # calc_sum(5,1
# def show(n):
#   if(n==0):
#     return
#   print(n)
#   show(n-1)
# show(5)
# def fact(n):
#   if(n==1 or n==0):
#     return 1
#   return fact(n-1) * n
# print(fact(9))
# for i in range(1,5):
#     for j in range(1,5-i):
#         print("",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(3,0,-1):
#     for j in range(1,5-i):
#         print("",end=" ")
#     for j in range(i):
#         print("*",end=" ")  
#     print() 
# for i in range(1,5) :
#     for j in range(i) :
#         if i==1:
#             print("@",end=" ") 
#         if i==2:
#             print("#",end=" ") 
#         if i==3:
#             print("$",end=" ")
#     print() 
# for i in range(1,5):
#     for j in range(1,5-i):
#         print("",end=" ")
#     for j in range(i):
#         print("*",end=" ") 
#     print()
# for i in range(3,0,-1):
#     for j in range(1,5-i):
#         print("",end=" ")
#     for j in range(i):
#         print("*",end=" ") 
#     print()
# for i in range(1,6):
#     for j in range(1,6) :
#         print("*",end=" ")
# n=6
# for i in range(n,0,-61):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
# n=int(input("enter a namber"))
# for i in range(1,6+1):
#     for j in range(1,6+1):
#         if i==1 or i==6 or j==1 or j==6:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ") 
#     print() 
# print(("_________register__________"))
# user=input("enter the use name:")
# password=input("enter the password:")
# print("__________loging________")
# user1=input("enter the use name again:")
# if user1 == user:
#     password1 = input("enter the password")
#     if password1 == password: 
#       print("welcome")  
#     else:
#      print("password is wrong") 
# else:
#   print("user1 name is worng") 
# a=2
# b=3
# print(a==b)
# print(a!=b)
# print(a>=b)
# print(a<=b)
# first=int(input("ente the first number:"))
# second=int(input("enter the second number:"))
# print("sum=",first+second)
# str1="govind"
# str2="yadav"
# print(str1+str2)
# print(len(str1+str2))
# list=[1,3,2,5]
# list.append(4)
# print(list)
# list=[1,2,3,4,]

# list.sort(reverse=True)  # Sorts the list in place in descending order
# print(list)

# for i in range(1,5):
#     for j in range(5-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(3,0,-1):
#     for j in range(5-i):
#         print("",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print() 
# list=["python","govind",1,2,3,4]   
# list.append("rohit")
# print(list)
# list.remov
# imfo={
#     'name':'gobhi',
#     'class':9,
#     'food':{
#         'gulabjamun':230,
#         'panir':240,
#         'tatti':"100kg",
#         'tatti':150,
#     }
# }
# # print(imfo) 
# name= "govind"
# f=name(0)
# print(f)
# a=[0,1,2,3,4,5,6,7,8,9]
# c=0
# for i in a:
#     c+=i
#     print(c,end=" ")
# num={1,2,3,4,5,}
# num1={5,6,7,2,}
# print(num.union(num1))
# print(num.intersection(num1))
# i=1
# while i<=10:
#     c=i*2
#     print(c)
#     i+=1
# n= int=int(input("enter a number")) 
# if n<10000:
#     print("eligible") 
# else:
#     print("not eligible") 
# mini project in python
menu={
    'pizza':150,
    "pasta":200,
    "bauger":120,
    "coffee":10,
}
print("welcome  to restaurant") 
print("pizza:Rs150\npassta: Rs200\nbauger: 120\ncoffee: 10") 
order_total = 0

item_1= (input("enter the name of item you want to order = ")) 
if item_1 in menu:
    order_total += menu[item_1]  
    print(f"your item {item_1} has been added to your order")

else:
    print(f"order item {item_1} is not avaialable yet")

another_order = input("do you want to add another item? (Yes/NO)") 
if another_order =="Yes":
    item_2= input("enter the name of item you want to order = ")
    if item_2 in menu:
        order_total += menu[item_2]  
        print(f"your item {item_2} has been added to your order")

    else:
        print(f"order item {item_2} is not avaialable yet")
print(f"the total amount of item is {order_total}")

