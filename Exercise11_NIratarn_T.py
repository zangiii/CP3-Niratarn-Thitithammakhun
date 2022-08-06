numberInput = int(input("number = "))
for x in range(numberInput) :
    y = x+1
    z = (" "*(numberInput-x)+"*"*((x*2)+1))
    print(z)