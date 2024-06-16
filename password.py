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
    