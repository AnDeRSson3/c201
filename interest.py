from tkinter import *
window=Tk()

# add widgets here


window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_interest():
    p =float(principle_entry.get())
    r =float(interest_entry.get())
    t =float(time_entry.get())
    i =(p*r*t)/100
    interest= round(i,2)


    output_message=Label(result_frame, text="With "+str(p)+" at the rate of interest "+str(r)+" for "+str(t)+" years gives "+str(interest), bg = "lightcyan", font=("Calibri", 10), width=60)
    output_message.place(x=20,y=40)
    output_message.pack()

app_label=Label(window, text="Interest CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

principle_label=Label(window, text="Enter Principle", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=5)
principle_label.place(x=20, y=140)

principle_entry=Entry(window, text="", bd=2, width=15)
principle_entry.place(x=150, y=142)

interest_label=Label(window, text="Enter Interest in %", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=5)
interest_label.place(x=20, y=185)

interest_entry=Entry(window, text="", bd=2, width=15)
interest_entry.place(x=150, y=187)

time_label=Label(window, text="Enter Years", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=5)
time_label.place(x=20, y=225)

time_entry=Entry(window, text="", bd=2, width=15)
time_entry.place(x=150, y=225)

calculate_button=Button(window, text="CALCULATE", fg = "black", bg = "cyan", bd=4, command=calculate_interest)
calculate_button.place(x=20, y=275)

result_frame = LabelFrame(window, text="Result", bg="lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame, text="", bg = "lightcyan", font=("Calibri", 8), width=40)
result_label.place(x=20, y=20)
result_label.pack()

window.mainloop()









