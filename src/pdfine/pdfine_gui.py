
import tkinter as tk
# from tkinter import filedialog, messagebox
from pdfine_merge import add_files


main = tk.Tk()
main.title("PDFine")
main.config(bg="#E4E2E2")
main.geometry("700x350") # size can be 500x415
main.update_idletasks()

geometryX = 500
geometryY = 100

main.geometry("+%d+%d"%(geometryX, geometryY))

def file_adder():
    file_list = add_files()
    for file in file_list:
        listbox.insert(tk.END, file)

menu = tk.Menu(main)
main.config(menu=menu)
menu_0 = tk.Menu(menu, tearoff=0)
menu_0.add_command(label="Add", command=file_adder)
menu_0.add_command(label="Clear", command=lambda: print("Clear clicked"))
menu_0.add_command(label="Exit", command=lambda: print("Exit clicked"))
menu.add_cascade(label="File", menu=menu_0)
menu_1 = tk.Menu(menu, tearoff=0)
menu_1.add_command(label="Merge", command=lambda: print("Merge clicked"))
menu_1.add_command(label="Compress", command=lambda: print("Compress clicked"))
menu.add_cascade(label="Edit", menu=menu_1)


# Listbox to show selected files
listbox = tk.Listbox(master=main) # size width=70, height=20
listbox.config(bg="#EDECEC", fg="#000", bd=1, font=("Arial", 13, "bold"),selectmode="browse")
listbox.place(x=0, y=0, width=700, height=350)



# Use to add buttons for merge and compress

# merge = tk.Button(master=main, text="Merge")
# merge.config(bg="#E4E2E2", fg="#000", bd=1, relief=tk.RAISED)
# merge.place(x=90, y=194, width=80, height=40)

# compress = tk.Button(master=main, text="Compress")
# compress.config(bg="#E4E2E2", fg="#000", bd=1, relief=tk.RAISED)
# compress.place(x=171, y=194, width=80, height=40)




main.mainloop()