'''A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a password generator 
application using Python, allowing users to specify the length and complexity of the password.
User Input: Prompt the user to specify the desired length of the password.
Generate Password: Use a combination of random characters to
generate a password of the specified length.
Display the Password: Print the generated password on the screen.'''


import random
n = int(input())
low_case = chr(random.randint(97,122))
upp_case = chr(random.randint(65,90))
num_case = str(random.randint(1,100))
res = low_case+upp_case+num_case

l = []
for i in range(n):
    char = random.choice(res)
    l.append(char)
    
new_res = ''.join(l)
print(new_res)
    
