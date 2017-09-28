Names=['Nick','Susan','Chet','Dolly','Bill']
print (Names) 
Names[1]='Ellie' #a.replace Susan with Ellie
Names[2]='Beatrice' #a.replace Chet with Beatrice
Names.insert(3,'Charles') #a.insert Charles
print(Names)
Names.pop() #b.Using pop function to remove Bill from the array as that element is the last one
print(Names)
Names.append('Lewis')
Names.append('Izzy') #c.Appending Lewis and Izzy (adding them to the end of the array)
print(Names)
Names.pop(0) #d.Remove Nick from the beginning of the array
print(Names)
Names.reverse() #e.Reversing the array
print(Names)
Names.insert(0,'Archie') #f.Inserting Archie to the beginning of the Array
print(Names)
Names.sort() #g.Sorting the array
print(Names)

