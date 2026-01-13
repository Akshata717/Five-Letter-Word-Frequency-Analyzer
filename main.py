hashTable = {
'.' : " ",
'?' : " ",
'!' : " ",
',' : " ",
'-' : " ",
'_' : " ",
'(' : " ",
')' : " ",
'[' : " ",
']' : " ",
':' : " ",
';' : " ",
'/' : " ",
'\'': " ",
'`': " ",
'"': " "
}

readFile=open("input.txt") 
outFile=open("output.txt",'w') 

for line in readFile:     
  for char in line: 
   if char in hashTable:
     outFile.write(hashTable[char].lower())
   else:
     outFile.write(char.lower())


#print(len("hello"))
readFile.close()
outFile.close() 

realcount = 0
x = []
outFile=open("output.txt")
for line in outFile:
  for word in line.split():
    if (len(word) ==5):
    #  print(word)
      realcount +=1
      x.append(word)



for i in range(len(x)):
  for j in range(i+1,len(x)):
    if x[i]> x[j]:
      temp = x[j]
      x[j] = x[i]
      x[i] = temp
print(x)

mode = 0
max = 0
count = 0

for a in range(len(x)):
  for b in range (a+1,len(x)):
    if x[a] == x[b]:
      count +=1
      if count > max:
         max = count
         mode = x[a]
    else:
      count =0


print()
print()
print("the five letter word the appears the most is " + str(mode) + ", it appears "+ str(max) + " times")

print("In total, there are " + str(realcount) + " five letter words")
outFile.close() 
