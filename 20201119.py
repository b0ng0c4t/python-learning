#Given a two list of equal size create a set such that it shows the element from 
# both lists in the pair
print("EXERCISE 1")
firstList = [2,3,4,5,6,7,8]
print('First List:', firstList)
secondList = [4,9,16,25,36,49,64]
print('Second List:', secondList)
result = zip(firstList, secondList)
resultSet = set(result)
print(resultSet) 
print('\n')

#Given a following two sets find the intersection and remove those
# elements from the first set
print('EXERCISE 2')
firstSet = {23,42,65,57,78,83,29,13}
secondSet = {57,83,29,67,73,43,48,14}
print('first set:', firstSet)
print('Second set;', secondSet)

intersection = firstSet.intersection(secondSet)
print('Intersection is ', intersection)
for item in intersection:
    firstSet.remove(item)

print('First set after removing common element;', firstSet)
print('\n')

#Given a two integer numbers return their product and  if the product is greater 
# than 1000, then return their sum
print('EXERCISE 3')
def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

result = multiplication_or_sum(20, 40)
print("The result is", result)
print('\n')

#Given a range of first 10 numbers, Iterate from start number to the end number 
# and print the sum of the current number and previous number
print('EXERCISE 4')
def sumNum(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print("Current number is", i, "Previous Number is", previousNum, "Sum", sum)
        previousNum = i

print("Printing current and previous number sum in a given range (5)")
sumNum(5)
print('\n')

#Given a string and an integer number n, remove characters from a string starting 
# from zero up to n and return a new string
print('EXERCISE 5')
def removeChar(str, n):
    return str[n:]

print('removing n number of chars')
print(removeChar("pynative", 2))
print('\n')

#Given a list of numbers, return True if first and last number of a list is same
print('EXERCISE 6')
def sameLast(numberList):
    print('Given list is ', numberList)
    firstElement = numberList[1]
    lastElement = numberList[-3]
    if (firstElement == lastElement):
        return True
    else:
        return False
numList = [10, 20, 20, 40, 10]
print("Result is", sameLast(numList))
print('\n')

#Given a list of numbers, Iterate it and print only those numbers which are 
# divisible of 5
print('EXERCISE 7')
def findDivisible(numberList):
    print("Given list is", listNum)
    print('Divisible of 5 in a list')
    for num in listNum:
        if(num % 5 == 0):
            print(num)
listNum = [10,20,30,46,22]
findDivisible(numList)
print('\n')

#Return the total count of sub-string “Emma” appears in the given string
print('EXERCISE 8')
print("Emma is a good deverloper because Emma is a writter")
sampleStr = "Emma is a good deverloper because Emma is a writter"
cnt = sampleStr.count("Emma")
print('the string Emma appears :', cnt)
print('\n')