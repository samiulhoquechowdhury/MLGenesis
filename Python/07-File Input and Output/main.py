#opening a file

file = open("example.txt", "r")
content = file.read()

print(content)
file.close()