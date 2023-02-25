from tkinter import *
window = Tk()

window.title("Simple Interest Calculator")
window.geometry("380x400")
window.configure(bg='gray')

def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i,2)
    show_label.destroy()
    message = Label(result_frame, text="Rs " + str(interest), bg="grey", font=("Calibri",12), width=33)
    message.place(x=20, y=40)
    message.pack()


app_title = Label(window, text="SIMPLE INTEREST CALCULATOR", fg="black", bg="white", font=("Calibri", 20),bd=5)
app_title.place(x=20, y=20)

principle_label=Label(window, text="Enter the Principle", fg = "black", bg = "white", font=("Calibri", 12)) 
principle_label.place(x=20, y=90)

principle = Entry(window, text="", bd=2, width=15)
principle.place(x=180, y=92)


rate_label=Label(window, text="Enter the Rate", fg = "black", bg = "white", font=("Calibri", 12)) 
rate_label.place(x=20, y=140)

rate = Entry(window, text="", bd=2, width=15)
rate.place(x=180, y=142)


time_label=Label(window, text="Enter the Time", fg = "black", bg = "white", font=("Calibri", 12)) 
time_label.place(x=20, y=185)

time = Entry(window, text="", bd=2, width=15)
time.place(x=180, y=187)

calculate_button=Button(window,text="CALCULATE",fg = "white", bg = "black",bd=4,command=calculate_interest) 
calculate_button.place(x=20,y=250)


result_frame = LabelFrame(window, text="Result", bg="grey", font=("Calibri",12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20, y=300)

show_label=Label(result_frame,text=" ", bg = "white", font=("Calibri", 12), width=33)
show_label.place(x=20,y=20)
show_label.pack()

window.mainloop()