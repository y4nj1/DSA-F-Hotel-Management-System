import os
from subprocess import call

import sys


from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
py3 = True

def click_checkinn():
    call(["python", "checkin.py"])
def click_list():
    call(["python", "list.py"])
def click_checkout():
    call(["python", "checkout.py"])
def click_getinfo():
    call(["python","getinfo.py"])
def logout():
    root.destroy()
    call(["python","main.py"])


class HOTEL_MANAGEMENT:
    def __init__(self):
        global root
        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#04151F'  
        _fgcolor = '#ffffff'  
        _compcolor = '#ffffff' 
        _ana1color = '#ffffff' 
        _ana2color = '#ffffff' 
        font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 60 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("963x749+540+110")
        root.title("GOLDSTAR HOTEL MANAGEMENT")
        root.configure(background="#F1E67A")
        root.configure(highlightbackground="#66717E")
        root.configure(highlightcolor="white")



        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#04151F")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Message6 = Message(self.Frame1)
        self.Message6.place(relx=0.06, rely=0.01, relheight=0.15, relwidth=0.86)
        self.Message6.configure(background="#04151F")
        self.Message6.configure(font=font16)
        self.Message6.configure(foreground="#F1E67A")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text='''GOLDSTAR HOTEL''')
        self.Message6.configure(width=800)

        self.Button2 = Button(self.Frame1)
        l_icon = Image.open("./assets/i-checkin.png")
        l_icon1 = l_icon.resize((200,200), Image.ANTIALIAS)
        l_icon2 = ImageTk.PhotoImage(l_icon1)
        self.Button2.pack(side=TOP)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#F1E67A")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''CHECK IN''', image = l_icon2, compound=TOP)
        self.Button2.configure(width=300)
        self.Button2.place(x=25, y=150)
        self.Button2.configure(command=click_checkinn)

        self.Button3 = Button(self.Frame1)
        m_icon = Image.open("./assets/i-guestlist.png")
        m_icon1 = m_icon.resize((200,200), Image.ANTIALIAS)
        m_icon2 = ImageTk.PhotoImage(m_icon1)
        self.Button3.pack(side=TOP)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#F1E67A")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=font14)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''SHOW GUEST LIST''', image = m_icon2, compound=TOP)
        self.Button3.configure(width=300)
        self.Button3.place(x=350, y=150)
        self.Button3.configure(command=click_list)

        self.Button4 = Button(self.Frame1)
        n_icon = Image.open("./assets/i-checkout.png")
        n_icon1 = n_icon.resize((200,200), Image.ANTIALIAS)
        n_icon2 = ImageTk.PhotoImage(n_icon1)
        self.Button4.pack(side=TOP)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#F1E67A")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font14)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''CHECK OUT''', image = n_icon2, compound=TOP)
        self.Button4.configure(width=300)
        self.Button4.place(x=25, y=425)
        self.Button4.configure(command=click_checkout)

        self.Button5 = Button(self.Frame1)
        o_icon = Image.open("./assets/i-info.png")
        o_icon1 = o_icon.resize((200,200), Image.ANTIALIAS)
        o_icon2 = ImageTk.PhotoImage(o_icon1)
        self.Button5.pack(side=TOP)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#F1E67A")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=font14)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''GET INFO OF ANY GUEST''', image = o_icon2, compound=TOP)
        self.Button5.configure(width=300)
        self.Button5.place(x=350, y=425)
        self.Button5.configure(command=click_getinfo)

        self.Button6 = Button(self.Frame1)
        p_icon = Image.open("./assets/i-logout.png")
        p_icon1 = p_icon.resize((200,200), Image.ANTIALIAS)
        p_icon2 = ImageTk.PhotoImage(p_icon1)
        self.Button6.pack(side=TOP)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(font=font14)
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''LOG OUT''', image = p_icon2, compound=TOP)
        self.Button6.configure(height=515, width=215)
        self.Button6.place(x=675, y=150)
        self.Button6.configure(command=logout)
        root.mainloop()


if __name__ == '__main__':
    GUEST=HOTEL_MANAGEMENT()


 