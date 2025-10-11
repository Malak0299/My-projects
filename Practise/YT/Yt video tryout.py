#x = input("WHat is your name ")

#with open ('file.txt', 'w') as MyFile:
 #   MyFile.write(x)


with open ('file.txt', 'r') as AFile:
    lines = AFile.readlines()
    for name in lines:
        num = name.split (' ')[1]
        print(num)
    