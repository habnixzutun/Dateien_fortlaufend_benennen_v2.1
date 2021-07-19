import os
import random
from tkinter import *
from tkinter import filedialog
import psutil

chars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16]


def start():
    if r.get() == "original" and directorypath_entry.get() != "":
        rename_files_original(directorypath_entry.get())
    elif r.get() != "original" and directorypath_entry.get() != "" and r.get() != "remove_doubles":
        rename_files_everything(directorypath_entry.get(), r.get())
    else:
        return


def rename_files_original(dateipfad):
    os.chdir(dateipfad)
    try:
        files = os.listdir()
        x = 1
        for i in files:
            _, dateiendung = os.path.splitext(dateipfad + i)
            os.rename(i, "{}{}".format(x, dateiendung))
            x += 1
        files = os.listdir()
        temp = set()
        try:
            for file in files:
                temp.add(open(file, "rb").read())
                if (psutil.virtual_memory()[1]) / 1_000_000_000 < 0.3:
                    _ = int(1j)
            for file in files:
                os.remove(file)
            i = 1
            for file in temp:
                outfile = open(str(f"{i}{dateiendung}"), "wb")
                outfile.write(file)
                outfile.close()
                i += 1
        except:
            _ = int(1)
    except:
        files = os.listdir()
        x = 1
        for i in files:
            temp_name = ""
            waste1, extension = os.path.splitext(dateipfad + i)
            for char in range(10):
                temp_name += str(random.choice(chars))
            os.rename(i, "{}{}{}".format(temp_name, x, extension))
            x += 1
        rename_files_original(dateipfad)


def rename_files_everything(dateipfad, dateiendung):
    os.chdir(dateipfad)
    try:
        files = os.listdir()
        x = 1
        for i in files:
            os.rename(i, "{}{}".format(x, dateiendung))
            x += 1
        files = os.listdir()
        temp = set()
        i = 1
        try:
            for file in files:
                temp.add(open(file, "rb").read())
                if (psutil.virtual_memory()[1]) / 1000000000 < 0.3:
                    _ = int(1j)
            for file in files:
                os.remove(file)
            for file in temp:
                outfile = open(str(f"{i}{dateiendung}"), "wb")
                outfile.write(file)
                outfile.close()
                i += 1
        except:
            _ = int(1)
    except:
        files = os.listdir()
        x = 1
        for i in files:
            temp_name = ""
            for char in range(16):
                temp_name += str(random.choice(chars))
            os.rename(i, "{}{}{}".format(temp_name, x, dateiendung))
            x += 1
        rename_files_everything(dateipfad, dateiendung)


def choose_path():
    path = filedialog.askdirectory()
    directorypath_entry.delete(0, END)
    directorypath_entry.insert(0, path)


root = Tk()
root.title("Dateien fortlaufend benennen")
root.geometry("888x500")

# Tkinter Variables
r = StringVar()
r.set("original")

# row 0
directorypath_label = Label(root, text="Directory path:", font=("Calibri", 12))
directorypath_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
directorypath_entry = Entry(root, width=80, font=("Calibri", 10))
directorypath_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=5)
directorypath_button = Button(root, text="Choose Directory path", font=("Calibri", 12), command=choose_path)
directorypath_button.grid(row=0, column=7, padx=5, pady=5)

# row 1
select_format = Label(root, text="Select a file format", font=("Calibri", 12))
select_format.grid(row=1, column=0, padx=5, pady=(10, 0))

# row 2, original
select_jpg = Radiobutton(root, text="Original", variable=r, value="original", font=("Calibri", 10))
select_jpg.grid(row=2, column=0, sticky="w")


# row 3, Images
select_jpg = Radiobutton(root, text=".jpg", variable=r, value=".jpg", font=("Calibri", 10))
select_jpg.grid(row=3, column=0, sticky="w")
select_png = Radiobutton(root, text=".png", variable=r, value=".png", font=("Calibri", 10))
select_png.grid(row=3, column=1, sticky="w")
select_gif = Radiobutton(root, text=".gif", variable=r, value=".gif", font=("Calibri", 10))
select_gif.grid(row=3, column=2, sticky="w")


# row 4, Videos
select_mp4 = Radiobutton(root, text=".mp4", variable=r, value=".mp4", font=("Calibri", 10))
select_mp4.grid(row=4, column=0, sticky="w")
select_mov = Radiobutton(root, text=".mov", variable=r, value=".mov", font=("Calibri", 10))
select_mov.grid(row=4, column=1, sticky="w")
select_avi = Radiobutton(root, text=".avi", variable=r, value=".avi", font=("Calibri", 10))
select_avi.grid(row=4, column=2, sticky="w")
select_wmv = Radiobutton(root, text=".wmv", variable=r, value=".wmv", font=("Calibri", 10))
select_wmv.grid(row=4, column=3, sticky="w")

# row 5, Documents
select_doc = Radiobutton(root, text=".doc", variable=r, value=".doc", font=("Calibri", 10))
select_doc.grid(row=5, column=0, sticky="w")
select_docx = Radiobutton(root, text=".docx", variable=r, value=".docx", font=("Calibri", 10))
select_docx.grid(row=5, column=1, sticky="w")
select_pdf = Radiobutton(root, text=".pdf", variable=r, value=".pdf", font=("Calibri", 10))
select_pdf.grid(row=5, column=2, sticky="w")
select_xlsx = Radiobutton(root, text=".xlsx", variable=r, value=".xlsx", font=("Calibri", 10))
select_xlsx.grid(row=5, column=3, sticky="w")
select_xls = Radiobutton(root, text=".xls", variable=r, value=".xls", font=("Calibri", 10))
select_xls.grid(row=5, column=4, sticky="w")


rename_button = Button(root, text="Start renaming files", command=start)
rename_button.grid(row=20, column=0, sticky="w", pady=5, padx=5, columnspan=5)


root.mainloop()
