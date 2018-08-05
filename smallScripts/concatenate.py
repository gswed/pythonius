import glob2
import datetime

timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

files=[]
for fileName in glob2.glob("*.txt"):
    if "file" in fileName:
        files.append(fileName)

with open(timestamp+".txt", "w") as file:
    for p in files:
        f=open(p, "r")
        c=f.read()
        file.write(c+"\n")
        f.close()
