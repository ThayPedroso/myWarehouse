"""
A program that stores materials in a warehouse:
Description, Manufacturer, Code
Quantity, BarCode

User can:
View all records
Search an entry
Add entry 
Update entry 
Delete
Close
"""

from tkinter import *
from backend import Database
from tkinter import messagebox

database = Database()

def get_selected_row(event):
        try:
                global selected_tuple
                index=list1.curselection()[0]
                selected_tuple=list1.get(index)
                e1.delete(0,END)
                e1.insert(END,selected_tuple[1])
                e2.delete(0,END)
                e2.insert(END,selected_tuple[2])
                e3.delete(0,END)
                e3.insert(END,selected_tuple[3])
                e4.delete(0,END)
                e4.insert(END,selected_tuple[4])
                e5.delete(0,END)
                e5.insert(END,selected_tuple[5])
        except IndexError:
                pass        

def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search(description_text.get(),manufacturer_text.get(), quantity_text.get(),code_text.get(),barCode_text.get()):
        list1.insert(END,row)

def add_command():
    if barCode_text.get() == "":
        messagebox.showerror('Message title', 'É necessário inserir um código de barras.') 
        return
    if quantity_text.get() == "":
        messagebox.showerror('Message title', 'É necessário inserir a quantidade.') 
        return
    if code_text.get() == "":
        messagebox.showerror('Message title', 'É necessário inserir um código para o produto.') 
        return
    database.insert(description_text.get(),manufacturer_text.get(), quantity_text.get(),code_text.get(),barCode_text.get())
    list1.delete(0,END)
    list1.insert(END,(description_text.get(),manufacturer_text.get(), quantity_text.get(),code_text.get(),barCode_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],description_text.get(),manufacturer_text.get(), quantity_text.get(),code_text.get(),barCode_text.get())

#Interface gráfica
window = Tk()

window.wm_title("Warehouse")

l1 = Label(window,text="Descrição")
l1.grid(row=0,column=0)

l2 = Label(window,text="Fabricante")
l2.grid(row=1,column=0)

l3 = Label(window,text="Quantidade")
l3.grid(row=1,column=2)

l4 = Label(window,text="Código")
l4.grid(row=2,column=0)

l5 = Label(window,text="Cód.Barras")
l5.grid(row=2,column=2)

description_text = StringVar()
e1 = Entry(window,textvariable=description_text,width=52)
e1.grid(row=0,column=1,columnspan=3)    

manufacturer_text = StringVar()
e2 = Entry(window,textvariable=manufacturer_text)
e2.grid(row=1,column=1)

quantity_text = StringVar()
e3 = Entry(window,textvariable=quantity_text)
e3.grid(row=1,column=3)

code_text = StringVar()
e4 = Entry(window,textvariable=code_text)
e4.grid(row=2,column=1)

barCode_text = StringVar()
e5 = Entry(window,textvariable=barCode_text)
e5.grid(row=2,column=3)

list1 = Listbox(window, height=8, width=62)
list1.grid(row=3, column=0, rowspan=8, columnspan=4)

sb1 = Scrollbar(window)
sb1.grid(row=3,column=4,rowspan=8)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(window,text="Ver todos", width=12,command=view_command)
b1.grid(row=1,column=5)

b2 = Button(window,text="Procurar", width=12,command=search_command)
b2.grid(row=2,column=5)

b3 = Button(window,text="Adicionar", width=12,command=add_command)
b3.grid(row=3,column=5)

b4 = Button(window,text="Update", width=12,command=update_command)
b4.grid(row=4,column=5)

b5 = Button(window,text="Delete", width=12,command=delete_command)
b5.grid(row=5,column=5)

b6 = Button(window,text="Fechar", width=12,command=window.destroy)
b6.grid(row=6,column=5)

window.mainloop()