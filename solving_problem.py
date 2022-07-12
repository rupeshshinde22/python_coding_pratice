# print("Hello world")

###     Calculate the multiplication and sum of two numbers
#  CONDITION : Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

# x = int(input("Enter first number : "))
#
# y = int(input("Enter second number : "))
#
# # print(x*y)
# if x * y <= 1000:
#     print("Product is : ", x * y)
# else:
#     print("Sum is ", x + y)

######################################
# Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.


# range_ = int(input("Enter yor range till what range you want to print"))
# for cur in range(range_):
#
#     if cur == 0 or cur == 1:
#         pre = 0
#         print("Current :", cur, "  Previous :", pre, "  Sum :", cur + pre)
#     else:
#
#         pre = cur - 1
#         print("Current :", cur, "  Previous :", pre, "  Sum :", cur + pre)

######################################

# Print characters from a string that are present at an even index number

#
# # accept input string from a user
# word = input('Enter word ')
#
# # get the length of a string
# size = len(word)
# print("Length :",len(word))
#
# print("Printing only even index chars")
# for i in range(0, size , 2):
#     print("index[", i, "]", word[i])

# or

# word = input('Enter word ')
# print("Original String:", word)
#
#
# x = list(word)
# for i in x[0::2]:
#     print(i)


# data = input("Enter any word ")
#
# x = list(data)
# for i in range(len(data)):
#     print(data[i])

######################################

# Dictionary (key and value)

# data = {"a": "apple", "e": "egg", "b": "bat", "james": 123, 456: "james"}
# print(data)

# data["name"]="Champ" #add into dictionaries

# for i in data:
#  print("#",i) #==> this will print key data

# print(data.get(i)) #==>  this will print value data

# print(data.keys()) #==>dict_keys(['a', 'e', 'b', 'james', 456])
# print(data.values()) #==>dict_values(['apple', 'egg', 'bat', 123, 'james'])

# OR

# for i in data.keys():
#     print(i)
#
# for i in data.values():
#     print(i)

## key value

# data = {"a": "apple", "e": "egg", "b": "bat", "james": 123, 456: "james"}
#
# for k,v in data.items():
#     print("key:",k,"value:",v)

"""if you want to clear the data like key and values everything
just do
data.clear()"""

################################################
# Check if the first and last number of a list is the same
# data=list(input("Enter list of any thing : "))
#
# #data = [1, 23, 34354, 4565, 656, 545, 3, 452, 3, 0]
#
# if data[0] == data[-1]:
#     print("The first number and last number are same")
# else:
#     print("The first number and last number are not same")

################################################

## Check if the first and last number of a list is the same
# using function

# data = input("Enter list of any thing : ")


# data = [1, 23, 34354, 4565, 656, 545, 3, 452, 3, 0]
# data = []
# data = [item for item in input("Enter the list items : ").split(",")]  ##how to take data n store in string
#
# #print(data)
# def check_list(data):
#     #print(data)
#     if data[0] == data[-1]:
#         #print("The first number and last number are same")
#         print("True")
#     else:
#          #print("The first number and last number are not same")
#          print("False")
#
#
#
# check_list(data)


### storing string into list
# data = []
# data = [item for item in input("Enter the list items : ").split(",")]
# print(lst1)

################################################
# Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

str = input("Enter the word : ")
char_del = int(input("How much starting digits you want to delete : "))
# con_list=[item for item in str.split(",")]
con_list = list(str)
# print(con_list)
del con_list[0:char_del]
# str1=str(con_list)
str1 = ""
# data = [item for item in con_list.split(",")]
data = str1.join(con_list)
print(data)

################################################

import circle_functions as circle

area = circle.diameter_circle(2)
print(area)

################################################
