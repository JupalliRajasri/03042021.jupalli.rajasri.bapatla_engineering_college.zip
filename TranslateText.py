import time
import os
import psutil
start = time.time()
file1 = open("french_dictionary.csv","r+")
mainFile = open("t8.shakespeare.txt","r+")
counter = 0
Words = file1.read()
WordsList = Words.split("\n")
replaceWordLists = []
file1.close()
mainContent = mainFile.read()
for i in WordsList:
    if i:
        replaceWordLists.append(i.split(","))
for j in replaceWordLists:
    num_substrings = mainContent.lower().count(j[0])
    print(j[0],"Count = ",num_substrings)
    mainContent = mainContent.replace(j[0],j[1])
    mainContent = mainContent.replace(j[0].title(),j[1].title())
    mainContent = mainContent.replace(j[0].upper(),j[1].upper())
mainFile.close()
fout = open("data.txt", "wt")
fout.write(mainContent)
fout.close()
end = time.time()
process = psutil.Process(os.getpid())
print("Memory utilized is == ",process.memory_percent())
print(f"Runtime of the program is {end - start}")