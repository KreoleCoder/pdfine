
import tkinter as tk
from pathlib import Path
from pdfine.pdfine_core import add_files, merge_pdfs, compress_pdfs, clear_list

#asset relative path settings
# icon_dir = Path("../../asset/icon")

#get the absolute path of the module
base_dir = Path(__file__).resolve().parent

#Set the absolute path for the asset/icon resources
icon_dir = Path(Path(base_dir.parent).parent, "asset", "icon")

main = tk.Tk()
main.title("PDFine")
main.config(bg="#E4E2E2")
main.geometry("700x350")  # size can be 500x415
main.update_idletasks()

geometryX = 500
geometryY = 100

# This line is used to make the main window non-resizable
# main.resizable(False, False)

# --- Custom Window Icon ---
# Use a .png or .ico file
pdfine_favicon = tk.PhotoImage(file=icon_dir / "pdfine-icon-81x81.png")  # Replace with your file path
main.iconphoto(True, pdfine_favicon)

main.geometry("+%d+%d" % (geometryX, geometryY))


def file_adder():
    file_list = add_files()
    for file in file_list:
        listbox.insert(tk.END, file)


def wipe_list():
    clear_list()
    listbox.delete(0, tk.END)


menu = tk.Menu(main)
main.config(menu=menu)
menu_0 = tk.Menu(menu, tearoff=0)
menu_0.add_command(label="Add", command=file_adder)
menu_0.add_command(label="Clear", command=wipe_list)
menu_0.add_command(label="Exit", command=main.quit)
menu.add_cascade(label="File", menu=menu_0)
menu_1 = tk.Menu(menu, tearoff=0)
menu_1.add_command(label="Merge", command=merge_pdfs)
menu_1.add_command(label="Compress", command=compress_pdfs)
menu.add_cascade(label="Edit", menu=menu_1)

# Listbox to show selected files
listbox = tk.Listbox(master=main)  # size width=70, height=20
listbox.config(bg="#EDECEC", fg="#000", bd=1, font=("Arial", 13, "bold"), selectmode="browse")
listbox.place(x=0, y=0, width=700, height=350)


# Use to add buttons for merge and compress

# merge = tk.Button(master=main, text="Merge")
# merge.config(bg="#E4E2E2", fg="#000", bd=1, relief=tk.RAISED)
# merge.place(x=90, y=194, width=80, height=40)

# compress = tk.Button(master=main, text="Compress")
# compress.config(bg="#E4E2E2", fg="#000", bd=1, relief=tk.RAISED)
# compress.place(x=171, y=194, width=80, height=40)


def gui_app():
    main.mainloop()

if __name__ == "__main__":
    gui_app()
