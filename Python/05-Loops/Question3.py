#print multiplication table for n input number

number = int(input("Enter a number :"))
print("Multiplication Table of", number)

count = 1
while count <= 10:
    print(number, "X", count, "=",number * count)
    count += 1
print("Happy coding")