menuLists =[]
priceLists=[]
def showBill():
    print("Your Orders".center(21,"-"))
    for i in range(len(menuLists)):
        print((i+1),menuLists[i],"Price :",priceLists[i])
    print("Total  ",sum(priceLists),"TH")
def selectMenu():
    while True:
        menuName = input("Please Enter You Menu :")
        if menuName.lower() == "done":
            break
        else:
            menuPrice = int(input("Price :"))
            menuLists.append(menuName)
            priceLists.append(menuPrice)
selectMenu()
showBill()
print("THANK YOU".center(21,"-"))
