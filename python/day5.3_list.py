#list 
iteam =["colour", "time", 2 ]
#print(iteam)
#list  function
mark=[90,91,93,95,94,95,92,99,100 ]
print(mark[0:])
print("length of the  mark ", len(mark))
print("maximum value ",max(mark))
print("minu=imum value ",min(mark))

#list methods
mark.append(80) #add element in last 
print(mark)
mark.sort() #short 
print(" after sorted" ,mark)
mark.reverse()
print(mark)
mark.remove(80) #deleted element 
print(mark)
mark.pop(0) #deleted element by index 
print(mark)
mark.insert(0,80)
print(mark)