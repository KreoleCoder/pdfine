# PDFine

[![PyPI - Version](https://img.shields.io/pypi/v/pdfine?label=pypi%20package&labelColor=green&color=8A2BE2)](https://pypi.org/project/pdfine)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pdfine?labelColor=green&color=8A2BE2)](https://pypi.org/project/pdfine)
[![PyPI License](https://img.shields.io/pypi/l/pdfine?labelColor=green&color=8A2BE2)](https://pypi.org/project/pdfine)
[![PyPI Wheel](https://img.shields.io/pypi/wheel/pdfine?style=plastic&labelColor=green&color=8A2BE2)](https://pypi.org/project/pdfine/#files)
-----

## Table of Contents

- [Overview](#overview) 
- [Installation](#installation)
- [Usage](#usage) 
- [Disclaimer](#disclaimer)
- [License](#license)

---

## Overview

PDFine is a Free Libre and Open Source PDF editor that enables users to merge and compress PDF files via a desktop graphical
interface. Built with Python, it provides a lightweight alternative to expensive PDF manipulation software by leveraging the
PyPDF library for PDF operations.

### Why PDFine

PDFine is the combination of:
- PDF: Portable Document Format; and 
- (F)ine: As in ReFined or ReFiner 

PDFine is **for now, ver simple**, it does one thing (well actually two things :) ), and try to do it well, it **merges** multiple PDF
files into one single PDF file and, it **compresses** one or multiple PDF files.

---

## Installation

### Prerequisites

- `python` 3.8 or higher
- `pip` or `pipx` package manager

> [!NOTE]  
> On some Linux distros you will be required to install `tkinter` python's standard built-in GUIs library.

> ### Recommended
> 
>
>```console
>pipx install pdfine
>```
>***This installs PDFine in an isolated environment, preventing dependency conflicts.***

> ### Alternative
>```console
>pip install pdfine
>```  

> ### Standalone installer for Window  
> Coming soon

---

## Usage

> Open pdfine app interface, it looks like this.

![main](https://github.com/KreoleCoder/pdfine/blob/82e3d49470a2671de61a7699b7ef8b72702462e6/asset/doc/img/main_window.png)

> There are two menu option `File` and `Edit` </br>
> 
> To add a file or multiple files select the `File` option and chose `Add`

![file](https://github.com/KreoleCoder/pdfine/blob/82e3d49470a2671de61a7699b7ef8b72702462e6/asset/doc/img/add_file.png)

> Now to Merge multiple PDF files into one single PDF file, select the `Edit`
> option and chose `Merge`.

![merge](https://github.com/KreoleCoder/pdfine/blob/82e3d49470a2671de61a7699b7ef8b72702462e6/asset/doc/img/merge_files.png)

> There is also the option of compressing one or more PDF files, to achieve
> this, go to `Edit` and select `Compress`</br>

![compress](https://github.com/KreoleCoder/pdfine/blob/82e3d49470a2671de61a7699b7ef8b72702462e6/asset/doc/img/compress_files.png)

> [!IMPORTANT]  
> Always make sure PDF file is already added before merging or compressing.

---

## Disclaimer

This project uses AI as a **productivity tool** limited to documentation,
commit message and a small portion of code mainly use for sampling the design
of the GUI. The final content has been reviewed, modified as needed, and
validated by the author through the project's development and testing process.

### Use of AI-assisted content

- **Documentation** - approximately ***10%*** of documentation was assisted
by AI.  
- **Commit Message** - approximately ***10%*** of commit messages was assisted by AI.  
- **Code** - approximately ***3%*** of the source code was **assisted** by AI
and **used only for the design sample of the GUI** which was overall 
edited/changed by human. **(Actual AI-assisted source code is <1%)**.  

> [!NOTE]   
> Note that the commit message, code, ect, has not been written with AI,
> but only consulted for best practices, use case, and samples.  
> The documentation of this project on the other hand, is being written with
> the help of AI (the Docs not the README). It was giving to copilot within
> the Repo to have it generated (pending review and release).  
> 
> **Also note that all AI-assisted and generated material has undergone human
> review, editing, testing, and approval before release**.  

---

## License

`pdfine` is distributed under the terms of the [GPL-2.0-only](https://spdx.org/licenses/GPL-2.0-only.html) license.

---