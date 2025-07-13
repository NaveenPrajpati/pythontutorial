
a=open('file.txt')
txt=a.read()
print(txt)
a.close()

b=open('file.txt','w')
b.write('this is inserted text')
b.close()
b=open('file.txt','+a')
b.write('this is inserted text 2')
b.close()


with open('file.txt','r') as f:
    print(f.read())