#1 hello world program

# print("hello world")


# 2 variable

# name="devansh"
# age=40
# marks=80.8
# print(name)
# print(age)
# print(marks)

# name="a"
# Name="b"
# naMe="c"
# NAM="d"
# n_a_m_e="e"
# _name="f"
# name_="g"
# na76me="f"
# print(name,Name,naMe,NAM,n_a_m_e,_name,name_,na76me,)

# x=y=z=50
# print(x)
# print(y)
# print(z)

# a,b,c=78,89,90
# print(a)
# print(b)
# print(c)

# local variable

# declaration  a function
# def add():
#     # local variable
#     a=20
#     b=40
#     c=a+b
     
# add()
# print(a)// generate  error



# global variable
# we can use global variables inside our outside the function
# x=500
# def mainfunction():
#     global x
#     print (x)
#     x="welcome ajit"
#     print(x)
# mainfunction()
# print (x)


# delete variable
# x=78
# print(x)
# del x
# print (x)


# maximum possible values of ineger in python
# x=56000000000000000000000000000000000000000000000000000000
# x=x+1
# y=9.7
# print(type(x))
# print(type(y))
# print(x)
# print(y)


# data type
# a=59
# b="hello ajit "
# c=9.98
# print(type(a))
# print(type(b))
# print(type(c))

# standard data type are
# numbers=integer,float,complex
# sequence type=string,list,tuple
# boolean
# set
# dictionary


# numbers
# r=8
# o=9.98
# t=1+3j
# print(type(r))
# print(type(type(o)))
# print(type(t))

# string
# str="welcome to ajit "
# print(str)

# list
# list1=[1,"ajit",8.9]
# print(type(list1))
# print(list1)

# tuple
# tup=(34,"ajit",8.89)
# print(type(tup))
# print(tup)


# dictionary
# d={1:"ajit",2:"kumar",3:"bisen"}
# print(d.keys())
# print(d.values())
# print(d)

# set
# set1=set()
# set2={"ajit",4,"bisen",45}
# print(set2)


# keyword
# import keyword
# print(keyword.kwlist)

# operator
# 1 arithmatic
# a=7
# b=6
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)


# 2 assignment
# a=70
# b=40
# a=a+b
# print(a)

# 3 comparision operator
# a=7
# b=9
# print(a==b)
# print(a!=b)
# print(a>=b)
# print(a<=b)
# print(a<b)
# print(a>b)

# 4 logical operator
# x=5
# print(x>3 and x>2)
# print(x>7 and x>2)
# print(x>3 or x>2)
# print(x<4 or x<6)
# print(not(x>3 or x>2))


# 5 identity operators
# it is used to compare the objects;
# 1)is=return true if both variables are the same object
# 2) is not=return true if both variables are  not the same object


# x=["apple","bananas"]
# y=["apple","bananas"]
# z=x
# print(x is z)
# print(x is y)
# print(x==y)


# x=["apple","bananas"]
# y=["apple","bananas"]
# z=x
# print(x is not z)
# print(x is not y)
# print(x!=y)


# 6 membership operators
# it is used to test sequence is presented in an object
# in=return true if a sequence with the specified value is present in the object
# not in=return true if a sequence with the specified value is not present in the object
# x=["apple","banana"]
# print("banana" in x)
# print("papaya" not in x)


# 7 bitwise operator
# it is used to compare binary numbers
# &(and),|(or),^(xor),~(not),<<(zero fill lef shift),>>(signed right shift)

# taking input
# name=input("what is your name")
# print( "my name is"+  name)


# type conversion
# old_age=input("enter your age ")
# new_age= (old_age)+2 //error
# new_age= int(old_age)+2
# print(new_age)


# useful conversion functions
# float()
# bool()
# str()
# int()


# a= int(input("enter fist number "))
# b=  int(input("enter second number "))
# sum=a+b
# print(sum)
 
# if-else statement 
# a=int(input("enter a number"))
# if(a%2==0):
#     print( "it is even")
# else:
#     print("it is odd")    

# a=int(input("enter  fist number"))
# b=int(input("enter  second number"))
# c=int(input("enter third number"))
# if a>b and a>c:
#     print("a is greater")
# if b>c and b>c :
#     print("b is greater ")   
# else:
#     print ("c is greater")


# num=int(input("enter a number"))
# if num>33 and num<=45:
#     print("d grade")
# elif num>45 and num<60:
#     print("e grade")
# elif num>60 and num<75:
#     print("b grade")
# elif num>=75 and num<90:
#     print("a grade")
# elif num>=90 and num<=100:
#     print(" a+ grade")                
# else:
#     print("fail")    


# range function()
# x=range(5)
# for num in x:
#     print(num)


# loops
# 1)while
# i=1
# while(i<=5):
#     print(i)
#     i=i+1

# i=1
# while(i<=5):
#     print(i*"*")
#     i=i+1


# 2)for loop
# for i in range(5):
#     print(i)
#     i=i+1

# break and continue
# students=["ram","kam","ajit","lucky","sonu"]
# for student in students:
#     if student== "lucky":
#         continue
#         # break
#     print(student) 




# string in depth




# string example pyhton

# a="i love you ajit"
# print (a)

# access string character 

# a="hello"
# print(a[1])
# negative indexing
# a="hello"
# print(a[-4])

#  slicing =access a range of character in a string by using the slicing  operator colon:
# a="hello"
# print(a[1:4])

# note =python string are immutable

# operations

# a="hello ajit,"
# b=" i love you ajit"
# c="hello ajit"
# # comparision
# print(a==b)
# print(a==c)
# # join
# result=a+b
# print(a+b)
# # lenght
# print(len(a))
# print(a.upper())
# print(a.lower())
# replaced_a=a.replace('h','c')
# print(replaced_a)
# print(a.find('t'))
# print(a.split(' '))
# print(a.index("ajit"))



# list
# num=[1,3,6,8,8.9,9,0,9]
# aj=[4,6,7,9,3,]
# print(num)

# print(num[0])//access
# print(num[1])
# print(num[2])
# print(num[-1])
# print(num[-3])

# print(num[0:2])//slicing
# print(num[3:6])

# num.append(88)
# print(num)

# num.extend(aj)
# print(num)


# num[2]=4
# print(num)


# del num[1]
# print(num)


# num.remove("hii")
# print(num)

# num.insert(1,9)
# print(num)


# num.pop(0)
# print(num)


# num.clear()
# print(num)

# num.sort()
# print(num)

# num.reverse()
# print(num)

# num.copy()
# print(num)


 
# print(len(num))



#  tuple
# a=(1,2,3,4,6,"hii",9.6,3,3,3,)
# print(a)
# b=(2,4,5,6,[3,4,5,6],(7,8,9))
# print(b)
# c="ajit"
# print(c)

# access
# print(a[0])
# print(a[3])

# slicing

# print(a[2:5])   
# print(a[ 3:])
# print(a[:])



# methods
# print(a.count(3))
# print(a.index(4))


# set

# a={1,2,3,4,}
# print(a)
# b={4,5,(5,6,7)}
# print(b)

# a.add(8)
# print(a)

# a.update([3,5,7,6])
# print(a)

# a.update({44,55,66},[77,88,99])
# print(a)


# a.discard(4)
# print(a)
# a.remove(3)
# print(a)


 
# print(a.pop())


# a={1,2,3,4,5}
# b={4,5,6,7}
# print(a|b)
# print(a&b)
# print(a-b)
# print(a^ b)



# dictionary
# a={"ajit":"bisen","shubham":"choudhary","lalith":"thakre"}
# b={1:"ajit",2:"tushar",3:"vikash"}
# print(a)
# print(b)

# add element
# a["aakash"]="bisen"
# print(a)
 
#  access element
# print(a["ajit"])

# removing element
# del a["shubham"]
# print(a)








