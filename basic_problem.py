################################
# for loop
# total=0
# home = ["men", "women", "children", "fan", "ac"]
# for item in home:
#     print(item)
# total=total+item

######################################
# item=[1,2,3,4,5,6,7,7,7,88,8,889,9,54]
# for i in range(len(item)):
#     print(len(item))
#     break    #14
#
# print("Hi")
# print(len(item))
#######################################

# x = 5
# y = 6
# print("Hi",x,y,"Bye")

#######################################
# writing function to check
day1_expense = [22, 33, 44, 55, 66, 66, 77]
day2_expense = [11, 22, 33, 44, 55, 66]


# counting expense using function

def total_expense(exp):
    total = 0
    for money in exp:
        total = total + money
    return total


day1 = total_expense(day1_expense)
day2 = total_expense(day2_expense)

print("DAY 1 Expenses:", day1)
print("DAY 2 Expenses:", day2)

#######################################
#combining two ranges using range
from itertools import chain

res = chain(range(10), range(10, 21))
for i in res:
    print(i)

#######################################
