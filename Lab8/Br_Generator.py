import csv
import os
from datetime import datetime
from tkinter import *
from tkinter import messagebox

import barcode
from barcode.writer import ImageWriter

s = 0
# Creating the base window for the GUI
window = Tk()
window.resizable(width=False, height=False)
window.eval('tk::PlaceWindow . center')
window.title("Bar Code Generator")
window.geometry("1920x1080")



####################GENERATED OUTPUTS INTO CSV FILE####################

# fucn to store data in csv files
def storedata():
    if not os.path.isfile(os.getcwd() + "\\Barcode Datas.csv"):
        with open("Barcode Datas.csv", "w", newline="") as codes:
            fields = ["Subject", "Type", "Timestamp"]
            writer = csv.DictWriter(codes, fieldnames=fields)
            writer.writeheader()
    with open("Barcode Datas.csv", "a", newline="") as codes:
        writer = csv.writer(codes)
        writer.writerow([Subject.get(), "Barcode", timestampStr2])


####################BARCODE GENERATOR####################

# func to generate Barcode
def bargenerate():
    if len(name.get()) != 0 and name.get() != "Enter filename here" and len(
            Subject.get()) != 0 and Subject.get() != "Enter subject here":
        if '/' not in name.get():
            global brcode, fpath, type1, timestampStr2
            brcode = barcode.get("code128", Subject.get(), writer=ImageWriter())
            brcodesvg = barcode.get("code128", Subject.get())
            dummy = os.getcwd() + "\\images"
            if not os.path.exists(dummy):
                os.makedirs(dummy)
            fpath = os.path.join(dummy, name.get())
            brcode.save(fpath)
            dateTimeObj = datetime.now()
            timestampStr2 = dateTimeObj.strftime("%d-%b-%Y (%I:%M:%S.%p)")
            type1 = 2
            storedata()
            try:
                showbrcode()
            except:
                pass
        else:
            messagebox.showinfo("", "filename can't contains '/'")
    else:
        messagebox.showinfo("", "Please Enter some filename or subject")

####################BARCODE INTO PNG####################

# func to save barcode in png format
def brsave():
    try:
        if len(name.get()) != 0 and name.get() != "Enter filename here":
            dir = "Bar_Codes"
            if not os.path.exists(dir):
                os.makedirs(dir)
            spath = os.path.join(dir, name.get())
            brcode.save(spath)
            os.remove(fpath + ".png")
            messagebox.showinfo("", "Barcode saved in png format")
        else:
            messagebox.showinfo("", "Please enter a File Name")
    except:
        messagebox.showinfo("", "Generate the Bar code first!")



# func to show barcode
def showbrcode():
    global photo1
    photo1 = PhotoImage(file=fpath + ".png")
    imageLabel.config(image=photo1)
    subLabel.config(text="")


# dummy func
def dummy():
    try:
        if len(name.get()) != 0 and Subject.get() != "Enter subject here" and name.get() != "Enter filename here":
            messagebox.showinfo("", "Select size")
        else:
            messagebox.showinfo("", "Please enter a File Name")
    except:
        messagebox.showinfo("", "Generate the bar code first!")


# func to clear out any entry boxes when the user shifts focus
def clear_widget(event):
    if SubEntry == window.focus_get() and SubEntry.get() == "Enter subject here":
        SubEntry.delete(0, END)
    elif nameEntry == window.focus_get() and nameEntry.get() == "Enter filename here":
        nameEntry.delete(0, END)


# func to repopulate the default text previously inside the entry boxes if nothing is putin
# while focused and changes focus to another widget
def repopulate_defaults(event):
    if SubEntry != window.focus_get() and SubEntry.get() == "":
        SubEntry.insert(0, "Enter subject here")
    elif nameEntry != window.focus_get() and nameEntry.get() == "":
        nameEntry.insert(0, "Enter filename here")


####################BARCODE GENERATOR GUI####################

# designing the GUI
f = Frame(window)
f.grid(row=0, column=0, sticky=N + S + W + E)

Subject = StringVar()
SubEntry = Entry(f, textvariable=Subject, width=50, font=("Arial", 12),justify='center')
SubEntry.grid(row=0, column=0, columnspan=5, sticky=N + S + W + E)
SubEntry.insert(END, "Enter student name")
SubEntry.bind("<FocusOut>", repopulate_defaults)
SubEntry.bind("<FocusIn>", clear_widget)

name = StringVar()
nameEntry = Entry(f, textvariable=name, width=50, font=("Arial", 12),justify='center')
nameEntry.grid(row=1, column=0, columnspan=5, sticky=N + S + W + E)
nameEntry.insert(0, "Enter Filename Here")
nameEntry.bind("<FocusOut>", repopulate_defaults)
nameEntry.bind("<FocusIn>", clear_widget)

f2 = Frame(window)
f2.grid(row=2, column=0, sticky=N + S + W + E)

s1 = Button(f2, text="Generate Barcode", width=15, bd=5, command=bargenerate, font=("Arial", 12, 'bold'))
s1.grid(row=0, column=3, sticky=N + S + W + E)


s1 = Button(f2, text="Save", width=9,bd=5, command=brsave, font=("Arial", 12,'bold'))
s1.grid(row=0, column=4, sticky=N + S + W + E)

imageLabel = Label(window)
imageLabel.grid(row=5, column=0, sticky=N + S + W + E)

subLabel = Label(window, text="")
subLabel.grid(row=6, column=0, sticky=N + S + W + E)

# making the GUI resposnsive
Rows = 6
Columns = 4

for row in range(Rows + 1):
    window.grid_rowconfigure(row, weight=1)

for col in range(Columns + 1):
    window.grid_columnconfigure(col, weight=1)

# looping the GUI
window.mainloop()