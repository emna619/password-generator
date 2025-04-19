#strong password generator
# 1- import string moduel 
# 2- stor all character in lists ( upper/ lower case digistes, punctuation )
# 3- take number of character form user
# 4- make sure the number of character is 6 or more 
# 5- shuffle all lists
# 6- calculate 30% AND 20% of number of  character
# 7- creat password 60% letters and 40% digits and punctuation
import string
import random

s1 = list ( string. ascii_lowercase)
s2 = list ( string.ascii_uppercase)
s3 = list ( string.digits)
s4 = list ( string.punctuation)

character_number = input (' how many  character for the password ?:' )  
while True:
      try:
          character_number = int (character_number)      
          if  character_number< 6 :
            print ('you need at least  6 characters ')
            character_number =input('how many character for the pasword?:')
          else: 
                break 
      except:
             print('pleas enter numbers only')
             character_number =input('how many character for the pasword?:')

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round (character_number * (30/100 ) ) # التقريب round 
part2 = round (character_number * (20/100 ))

password = []


for i in range(part1):
  password.append(s1[i])
  password.append(s1[i])

for i in range(part2):
  password.append(s3[i])
  password.append(s4[i])

random.shuffle(password)

password = "".join(password[0:])

print (password)


                        
       

 
           
        




