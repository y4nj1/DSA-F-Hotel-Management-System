#import modules
 
from tkinter import *
import os
from subprocess import call
from PIL import ImageTk, Image

def open_menu():
    call(["python", "menu.py"])

# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("500x300")
    register_screen.configure(bg="#66717E")
    font9 = "-family {Segoe UI} -size 9 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0" 
    font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
    font16 = "-family {Swis721 BlkCn BT} -size 28 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="#66717E", fg='white', font=font16).pack()
    Label(register_screen, text="", bg="#66717E").pack()
    username_lable = Label(register_screen, text="Username * ", bg="#66717E", fg='white', font=font14)
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ", bg="#66717E", fg='white', font=font14)
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="", bg="#66717E").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="#F1E67A", font=font9, command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("700x300")
    login_screen.configure(bg="#66717E")
    font9 = "-family {Segoe UI} -size 9 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0" 
    font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
    font16 = "-family {Swis721 BlkCn BT} -size 28 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
    
    Label(login_screen, text="Please enter details below to login", bg="#66717E", fg='white', font=font16).pack()
    Label(login_screen, text="", bg="#66717E").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ", bg="#66717E", fg='white', font=font14).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="", bg="#66717E").pack()
    Label(login_screen, text="Password * ", bg="#66717E", fg='white', font=font14).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="", bg="#66717E").pack()
    Button(login_screen, text="Login", width=10, height=1, bg="#F1E67A", font=font9, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
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
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    main_screen.destroy()
    open_menu()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.resizable(0,0)
    font9 = "-family {Segoe UI} -size 9 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0" 
    font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
    font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
    main_screen.geometry("750x500")
    main_screen.title("Hotel Management Account Login")
    main_screen.configure(bg='#04151F')
    

    header = Label(text="Welcome", bg="#F1E67A", width="11", height="2", font=(font16))
    header.pack()
    header.place(x=0, y=0)
    Label(text="").pack()
    
    l_icon = Image.open("./assets/i-login.png")
    l_icon1 = l_icon.resize((150,150), Image.ANTIALIAS)
    l_icon2 = ImageTk.PhotoImage(l_icon1)
    l_but = Button(text="Login", image = l_icon2, compound=TOP, font=(font14), bg="#F1E67A", command = login)
    l_but.pack(side=TOP)
    l_but.place(x=15, y=200)
    Label(text="").pack()
   
    r_icon = Image.open("./assets/i-register.png")
    r_icon1 = r_icon.resize((150,150), Image.ANTIALIAS)
    r_icon2 = ImageTk.PhotoImage(r_icon1)
    r_but = Button(text="Register", image = r_icon2, compound=TOP, font=(font14), bg="#F1E67A", command=register)
    r_but.pack(side=TOP)
    r_but.place(x=180, y=200)

    photo = PhotoImage(file = "./assets/i-titlebi.png")
    main_screen.iconphoto(False, photo)

    frame = Canvas(main_screen, width=400, height=500, highlightbackground = '#04151F')
    frame.place(x=350, y=0)
    frame.configure(bg='#04151F')


    photo1 = Image.open("./assets/i-hotel.png")
    photo1_1 = photo1.resize((375,350), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(photo1_1)
    frame.create_image(200,50, anchor=N, image=photo2)

 
    main_screen.mainloop()
 
 
main_account_screen()