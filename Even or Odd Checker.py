from tkinter import *

# GUI window
root=Tk()
root.title("Even/Odd Checker")
root.geometry("400x300")

# function for check number is even or odd and error handling for non numeric value
def check(event=None):
    try:
        number = int(entry.get())
        if number %2==0:
            result_label.config(text=f"{number} is an even number",fg="green")
        else:
            result_label.config(text=f"{number} is an odd number", fg="grey")
        entry.delete(0, END)
    except ValueError:
         result_label.config(text="Please enter a valid number", fg="red")
# reset function for reset button
def reset():
    entry.delete(0 ,END)
    result_label.config(text="")

# label 
label=Label(root, text="Enter Your Number :-", font="Dubai 20 bold", padx=5, pady=5)
label.pack(pady=10)

# entry widget for input
entry=Entry(root, font="15")
entry.pack(pady=10)
entry.focus() #includes a blinking cursor to entry widget so that the user doesn't have to click repeatedly.
entry.bind("<Return>", check) #for click enter to check

# frame for contain buttons 
frame=Frame(root)
check_button=Button(frame, text="Check", font="Dubai 15 bold", bg="green", fg="white", command=check)
check_button.grid(row=0, column=0, padx=10, pady=10)

Reset_button=Button(frame, text="Reset", font="Dubai 15 bold", bg="red", fg="white", command=reset)
Reset_button.grid(row=0, column=1, padx=10, pady=10)
frame.pack()

# label for showing result
result_label=Label(root, text="", font="Dubai 20 bold")
result_label.pack(pady=5)
                                                                           
root.mainloop()