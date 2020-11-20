#Write a function func1() such that it can accept a variable 
# length of  argument and print all arguments value
print("EXERCISE 1")
def func1(*args):
    for i in args:
        print (i)

func1(20,10,10)
print('\n')

#Write a function calculation() such that it can accept two 
# variables and calculate the addition and subtraction of it. And also it must 
# return both addition and subtraction in a single return call
print("EXERCISE 2")
def calculation(a,b):
    return a+b,a-b
res = calculation(40,10)
print(res)
print('\n')

#Create a function showEmployee() in such a way that it should
#  accept employee name, and it’s salary and display both, and if the salary is
#  missing in function call it should show it as 9000
print("EXERCISE 3")
def showEmployee(name, salary=9000):
    print("Employee", name, "salary is;", salary)

showEmployee('Ben')
showEmployee('Raul', 7000)
print('\n')

#Exercise Question 5: Create an inner function to calculate the addition in the following way
print("EXERCISE 4")
def outerFun(a,b):
    def innerFun(a,b):
        return a+b
    add = innerFun(a,b)
    return add+5

result = outerFun(5, 10)
print(result)
print("\n")

#Exercise Question 6: Write a recursive function to calculate the sum of numbers from 0 to 10
print("EXERCISE 5")
def calculateSum(num):
    if num:
        return num + calculateSum(num-1)
    else:
        return 0

res = calculateSum(11)
print(res)
print('\n')

#Print the following pattern
print("EXERCISE 6")
for num in range(6):
    for i in range(num):
        print(num, end=" ")
    print("\n")

#Reverse a given number and return true if it is the same as the original number
print("EXERCISE 7")
def reverseCheck(number):
    print('original number', number)
    originalNum = number
    reverseNum = 0
    while (number > 0):
        reminder = number % 10
        reverseNum = (reverseNum * 10) + reminder
        number = number // 10
    if (originalNum == reverseNum):
        return True
    else:
        return False
print("The original and reverse number is the same; ", reverseCheck(121))
print("\n")

#Given a two list of numbers create a new list such that new list should 
# contain only odd numbers from the first list and even numbers from the second list
print("EXERCISE 8")
def mergeList(listOne, listTwo):
    print('List 1 is :', listOne)
    print('List 2 is :', listTwo)
    thirdList = []

    for num in listOne:
        if (num % 2 != 0):
            thirdList.append(num)
    for num in listTwo:
        if (num % 2 == 0):
            thirdList.append(num)
    return thirdList

listOne = [10, 13, 1222, 57, 550]
listTwo = [33, 70, 5567, 44, 33]

print("result list is :", mergeList(listOne, listTwo))
print("\n")

