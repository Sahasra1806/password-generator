
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import string, random

root = Tk()
root.geometry("500x500")
root.title("Sahasra Password Generator")
root.config(bg="#f4f4f4")  
root.resizable(False, False)

def password_generate():
    try:
        length_password = solidboss.get()
        small_letters = string.ascii_lowercase
        capital_letters = string.ascii_uppercase
        digits = string.digits
        special_character = string.punctuation
        all_list = []
        all_list.extend(list(small_letters))
        all_list.extend(list(capital_letters))
        all_list.extend(list(digits))
        all_list.extend(list(special_character))
        random.shuffle(all_list)
        password.set("".join(all_list[0:length_password]))
    except:
        messagebox.askretrycancel("A Problem Has Occurred", "Please Try Again")
        
all_no = {str(i): str(i) for i in range(1, 31)}

Title = Label(root, text="Sahasra Password Generator", bg="#ffffff", fg="#1f0099", font=("Helvetica", 20, "bold"))
Title.pack(anchor="center", pady=20)

length = Label(root, text="Select the Length of Your Password:", fg="#006666", bg="#f4f4f4", font=("Helvetica", 12))
length.place(x=20, y=70)

solidboss = IntVar()
Selector = Combobox(root, textvariable=solidboss, state="readonly", font=("Helvetica", 10))
Selector['values'] = [l for l in all_no.keys()]
Selector.current( )
Selector.place(x=270, y=72)

def on_enter(e):
    generate_btn['bg'] = "#005580"
    generate_btn['fg'] = "white"
    
def on_leave(e):
    generate_btn['bg'] = "#00b386"
    generate_btn['fg'] = "black"
    
generate_btn = Button(root, text="Generate Password", bg="#00b386", fg="black", font=("Helvetica", 14, "bold"),cursor="hand2", command=password_generate, bd=0, relief=SOLID)
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)
generate_btn.pack(anchor="center", pady=50)
generate_btn.place(x=150, y=220)

result_label = Label(root, text="Generated Password:", bg="#f4f4f4", fg="#006666", font=("Helvetica", 12))
result_label.place(x=20, y=160)

password = StringVar()
password_final = Entry(root, textvariable=password, state="readonly", fg="#004d4d", font=("Helvetica", 14), width=25,bd=2, relief=GROOVE, justify="center")
password_final.place(x=200, y=160)

root.mainloop()
