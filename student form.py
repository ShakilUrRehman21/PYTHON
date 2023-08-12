from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

#Heading
label= Label(root, text="Student Registration Form",width=20,font=("bold", 20)).place(x=2,y=5)

#function for validating entry field for int input
def only_numbers(char):
    return char.isdigit()
validation = root.register(only_numbers)

#function for validating entry field for string input
def validate(u_input):
    return u_input.isalpha()
validation1 = root.register(validate)

def submit_form():
    name=firstname.get()
    age=age.get()
    email=email.get()
    if not name:
        return messagebox.showerror("error")

#firstname field
firstname=Label(root,text="First Name: ").place(x=50,y=50)
entry1=Entry(root,validate="key", validatecommand=(validation1, '%S')).place(x=150,y=50)


#middlename field
middlename=Label(root,text="Middle Name: ").place(x=50,y=80)
entry2=Entry(root,validate="key", validatecommand=(validation1, '%S')).place(x=150,y=80)

#lastname field
lastname=Label(root,text="Last Name: ").place(x=50,y=110)
entry3=Entry(root,validate="key", validatecommand=(validation1, '%S')).place(x=150,y=110)


#contact field
contact=Label(root,text="Contact No: ").place(x=50,y=140)
entry5=Entry(root,validate="key", validatecommand=(validation, '%S')).place(x=150,y=140)

#age
label4 = Label(root, text="Age:").place(x=50,y=170)
entry6 = Entry(root,validate="key", validatecommand=(validation, '%S')).place(x=150,y=170)


#email field
email=Label(root,text="Email: ").place(x=50,y=200)
entry4=Entry(root).place(x=150,y=200)

#gender
gen=Label(root,text="Gender: ").place(x=50,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=150,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=220,y=230)

#course
course=Label(root,text="Course: ")
course.place(x=50,y=270)
menu= StringVar()
menu.set("Select course")
drop= OptionMenu(root, menu,"B.Tech", "Diploma","M.B.B.S","C.A").place(x=150,y=270)


#remember me
var1 = IntVar()
Radiobutton(root, text="I accept all the T&C",padx = 5, variable=var1, value=1).place(x=150,y=320)
def clicked():
    print("Registration seccussfully done")
Button(root, text='Submit',width=20,bg='brown',fg='white',command=clicked).place(x=180,y=380)

root.mainloop()
print("Thank You!")

