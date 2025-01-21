from tkinter import *
import random as rn
import customtkinter as cutk
from tkinter import messagebox
PROGRESS_CR = '#A3320B'
list_of_numbers = ['0','1','2','3','4','5','6','7','8','9']
list_of_chars = ['a','b','c','d','f','g','h','m','n','r','t','e','q','o','p','u','y','w','i','s','j','k','l','z','x','v']
list_of_symbols = ['*','+','-','/','-','_','=',')','(','#','$','%','@','{','}','(',')','>','<','!','?']
str_ = ' '
def generate_password_func() -> None:
    main_entry.delete(0,'end')
    all_list = []
    finally_list = []
    if not (second_entry.get()):
        messagebox.showerror('Erorr','You should put length your password')
        return
    if (var_char.get()):
        for char in list_of_chars:
            all_list.append(char)
    if (var_num.get()):
        for num in list_of_numbers:
            all_list.append(num)
    if (var_sym.get()):
        for symbol in list_of_symbols:
            all_list.append(symbol)    
    if (var_spa.get()):
        for i in range(15):
            all_list.append(str_)
    if not all_list:
        for num in list_of_numbers:
            all_list.append(num)
    rn.shuffle(all_list)
    rn.shuffle(all_list)
    for i in range(int(second_entry.get())):
        pass__ = rn.choice(all_list)
        finally_list.append(pass__)
    else:
        print(finally_list)
    main_entry.insert(0,''.join(finally_list))
 
root = Tk()
root.title('genrate password')
root.geometry('600x400+250+100') 
var_char = IntVar()
var_num = IntVar()
var_sym = IntVar()
var_spa = IntVar()
main_entry = cutk.CTkEntry(root,width=300)
main_entry.place(x=5,y=10)
second_entry = cutk.CTkEntry(root,width=30)
second_entry.place(x=5,y=40)
main_button = cutk.CTkButton(root,text='generate',command=generate_password_func).place(x=5,y=80)
label = cutk.CTkLabel(root,text='--------------------------------------------------------------------------------------------------------------------------------',text_color=PROGRESS_CR).place(x=5,y=120)
cutk.CTkSwitch(root,text='Numbers',variable=var_num,progress_color=PROGRESS_CR).place(x=5,y=150)
cutk.CTkSwitch(root,text='Chars',variable=var_char,progress_color=PROGRESS_CR).place(x=5,y=175)
cutk.CTkSwitch(root,text='Symbols',variable=var_sym,progress_color=PROGRESS_CR).place(x=5,y=205)
cutk.CTkSwitch(root,text='Spaces',variable=var_spa,progress_color=PROGRESS_CR).place(x=5,y=235)

root.mainloop()