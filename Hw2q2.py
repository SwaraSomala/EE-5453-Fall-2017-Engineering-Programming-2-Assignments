elective= {'2CPR2B': 'C Language','1UNX1B': 'Intro to UNIX','3SH414':'Shell Programming','4PL400':'Perl Programming'}  # Create elective hash  keys = elective.keys()
for key in sorted(elective.keys()):   #Sorting of Hash by key(sorting dictionary by key)
 print(key,'=>',elective[key])        #Printing the sorted hash in the format key =>value
while(key!='-1'):                    #Sentinel Control using while loop
 key=input("Enter the code number for the course you plan to take this semester? (Enter -1 to exit)")
 if key in elective.keys():
  print("You will be taking",elective[key],"this semester")   #Outputs the course name for the key entered
 elif (key=='-1'):
  break;        #Comes out of loop if value entered is -1
 else:
     print("Enter a valid course code")

    
    
