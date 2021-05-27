x = int(input("Please enter a number: "))
y = int(input("Please enter a number: "))
op = input("Please enter an operation (+,-,*,/): ")
if op=="+":
    print("{0}{1}{2}={3}".format(x,op,y,x+y))
elif op=="-":
    print("{0}{1}{2}={3}".format(x,op,y,x-y))
elif op=="*":
    print("{0}{1}{2}={3}".format(x,op,y,x*y))
elif op=="/":
    print("{0}{1}{2}={3}".format(x,op,y,x/y))
else:
    print("invalid operation")
