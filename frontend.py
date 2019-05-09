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
from tkinter import ttk

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

def get_selected_row_2(event):
        try:
                global selected_tuple_2
                index=list2.curselection()[0]
                selected_tuple_2=list2.get(index)
                e6.delete(0,END)
                e6.insert(END,selected_tuple_2[1])
                e7.delete(0,END)
                e7.insert(END,selected_tuple_2[2])
                e8.delete(0,END)
                e8.insert(END,selected_tuple_2[3])
                e9.delete(0,END)
                e9.insert(END,selected_tuple_2[4])
                e10.delete(0,END)
                e10.insert(END,selected_tuple_2[5])
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
    database.insert(description_text.get().upper(),manufacturer_text.get().upper(), quantity_text.get(),code_text.get().upper(),barCode_text.get())
    list1.delete(0,END)
    list1.insert(END,(description_text.get().upper(),manufacturer_text.get().upper(), quantity_text.get(),code_text.get().upper(),barCode_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],description_text.get().upper(),manufacturer_text.get().upper(), quantity_text.get(),code_text.get().upper(),barCode_text.get())

def advancedSearch_command():
    list2.delete(0,END)
    for row in database.advancedSearch(description_text_2.get(), code_text_2.get()):
        list2.insert(END,row)

#Interface gráfica
window = Tk()

window.wm_title("Warehouse")

#Divisão em abas
tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
 
tab_control.add(tab1, text='Cadastro')
tab_control.add(tab2, text='Consulta')


# Inicio - tab1
l1 = Label(tab1,text="Descrição")
l1.grid(row=0,column=0)

l2 = Label(tab1,text="Fabricante")
l2.grid(row=1,column=0)

l3 = Label(tab1,text="Quantidade")
l3.grid(row=1,column=2)

l4 = Label(tab1,text="Código")
l4.grid(row=2,column=0)

l5 = Label(tab1,text="Cód.Barras")
l5.grid(row=2,column=2)

description_text = StringVar()
e1 = Entry(tab1,textvariable=description_text,width=52)
e1.grid(row=0,column=1,columnspan=3)    

manufacturer_text = StringVar()
e2 = Entry(tab1,textvariable=manufacturer_text)
e2.grid(row=1,column=1)

quantity_text = StringVar()
e3 = Entry(tab1,textvariable=quantity_text)
e3.grid(row=1,column=3)

code_text = StringVar()
e4 = Entry(tab1,textvariable=code_text)
e4.grid(row=2,column=1)

barCode_text = StringVar()
e5 = Entry(tab1,textvariable=barCode_text)
e5.grid(row=2,column=3)

list1 = Listbox(tab1, height=8, width=62)
list1.grid(row=3, column=0, rowspan=8, columnspan=4)

sb1 = Scrollbar(tab1)
sb1.grid(row=3,column=4,rowspan=8)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(tab1,text="Ver todos", width=12,command=view_command)
b1.grid(row=1,column=5)

b2 = Button(tab1,text="Procurar", width=12,command=search_command)
b2.grid(row=2,column=5)

b3 = Button(tab1,text="Adicionar", width=12,command=add_command)
b3.grid(row=3,column=5)

b4 = Button(tab1,text="Update", width=12,command=update_command)
b4.grid(row=4,column=5)

b5 = Button(tab1,text="Excluir", width=12,command=delete_command)
b5.grid(row=5,column=5)

b6 = Button(tab1,text="Fechar", width=12,command=window.destroy)
b6.grid(row=6,column=5)


# Inicio - tab2
l6 = Label(tab2,text="Descrição")
l6.grid(row=0,column=0)

l7 = Label(tab2,text="Fabricante")
l7.grid(row=1,column=0)

l8 = Label(tab2,text="Quantidade")
l8.grid(row=1,column=2)

l9 = Label(tab2,text="Código")
l9.grid(row=2,column=0)

l10 = Label(tab2,text="Cód.Barras")
l10.grid(row=2,column=2)

description_text_2 = StringVar()
e6 = Entry(tab2,textvariable=description_text_2,width=52)
e6.grid(row=0,column=1,columnspan=3)    

manufacturer_text_2 = StringVar()
e7 = Entry(tab2,textvariable=manufacturer_text_2, state='disabled')
e7.grid(row=1,column=1)

quantity_text_2 = StringVar()
e8 = Entry(tab2,textvariable=quantity_text_2, state='disabled')
e8.grid(row=1,column=3)

code_text_2 = StringVar()
e9 = Entry(tab2,textvariable=code_text_2)
e9.grid(row=2,column=1)

barCode_text_2 = StringVar()
e10 = Entry(tab2,textvariable=barCode_text_2, state='disabled')
e10.grid(row=2,column=3)

list2 = Listbox(tab2, height=8, width=62)
list2.grid(row=3, column=0, rowspan=8, columnspan=4)

sb2 = Scrollbar(tab2)
sb2.grid(row=3,column=4,rowspan=8)

list2.configure(yscrollcommand=sb2.set)
sb2.configure(command=list2.yview)

list2.bind('<<ListboxSelect>>',get_selected_row_2)

b6 = Button(tab2,text="Procurar", width=12,command=advancedSearch_command)
b6.grid(row=1,column=5)


tab_control.pack(expand=1, fill='both')
window.mainloop()