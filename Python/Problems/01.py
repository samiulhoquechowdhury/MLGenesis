# #Add two numbers

# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))

# result = num1 + num2
# print("The sum is:", result)


# #Find the largest number

# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# num3 = int(input("Enter the third number:"))

# largest = max(num1, num2, num3)
# print("The largest number is:", largest)



# #Check even or odd

# num = int(input("Enter a number:"))

# if num % 2 == 0:
#     print("EVEN NUMBER.")
# else:
#     print("ODD NUMBER")





# #cHECK OF LEAP YEAR

# year = int(input("Enter a year:"))

# if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")






# #REVERSE A STRING

# string = input("Enter a string:")

# reversed_string = string[::-1]
# print("Reversed string:", reversed_string)




# #Factorial of a number

# # Input a number
# num = int(input("Enter a number: "))

# # Find factorial using a loop
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i

# print(f"The factorial of {num} is {factorial}.")





# #DATA STRUCTURE(LISTS, TUPLE, DICTIONSARIES, SETS)





# #CREATE A LIST AND ACCESS ELEMENT

# number = [10, 20, 30, 40, 50]

# print("First Element", number[0])
# print("Second Element", number[1])



# #ADD OR REMOVE ELEMENT FROM LIST

# number = [12, 23, 45, 5677, 823]
# print("Original List:", number)

# number.append(120)

# print("After adding an element",number)

# number.remove(12)
# print("After removing an Element:", number)





# #Sort a list

# numbers = [3,6,78,9,34,1,6]

# numbers.sort()
# print("Sorted List:", numbers)






# #tuple
# my_tuple = (1,3,4,6,8,9,12)

# lenght = len(my_tuple)
# print("Length of my tuple is:",lenght)




#convert list to a tuple

# my_list = [12,34,12,56,76]
# my_tuple = tuple(my_list)

# print("Tuple:", my_tuple)




#Add a key value pair in dictionary

# person = {'name':'samiul', 'city':'guwahati'}

# person['age'] = 25

# print("Updated dictionary", person)





# #7. Check If a Key Exists in a Dictionary

person = {'name':'Samiul','city':'guwahati'}

if 'name' in person:
    print("Key 'name' exist is dict")
else:
    print("Key 'name' doesnot exist in the dict")

