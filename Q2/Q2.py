number = int(input("Please enter a decimal number: "))
binary=[]
while number>0:
    binary.append(number%2)
    number=int(number/2)
binary.reverse()
print('The equivalent binary number: ',binary)
    
