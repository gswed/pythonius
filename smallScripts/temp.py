numbers=[1,2,3]
file = open("numbers.txt", "w")
for nr in numbers:
    file.write(str(nr)+"\n")
file.close()
