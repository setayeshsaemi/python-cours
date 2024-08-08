x = int(input('enter your number: '))
binary = ''
while True:
    r=x%2
    x=x//2
    binary = binary+str(r)
    if(x==0):
        break
print(binary)