#Assign a different name to function and call it through the new name
print('EXERCISE 1')
def displayStudent(name, age):
    print(name, age)
displayStudent('Emma', 26)

showStudent = displayStudent
showStudent('Lucas', 15)
print('\n')

#Generate a Python list of all the even numbers between 4 to 30
print('EXERCISE 2')
print(list(range(4,30,2)))
print('\n')

#Return the largest item from the given list
print('EXERCISE 3')
aList = [4, 6, 8, 245, 244, 22]
print(max(aList))
print('\n')

#Given a two list. Create a third list by picking an odd-index 
# element from the first list and even index elements from second.
print('EXERCISE 4')
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = list()

oddElements = listOne[1::2]
print('Element at odd-index positions from list one')
print(oddElements)
EvenElements = listTwo[0::2]
print('Element at even-index positions from list two')
print(EvenElements)
print('Printing Final third list')
listThree.extend(oddElements)
listThree.extend(EvenElements)
print(listThree)
print('\n')

#Given an input list removes the element at index 4 and add 
# it to the 2nd position and also, at the end of the list
print('EXERCISE 5')
sampleList = [34,54,67,89,11,43,94]

print('Original list:', sampleList)
element = sampleList.pop(4)
print("List After removing element at index 4 ", sampleList)
sampleList.insert(2,element)
print('List after adding element at index 2 ', sampleList)
sampleList.append(element)
print("List after adding element at last ", sampleList)
print('\n')

#Given a two list of equal size create a set such that it shows the element from 
# both lists in the pair
print("EXERCISE 6")
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
print('EXERCISE 7')
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