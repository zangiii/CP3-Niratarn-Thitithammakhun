def login():
    UsernameInput = input("username = ")
    PasswardInput = int(input("passward = "))
    if UsernameInput == "A" and PasswardInput == 1234:
        return True
    else:
        return False
def showMenu():
    print("------ Welcome to SAIFAH COFFEE SHOP ------")
    print(" 1. Vat Calculator")
    print(" 2. price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculate(totalPrice):
    vat  = 7
    result = totalPrice + (totalPrice*vat/100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return price1+price2

login()
showMenu()
print("Select Menu")
if menuSelect() == 1:
    print(vatCalculate(priceCalculate()))
else :
    print(priceCalculate())
AnyThingElse = input("Anything else ?(yes or no) :")
if AnyThingElse == "yes" :
    showMenu()
    print("Select Menu")
    if menuSelect() == 1:
        print(vatCalculate(priceCalculate()))
    else:
        print(priceCalculate())
print("----- THANK YOU -----")
