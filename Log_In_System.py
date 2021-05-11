from tkinter import*
from tkinter import messagebox
import os


class Login_System:

        
    def __init__(self,root):
        
        #MAKING THE GUI
        self.root=root
        self.root.title("Stock Docs")
        self.root.geometry("1350x700+0+0")

        Log_In_Frame = Frame(self.root)
        Main_Menu_Frame = Frame(self.root)


        #HEADER FOR LOG IN FRAME
        Label(Log_In_Frame,text="Log In Page",font = ("Arial",40,"bold"), bg="white",relief=GROOVE).pack()
        Label(Log_In_Frame, text="").pack()
        
        global username_verify
        global password_verify
     
        username_verify = StringVar()
        password_verify = StringVar()
     
        global username_login_entry
        global password_login_entry
 

        Label(Log_In_Frame, text="Username * ",font=("Arial",20,"bold")).pack()
        username_login_entry = Entry(Log_In_Frame, textvariable=username_verify,relief=GROOVE,font=("",15))
        username_login_entry.pack()
        Label(Log_In_Frame, text="").pack()
        Label(Log_In_Frame, text="Password * ",font=("Arial",20,"bold")).pack()
        password_login_entry = Entry(Log_In_Frame, textvariable=password_verify, show= '*',relief=GROOVE,font=("",15))
        password_login_entry.pack()
        Label(Log_In_Frame, text="\n\n").pack()
        Button(Log_In_Frame, text="Login", height=1, command = self.login_verify,width=20,font=("Arial",14,"bold"),bg="green").pack()
        Label(Log_In_Frame, text="").pack()
        btn_reg=Button(Log_In_Frame, text="No Account? Register",command=self.register,width=20,font=("Arial",14,"bold"),bg="red").pack()
        Log_In_Frame.pack(fill = 'both', expand=1)
        

        #HEADER FOR MAIN MENU FRAME
        Label(Main_Menu_Frame,text="NAK NAM POTA!",font = ("Arial",40,"bold"), bg="white",relief=GROOVE).pack()
        Label(Main_Menu_Frame, text="").pack()


    def register(self):
        #MAKING THE GUI
        global register_screen
        register_screen = Toplevel(root)
        register_screen.title("Stock Docs")
        register_screen.geometry("1350x700+0+0")

        global username
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()


        Label(register_screen, text="Please enter details below",font = ("Arial",40,"bold"), bg="white",relief=GROOVE).pack()
        Label(register_screen, text="").pack()
        username_lable = Label(register_screen, text="Username * ",font=("Arial",20,"bold"))
        username_lable.pack()
        username_entry = Entry(register_screen, textvariable=username,relief=GROOVE,font=("",15))
        username_entry.pack()
        password_lable = Label(register_screen, text="Password * ",font=("Arial",20,"bold"))
        password_lable.pack()
        password_entry = Entry(register_screen, textvariable=password, show='*',relief=GROOVE,font=("",15))
        password_entry.pack()
        Label(register_screen, text="").pack()
        Button(register_screen, text="Register", width=20, command = self.register_user,font=("Arial",14,"bold"),bg="green").pack()
 




    # Implementing event on register button
    def register_user(self):
        
        username_info = username.get()
        password_info = password.get()
         
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
         
        username_entry.delete(0, END)
        password_entry.delete(0, END)
         
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

    # Implementing event on login button 
    def login_verify(self):   
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
         
        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                self.login_sucess()
         
            else:
                self.password_not_recognised()
         
        else:
            self.user_not_found()
                
    # Designing popup for login success            
    def login_sucess(self):
        global login_success_screen
        login_success_screen = Toplevel(root)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Login Success").pack()
        Button(login_success_screen, text="Proceed to Home Screen", command=self.delete_login_success).pack()
        
    # Designing popup for login invalid password
     
    def password_not_recognised(self):
        global password_not_recog_screen
        password_not_recog_screen = Toplevel(root)
        password_not_recog_screen.title("Success")
        password_not_recog_screen.geometry("150x100")
        Label(password_not_recog_screen, text="Invalid Password ").pack()
        Button(password_not_recog_screen, text="OK", command=self.delete_password_not_recognised).pack()
     
    # Designing popup for user not found
     
    def user_not_found(self):
        global user_not_found_screen
        user_not_found_screen = Toplevel(root)
        user_not_found_screen.title("Success")
        user_not_found_screen.geometry("150x100")
        Label(user_not_found_screen, text="User Not Found").pack()
        Button(user_not_found_screen, text="OK", command=self.delete_user_not_found_screen).pack()
     
    # Deleting popups
    def delete_login_success(self):
        login_success_screen.destroy()

    def delete_password_not_recognised(self):
        password_not_recog_screen.destroy()
        
    def delete_user_not_found_screen(self):
        user_not_found_screen.destroy()
     
          
        

            

root=Tk()
obj=Login_System(root)
root.mainloop()



        
