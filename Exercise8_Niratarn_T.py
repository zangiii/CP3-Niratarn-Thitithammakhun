UsernameInput = input("username = ")
PasswardInput = int(input("passward = "))
if UsernameInput == "A" and PasswardInput == 1234 :
    print("------ Welcome to SAIFAH COFFEE SHOP ------")
    print("Menu Drinks")
    print(" Americanos              $6 ")
    print(" Decaf Pike Place        $6 ")

    UsernameSelected = input("Add your order here ")
    if UsernameSelected == "Americanos" :
        Quantitty = int(input("Quantitty = "))
        result1 = Quantitty*6
        print("your orders is",Quantitty, "x",  UsernameSelected, "=" ,"$",result1  )
        Usernameordermore = input(" Anything else ? ")
        if Usernameordermore == "yes":
            UsernameSelected2 = input("Add your order here ")
            if UsernameSelected2 == "Decaf Pike Place" :
                Quantitty2 = int(input("Quantitty = "))
                result2 = Quantitty2 *6
                print("your orders is", Quantitty2, "x", UsernameSelected2, "=", "$", result2)
                print(" your totol is", "$", result1 + result2)
                print(" --- THANK YOU ---")
        else:
            print(" your totol is","$", result1 )
            print(" --- THANK YOU ---")
    else:
        Quantitty = int(input("Quantitty = "))
        print("your orders is", Quantitty, "x Decaf Pike Place" , "=", "$", Quantitty * 6)
        print(" your totol is", "$", Quantitty * 6)
        print(" --- THANK YOU ---")




