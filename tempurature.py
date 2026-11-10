from tkinter import *
import tkinter.font as font
window = Tk()
window.geometry("900x500")
window.title("Celsius to fahrenheit converter")

def on_button_press():
    tempurature_answer = tempurature_entry.get()

    fahrenheit_temp = tempurature_answer*1.8 + 32

    answer_label = Label(frame,text=f"{tempurature_entry} in fahrenheit is {fahrenheit_temp}")
    answer_label.grid(row=3,column=0,pady=10)


title1 = Label(window,text="Celsius -> fahrenheit",font=font.Font(size=30),fg="grey").pack()

frame = Frame(window)
frame.pack(pady= 50)

tempurature = Label(frame,text="Enter tempurature in Celsius : ",font=font.Font(size=15))
tempurature.grid(row=1,column=0)

tempurature_entry = Entry(frame)
tempurature_entry.grid(row=1,column=1)


convert_button = Button(frame,text="Convert to fahrenheit",pady=10,padx=20,font=font.Font(size=15),width=20,height=2,fg="black",bg="green",command=on_button_press())
convert_button.grid(row=4,column=0,columnspan=2,pady=10)

error_messege = Label(frame,text="Please enter a valid input",font=font.Font(size=8),fg="red")


tempurature_answer = tempurature_entry.get
window.mainloop()