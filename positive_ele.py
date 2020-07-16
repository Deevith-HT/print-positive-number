#output is printed as individual elements(not in a list)
n = list(map(int, input('Enter numbers: '). split()))
for i in n:
    if i>=0:
        print(i, end=",")
        
print()
