import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Address Book')
root.geometry('800x600')


class PhoneEntry:
    name = ''
    phoneNr = ''


dataList = []

# FUNCTIONS


# Read data at start

def read():
    with open('data.txt', 'r', encoding='utf-8') as file:
        listbox_index = 1
        for line in file:
            columns = line.split(',')
            pe = PhoneEntry()
            pe.name = columns[0]
            pe.phoneNr = columns[1]
            dataList.append(pe)
            list_box.insert(listbox_index, pe.name)
            listbox_index += 1


# Clear Fields Function

def clear_fields():
    global name_entry
    global phone_number_entry

    name_entry.delete(0, END)
    name_entry.focus()
    phone_number_entry.delete(0, END)


# Add Button Function

def add():
    global name_entry
    global phone_number_entry

    pe = PhoneEntry()
    pe.name = name_entry.get()
    pe.phoneNr = phone_number_entry.get()
    dataList.append(pe)
    with open('data.txt', 'r', encoding='utf-8') as file:
        no_name_lines = 0
        for line in file:
            if 'no name' in line:
                no_name_lines += 1

    with open('data.txt', 'a', encoding='utf-8') as file:
        if pe.name != '' and pe.phoneNr != '':
            file.write(pe.name + ',' + pe.phoneNr + '\n')
            list_box.insert(len(dataList) + 1, pe.name)
        elif pe.name != '' and pe.phoneNr == '':
            file.write(pe.name + ',' + 'no phone number' + '\n')
            list_box.insert(len(dataList) + 1, pe.name)
        else:
            file.write('no name' + str(no_name_lines + 1) + ',' + pe.phoneNr + '\n')
            list_box.insert(len(dataList) + 1, 'no name' + str(no_name_lines + 1))

    name_entry.delete(0, END)
    phone_number_entry.delete(0, END)
    name_entry.focus()


# View Button Function
def view():
    global name_entry
    global phone_number_entry
    global add_button

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
    add_button = Button(root, text='Add', padx=5, pady=5, state=DISABLED)
    add_button.grid(row=3, column=0)
    new_entry_button = Button(root, text='New Entry', command=new_entry, padx=5, pady=5)
    new_entry_button.grid(row=0, column=2, rowspan=2)


# New Entry Button Function
def new_entry():
    global add_button

    clear_fields()
    add_button = Button(root, text='Add', command=add, padx=5, pady=5)
    add_button.grid(row=3, column=0)


# Delete Button Function
def delete_entry():
    clear_fields()
    with open('data.txt', 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
        with open('data.txt', 'w', encoding='utf-8') as outfile:
            for line in lines:
                for i in list_box.curselection():
                    if list_box.get(i) not in line:
                        outfile.write(line)
    list_box.delete(tkinter.ANCHOR)


def reset():
    response = messagebox.askyesno('Warning!', 'Are you sure you want to delete all entries?')
    if response == 1:
        clear_fields()
        with open('data.txt', 'a', encoding='utf-8') as infile:
            infile.truncate(0)
        list_box.delete(0, END)
    else:
        pass


# Widgets Column 0

name_label = Label(root, text='Name')
name_label.grid(row=0, column=0)

phone_number_label = Label(root, text='Phone No.')
phone_number_label.grid(row=1, column=0)

# addressLabel = Label(root, text='Address')
# addressLabel.grid(row=2, column=0)

add_button = Button(root, text='Add', command=add, padx=5, pady=5)
add_button.grid(row=3, column=0)

view_button = Button(root, text='View', command=view, padx=5, pady=5)
view_button.grid(row=4, column=0)

delete_button = Button(root, text='Delete', command=delete_entry, padx=5, pady=5)
delete_button.grid(row=5, column=0)

reset_button = Button(root, text='Reset', command=reset, padx=5, pady=5)
reset_button.grid(row=6, column=0)

# Widgets Column 1

name_entry = Entry(root, width=30)
name_entry.grid(row=0, column=1)

phone_number_entry = Entry(root, width=30)
phone_number_entry.grid(row=1, column=1)

# addressEntry = Text(root, width=30, height=10)
# addressEntry.grid(row=2, column=1)

list_box = Listbox(root, width=30)
list_box.grid(row=3, column=1, rowspan=4)

read()

root.mainloop()
