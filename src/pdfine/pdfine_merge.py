
from tkinter import filedialog, messagebox
from pypdf import PdfWriter
from pdfine_compress import pdfs_compressor

file_list = []

def add_files():
    files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF Files", "*.pdf")]
    )

    for file in files:
        file_list.append(file)
    return files


def merge_pdfs():
    if not file_list:
        messagebox.showwarning("No Files", "Please add PDF files first.")
        return

    output_file = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        title="Save Merged PDF As"
    )

    if output_file:
        merger = PdfWriter()
        for pdf in file_list:
            merger.append(pdf)
        merger.write(output_file)
        merger.close()
        messagebox.showinfo("Success", f"Merged PDF saved as:\n{output_file}")

def compress_pdfs():
    if not file_list:
        messagebox.showwarning("No Files", "Please add PDF files first.")
        return

    for pdf in file_list:
        compress = PdfWriter(clone_from=pdf)
        pdfs_compressor(compress)

        output_file = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF Files", "*.pdf")],
                title="Save Compressed PDF As"
            )

        compress.write(output_file)

def clear_list():
    if file_list:
        file_list.clear()