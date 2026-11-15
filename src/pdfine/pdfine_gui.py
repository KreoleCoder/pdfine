
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from pdfine.pdfine_core import add_files, merge_pdfs, compress_pdfs, clear_list, delete_list_item, get_total_file_size, file_size

#asset relative path settings
# icon_dir = Path("../../asset/icon")

#get the absolute path of the module
base_dir = Path(__file__).resolve().parent

#Set the absolute path for the asset/icon resources
icon_dir = Path(Path(base_dir.parent).parent, "asset", "icon")

main = tk.Tk(className="PDFine")
main.title("PDFine")

# --- Custom Window Icon ---
# Use a .png or .ico file
pdfine_favicon = tk.PhotoImage(file=icon_dir / "pdfine-icon-81x81.png")  # Replace with your file path
main.iconphoto(True, pdfine_favicon)

main.config(bg="#E4E2E2")
main.geometry("980x580")  # size can be 500x415 | 700x350 | 980x580
main.update_idletasks()

# Help to set where the window will appear
geometryX = 500
geometryY = 100
main.geometry("+%d+%d" % (geometryX, geometryY))

# This line is used to make the main window non-resizable
main.resizable(False, False)

def file_adder():
    file_list = add_files()
    for file in file_list:
        listbox.insert(tk.END, Path(file).name)

    # listbox.get(0, tk.END)
    total_file_size = get_total_file_size()
    status_bar.config(text=f" {len(listbox.get(0, tk.END))} file(s) - ({(total_file_size/1000**2):.2f} MB) ")


def item_deletion():
    try:
        selected_item = listbox.curselection()[0]
        # Test code log output to console
        # print(selected_item)
        # if selected_item >= 0:
        listbox.delete(selected_item)
        files = delete_list_item(selected_item)
        total_file_size = get_total_file_size()
        status_bar.config(text=f" {str(len(files))} file(s) - ({(total_file_size/1000**2):.2f} MB) ")

    except IndexError:
        messagebox.showwarning("No File Selected", "Please select a file to delete")


def wipe_list():
    clear_list()
    listbox.delete(0, tk.END)
    status_bar.config(text=f" {len(listbox.get(0, tk.END))} file(s) ")


# Left click event handler function
# Clear selected item and update the status bar
def left_click(event):
    selected_index = listbox.curselection()
    if selected_index:
        listbox.selection_clear(0, tk.END)
        total_file_size = get_total_file_size()
        status_bar.config(text=f" {len(listbox.get(0, tk.END))} file(s) - ({(total_file_size / 1000 ** 2):.2f} MB) ")


# Right click event handler function
def right_click(event):
    context_menu.tk_popup(event.x_root, event.y_root)


# Escape Key event handler function
# Clear selected item and update the status bar
def clear_selected_item(event):

    if len(listbox.get(0, tk.END)) > 0:
        listbox.selection_clear(0, tk.END)
        total_file_size = get_total_file_size()
        status_bar.config(text=f" {len(listbox.get(0, tk.END))} file(s) - ({(total_file_size / 1000 ** 2):.2f} MB) ")

    else:
        status_bar.config(text=f" {len(listbox.get(0, tk.END))} file(s) ")


# Listbox items selection event handler function
# Update the Status Bar.
def status_bar_updater(event):
    selected_index = listbox.curselection()

    if selected_index:
        list_item_index = selected_index[0]
        selected_item = listbox.get(list_item_index)
        item_size = file_size(list_item_index)
        status_bar.config(text=f"{selected_item} ({(item_size/1000**2):.2f} MB) ")

    else:
        total_file_size = get_total_file_size()
        status_bar.config(text=f" {len(listbox.get(0, tk.END))} file(s) - ({(total_file_size/1000**2):.2f} MB) ")



menu = tk.Menu(main)
main.config(menu=menu)
menu_0 = tk.Menu(menu, tearoff=0)
menu_0.add_command(label="Add", command=file_adder)
menu_0.add_command(label="Clear", command=wipe_list)
menu_0.add_separator()
menu_0.add_command(label="Exit", command=main.quit)
menu.add_cascade(label="File", menu=menu_0)
menu_1 = tk.Menu(menu, tearoff=0)
menu_1.add_command(label="Merge", command=merge_pdfs)
menu_1.add_command(label="Compress", command=compress_pdfs)
menu_1.add_separator()
menu_1.add_command(label="Delete", command=item_deletion)
menu.add_cascade(label="Edit", menu=menu_1)


# Listbox to show selected files
listbox = tk.Listbox(master=main)  # size width=70, height=20
listbox.config(bg="#EDECEC",
               fg="#000",
               font=("Arial", 13, "bold"),
               selectmode="browse",
               selectbackground="#8453ED",
               selectforeground="white")
# listbox.place(x=0, y=0, width=700, height=350)
listbox.pack(fill="both", expand=True)


# menu use for mouse right click action
context_menu = tk.Menu(main, tearoff=0, font=("Arial", 11))
context_menu.add_command(label="Delete", command=item_deletion)


# Binding left click action to the listbox area
listbox.bind("<Button-1>", left_click)

# Binding right click action to the listbox area
listbox.bind("<Button-3>", right_click)

# Binding listbox selected item to the listbox area
listbox.bind("<<ListboxSelect>>", status_bar_updater)

# Binding the Escape Key to the listbox selected item
listbox.bind('<Escape>', clear_selected_item)

#Status Bar
status_bar = tk.Label(main, text= f" ", bd=1, relief= "sunken", anchor="n", bg="#EDECEC")
status_bar.pack(fill="x", side="left", ipadx= 80)

status_bar_b = tk.Label(main, text= f" PDFine", bd=1, relief= "sunken", anchor="n", bg="#EDECEC")
status_bar_b.pack(fill="x", side="right", ipadx= 80)


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
