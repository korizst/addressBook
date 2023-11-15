import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Address Book')
root.geometry('800x600')


class PhoneEntry:
    name = ''
    phoneNr = ''
    address = ''


dataList = []

# FUNCTIONS


# Read data at start

def read():
    with open('data.txt', 'r', encoding='utf-8') as file:
        listbox_index = 1
        for line in file:
            columns = line.split(',', 2)
            pe = PhoneEntry()
            pe.name = columns[0]
            pe.phoneNr = columns[1]
            pe.address = columns[2]
            dataList.append(pe)
            list_box.insert(listbox_index, pe.name)
            listbox_index += 1
    name_entry.focus()


# Clear Fields Function

def clear_fields():
    global name_entry
    global phone_number_entry
    global address_textbox

    name_entry.delete(0, END)
    name_entry.focus()
    phone_number_entry.delete(0, END)
    address_textbox.delete('1.0', END)


# Disable Add Button by click in the Listbox

def listbox_pressed(event):
    global add_button
    global new_entry_button
    global view_button
    global delete_button

    new_entry_button = Button(root, text='New Entry', command=new_entry, width=10, padx=5, pady=5)
    new_entry_button.grid(row=3, column=0, padx=5, pady=(20, 0))
    add_button = Button(root, text='Add', width=10, padx=5, pady=5, state=DISABLED)
    add_button.grid(row=4, column=0, padx=5, pady=5)
    view_button = Button(root, text='View', width=10, command=view, padx=5, pady=5)
    view_button.grid(row=5, column=0, padx=5, pady=5)
    delete_button = Button(root, text='Delete', width=10, command=delete_entry, padx=5, pady=5)
    delete_button.grid(row=6, column=0, padx=5, pady=5)


def out_of_listbox_pressed(event):
    global add_button
    global new_entry_button
    global view_button
    global delete_button

    new_entry_button = Button(root, text='New Entry', width=10, padx=5, pady=5, state=DISABLED)
    new_entry_button.grid(row=3, column=0, padx=5, pady=(20, 0))
    add_button = Button(root, text='Add', width=10, command=add, padx=5, pady=5)
    add_button.grid(row=4, column=0, padx=5, pady=5)
    view_button = Button(root, text='View', width=10, padx=5, pady=5, state=DISABLED)
    view_button.grid(row=5, column=0, padx=5, pady=5)
    delete_button = Button(root, text='Delete', width=10, padx=5, pady=5, state=DISABLED)
    delete_button.grid(row=6, column=0, padx=5, pady=5)


# Add Button Function

def add():
    global name_entry
    global phone_number_entry
    global address_textbox

    pe = PhoneEntry()
    pe.name = name_entry.get()
    pe.phoneNr = phone_number_entry.get()
    pe.address = address_textbox.get("1.0", END)
    dataList.append(pe)

    for attr, value in pe.__dict__.items():
        if value == '' or value == '\n':
            messagebox.showerror('Missing data', f'One or more fields are empty')
            #  here should the app return for user, which fields are empty

    if pe.name != '' and pe.phoneNr != '' and pe.address != '\n':
        with open('data.txt', 'a', encoding='utf-8') as file:
            file.write(pe.name + ',' + pe.phoneNr + ',' + pe.address)
            list_box.insert(len(dataList) + 1, pe.name)
            clear_fields()


# View Button Function
def view():
    global name_entry
    global phone_number_entry
    global new_entry_button

    with open('data.txt', 'r', encoding='utf-8') as file:
        for line in file:
            columns = line.split(',')
            pe = PhoneEntry()
            pe.name = columns[0]
            pe.phoneNr = columns[1]
            for i in list_box.curselection():
                if list_box.get(i) == pe.name:
                    name_entry = Entry(root, width=30)
                    name_entry.insert(0, pe.name)
                    name_entry.grid(row=0, column=1)
                    phone_number_entry = Entry(root, width=30)
                    phone_number_entry.insert(0, pe.phoneNr)
                    phone_number_entry.grid(row=1, column=1)
    new_entry_button = Button(root, text='New Entry', width=10, command=new_entry, padx=5, pady=5)
    new_entry_button.grid(row=3, column=0, padx=5, pady=(20, 0))


# New Entry Button Function
def new_entry():
    clear_fields()
    global add_button
    global new_entry_button
    global view_button
    global delete_button

    new_entry_button = Button(root, text='New Entry', width=10, padx=5, pady=5, state=DISABLED)
    new_entry_button.grid(row=3, column=0, padx=5, pady=(20, 0))
    add_button = Button(root, text='Add', width=10, command=add, padx=5, pady=5)
    add_button.grid(row=4, column=0, padx=5, pady=5)
    view_button = Button(root, text='View', width=10, padx=5, pady=5, state=DISABLED)
    view_button.grid(row=5, column=0, padx=5, pady=5)
    delete_button = Button(root, text='Delete', width=10, padx=5, pady=5, state=DISABLED)
    delete_button.grid(row=6, column=0, padx=5, pady=5)


# Delete Button Function
def delete_entry():
    response = messagebox.askyesno('Warning!', 'Are you sure you want to delete the selected item?')
    if response == 1:
        clear_fields()
        with open('data.txt', 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
            with open('data.txt', 'w', encoding='utf-8') as outfile:
                for line in lines:
                    for i in list_box.curselection():
                        if list_box.get(i) not in line:
                            outfile.write(line)
        list_box.delete(tkinter.ANCHOR)
    else:
        pass


# Reset Button Function
def reset():
    response = messagebox.askyesno('Warning!', 'Are you sure you want to delete all items?')
    if response == 1:
        clear_fields()
        with open('data.txt', 'a', encoding='utf-8') as infile:
            infile.truncate(0)
        list_box.delete(0, END)
    else:
        pass


# Widgets Column 0

name_label = Label(root, text='Name')
name_label.grid(row=0, column=0, padx=10, pady=(20, 0), sticky=W)

phone_number_label = Label(root, text='Phone No.')
phone_number_label.grid(row=1, column=0, padx=10, sticky=W)

address_label = Label(root, text='Address')
address_label.grid(row=2, column=0, padx=10, sticky=W)

new_entry_button = Button(root, text='New Entry', command=new_entry, width=10, padx=5, pady=5, state=DISABLED)
new_entry_button.grid(row=3, column=0, padx=20, pady=(20, 0))

add_button = Button(root, text='Add', command=add, width=10, padx=5, pady=5)
add_button.grid(row=4, column=0, padx=5, pady=5)

view_button = Button(root, text='View', padx=5, pady=5, width=10, state=DISABLED)
view_button.grid(row=5, column=0, padx=5, pady=5)

delete_button = Button(root, text='Delete', padx=5, pady=5, width=10, state=DISABLED)
delete_button.grid(row=6, column=0, padx=5, pady=5)

reset_button = Button(root, text='Reset', command=reset, width=10, padx=5, pady=5)
reset_button.grid(row=7, column=0, padx=5, pady=5)

# Widgets Column 1

name_entry = Entry(root, width=30)
name_entry.grid(row=0, column=1, pady=(20, 0))
name_entry.bind('<Button-1>', out_of_listbox_pressed)

phone_number_entry = Entry(root, width=30)
phone_number_entry.grid(row=1, column=1)
phone_number_entry.bind('<Button-1>', out_of_listbox_pressed)

address_textbox = Text(root, width=25, height=10)
address_textbox.grid(row=2, column=1)

list_box = Listbox(root, width=30)
list_box.grid(row=3, column=1, rowspan=5)
list_box.bind('<Button-1>', listbox_pressed)

exit_button = Button(root, text='Exit Program', command=quit, width=10, padx=5, pady=5)
exit_button.grid(row=8, column=1)

read()

root.mainloop()
