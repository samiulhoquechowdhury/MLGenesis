#string
str1 = "This is a \n string" #\n is a escape sequence
str2 = 'This is another string'
srt3 = """This is also a string"""

print(str1)

#Different operation on string
#Concatenation

print(str1 + " " +str2)


#lenght of string
print(len(str1));

#indexing
#we can access element through indexing but cannot update it.

print(str1[2])

#Slicing ==> accessing part of string

print(str1[0:4])
print(str1[9:len(str1)])

#Negative indexing
word = "apple"
print(word[-3:-1])
print(word.endswith("le"))
print(word.capitalize())
print(word.replace("a", "m"))
print(word.find("l")) #return index of the character
print(word.count("p")) # count the time of occurence.
print(word.upper())