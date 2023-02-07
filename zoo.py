#You are required to enter a word that consists of x and y
#that denote the number of Zs and Os respectively. 
#The input word is considered similar to word zoo if 2 * x = y.

#Determine if the entered word is similar to word zoo.
#For example, words such as zzoooo and zzzoooooo are similar to 
#word zoo but not the words such as zzooo and zzzooooo.

#Input format

#First line: A word that starts with several Zs and continues by several Os.
#Note: The maximum length of this word must be 20.
#Output format

#Print Yes if the input word can be considered as the string zoo otherwise, print No.

## my code:
name = str(input())      # Reading input from STDIN
z = 0
o = 0
namelst = []

# Puts given letters into a list
for letter in name:
    namelst.append(letter)

# Finds number of times z and o exist
for i in range(0, len(namelst)):
    if namelst[i] == 'z':
        z += 1
    else:
        o += 1

# Determines similarity to 'zoo'
if (2 * z) == o:
    print("Yes")
else: 
    print("No") # Writing output to STDOUT
    
## More concise code written by user Aniket Jagtap
name = input() # Reading input from STDIN 
#print('Hi, %s.' % name) # Writing output to STDOUT 
if name.startswith("z") and len(name) <= 20: 
  if name.count("z") * 2 == name.count("o"):
    print("Yes") 
  else: 
    print("No") 
        
# notes: 
## no need to put name in a list as strings are already recognized as lists in python
## .count() is a built in python function that does exactly what my for loop did 
