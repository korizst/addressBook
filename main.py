from tkinter import *

root = Tk()
root.title('Address Book')
root.geometry('800x600')

# Widgets Column 0

nameLabel = Label(root, text='Name')
nameLabel.grid(row=0, column=0)

phoneNumberLabel = Label(root, text='Phone No.')
phoneNumberLabel.grid(row=1, column=0)

addressLabel = Label(root, text='Address')
addressLabel.grid(row=2, column=0)

addButton = Button(root, text='Add')
addButton.grid(row=3, column=0)

viewButton = Button(root, text='View')
viewButton.grid(row=4, column=0)

deleteButton = Button(root, text='Delete')
deleteButton.grid(row=5, column=0)

resetButton = Button(root, text='Reset')
resetButton.grid(row=6, column=0)

# Widgets Column 1

nameEntry = Entry(root, width=30)
nameEntry.grid(row=0, column=1)

phoneNumberEntry = Entry(root, width=30)
phoneNumberEntry.grid(row=1, column=1)

addressEntry = Text(root, width=30, height=10)
addressEntry.grid(row=2, column=1)

dataLabel = Label(root, width=20, height=10, borderwidth=1, relief='solid')
dataLabel.grid(row=3, column=1, rowspan=4)

root.mainloop()
