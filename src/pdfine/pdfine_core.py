
from tkinter import filedialog, messagebox
from pathlib import Path
from pypdf import PdfWriter
from pdfine.pdfine_merge import pdfs_merger
from pdfine.pdfine_compress import pdfs_compressor

# Import for test code.
# from pathlib import Path

file_list = []


def file_size(list_item_index):
    selected_item_size = 0

    if file_list:
        selected_item = file_list[list_item_index]
        selected_item_size = Path(selected_item).stat().st_size

    return selected_item_size


def get_total_file_size():
    total_size = 0

    if file_list:
        for file in file_list:
            total_size += Path(file).stat().st_size

    return total_size


def add_files():
    files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF Files", "*.pdf")]
    )

    for file in files:
        file_list.append(file)
    return files


def merge_pdfs():
    merge_stat = False

    if not file_list:
        messagebox.showwarning("No Files", "Please add PDF files first.")
        return merge_stat

    output_file = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        title="Save Merged PDF As"
    )

    if output_file:
        merge_stat = True
        merger = PdfWriter()
        pdfs_merger(merger, file_list)
        merger.write(output_file)
        merger.close()
        messagebox.showinfo("Success", f"Merged PDF saved as:\n{output_file}")

    return merge_stat

def compress_pdfs():
    compress_stat = False

    if not file_list:
        messagebox.showwarning("No Files", "Please add PDF files first.")
        return compress_stat

    for pdf in file_list:
        compress = PdfWriter(clone_from=pdf)
        pdfs_compressor(compress)

        output_file = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF Files", "*.pdf")],
                title="Save Compressed PDF As"
            )

        if output_file:
            compress_stat = True
            compress.write(output_file)

    return compress_stat


def delete_list_item(selected_item):
    # Test code log output to console
    # for i in file_list:
    #     print(Path(i).name)
    # print("")

    # item_index = selected_item[0]
    # del file_list[selected_item]
    file_list.pop(selected_item)

    # Test code log output to console
    # for r in file_list:
    #     print(Path(r).name)
    return file_list


def clear_list():
    if file_list:
        file_list.clear()