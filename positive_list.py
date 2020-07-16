#positive number from parent list are stored in a new list
n = list(map(int, input('Enter numbers: '). split()))
a=[]
for i in n:
    if i>=0:
        a.append(i)
        
print(a)
