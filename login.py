from tkinter import*
from tkinter import messagebox
class Login_System:
    def __init__(self,root):
        # print("hello")
        self.root=root
        self.root.title("login System")
        self.root.geometry("1350x700+0+0")

        self.uname=StringVar()
        self.pass_=StringVar()

        title=Label(self.root,text="Login System",font=("times new roman",40,"bold"),
                   bg="yellow",fg="red" ,
                    bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=400,y=150)

        lbluser=Label(Login_Frame,text="Username",compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

        lblpass = Label(Login_Frame, text="Password", compound=LEFT, font=("times new roman", 20, "bold"),
                        bg="white").grid(row=2, column=0, padx=20, pady=10)
        txtpass = Entry(Login_Frame, bd=5,relief=GROOVE,textvariable=self.pass_,font=("", 15)).grid(row=2, column=1, padx=20)

        btn_log=Button(Login_Frame,text="Login",width=15,font=("times new rman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)


    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","All fields are required !!")
        elif self.uname.get()=="abc" and self.pass_.get()=="1234":
            messagebox.showinfo("Successfull",f"welcome{self.uname.get()}")
        else:
            messagebox.showerror("Error", "Invalid User and Password")
root=Tk()
obj=Login_System(root)
root.mainloop()