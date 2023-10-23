from tkinter import *

root = Tk()
root.title('Address Book')
root.geometry('800x600')


class PhoneEntry:
    name = ''
    phoneNr = ''

dataList = []

# FUNCTONS


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
            listBox.insert(listbox_index, pe.name)
            listbox_index += 1

# Add Button Function

def add():
    global nameEntry
    global phoneNumberEntry

    pe = PhoneEntry()
    pe.name = nameEntry.get()
    pe.phoneNr = phoneNumberEntry.get()
    dataList.append(pe)
    with open('data.txt', 'r', encoding='utf-8') as file:
        no_name_lines = 0
        for line in file:
            if 'no name' in line:
                no_name_lines += 1

    with open('data.txt', 'a', encoding='utf-8') as file:
        if pe.name != '' and pe.phoneNr != '':
            file.write(pe.name + ',' + pe.phoneNr + '\n')
            listBox.insert(len(dataList) + 1, pe.name)
        elif pe.name != '' and pe.phoneNr == '':
            file.write(pe.name + ',' + 'no phone number' + '\n')
            listBox.insert(len(dataList) + 1, pe.name)
        else:
            file.write('no name' + str(no_name_lines + 1) + ',' + pe.phoneNr + '\n')
            listBox.insert(len(dataList) + 1, 'no name' + str(no_name_lines + 1))

    nameEntry.delete(0, END)
    phoneNumberEntry.delete(0, END)
    nameEntry.focus()


# View Button Function
def view():
    global nameEntry
    global phoneNumberEntry

    with open('data.txt', 'r', encoding='utf-8') as file:
        for line in file:
            columns = line.split(',')
            pe = PhoneEntry()
            pe.name = columns[0]
            pe.phoneNr = columns[1]
            for i in listBox.curselection():
                if listBox.get(i) == pe.name:
                    print(listBox.get(i))
                    nameEntry = Entry(root, width=30)
                    nameEntry.insert(0, pe.name)
                    nameEntry.grid(row=0, column=1)
                    phoneNumberEntry = Entry(root, width=30)
                    phoneNumberEntry.insert(0, pe.phoneNr)
                    phoneNumberEntry.grid(row=1, column=1)




# Widgets Column 0


nameLabel = Label(root, text='Name')
nameLabel.grid(row=0, column=0)

phoneNumberLabel = Label(root, text='Phone No.')
phoneNumberLabel.grid(row=1, column=0)

# addressLabel = Label(root, text='Address')
# addressLabel.grid(row=2, column=0)

addButton = Button(root, text='Add', command=add, padx=5, pady=5)
addButton.grid(row=3, column=0)

viewButton = Button(root, text='View', command=view, padx=5, pady=5)
viewButton.grid(row=4, column=0)

deleteButton = Button(root, text='Delete', padx=5, pady=5)
deleteButton.grid(row=5, column=0)

resetButton = Button(root, text='Reset', padx=5, pady=5)
resetButton.grid(row=6, column=0)

# Widgets Column 1

nameEntry = Entry(root, width=30)
nameEntry.grid(row=0, column=1)

phoneNumberEntry = Entry(root, width=30)
phoneNumberEntry.grid(row=1, column=1)

# addressEntry = Text(root, width=30, height=10)
# addressEntry.grid(row=2, column=1)

listBox = Listbox(root, width=30)
listBox.grid(row=3, column=1, rowspan=4)

read()

root.mainloop()
