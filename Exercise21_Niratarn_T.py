from tkinter import *
import math

def leftClickButton(event):
    wight = float(textBoxWight.get())
    hight = float(textBoxHight.get())
    BMI = wight/((hight/100)**2)
    textBoxBMI1.configure(text=BMI)
    if BMI >= 30.0:
        return  lebelresult.configure(text = "อ้วนมาก")
    elif BMI >= 25.0:
        return  lebelresult.configure(text ="อ้วน")
    elif BMI >= 23.0:
        return lebelresult.configure(text ="น้ำหนักเกิน")
    elif BMI >= 18.6:
        return lebelresult.configure(text ="น้ำหนักพอดี เหมาะสม")
    else:
        return lebelresult.configure(text ="ผอมเกินไป")

mainWindow = Tk()
mainWindow.title("Body Mass Index")
lebelTitle = Label(mainWindow,text="Body Mass Index").grid(row=0,column=0)
lebelHight = Label(mainWindow,text = "ส่วนสูง(cm.)")
lebelHight.grid(row=1,column=0)
textBoxHight = Entry(mainWindow)
textBoxHight.grid(row=1,column=1)
lebelWight = Label(mainWindow,text = "น้ำหนัก(Kg.)")
lebelWight.grid(row=2,column=0)
textBoxWight = Entry(mainWindow)
textBoxWight.grid(row=2,column=1)
calculateButton = Button(mainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=3,column=1)
lebelBMI = Label(mainWindow,text = "ดัชนีมวลกาย (BMI) =")
lebelBMI.grid(row=4,column=0)
textBoxBMI1 = Label(mainWindow)
textBoxBMI1.grid(row=4,column=1)
lebelresult = Label(mainWindow )
lebelresult.grid(row=5,column=1)

mainloop()