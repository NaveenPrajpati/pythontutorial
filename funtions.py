def addNumber(a,b=6):
    print(f'addition {a+b}')
    return a+b


 
print('return value: ',addNumber(2,3))
 
def sumnumber(n):
    if(n==1):
        return 1
    return n+ sumnumber(n-1)

print(sumnumber(4))