# PDFine

[![PyPI - Version](https://img.shields.io/pypi/v/pdfine?label=pypi%20package&labelColor=green&color=8A2BE2)](https://pypi.org/project/pdfine)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pdfine?labelColor=green&color=8A2BE2)](https://pypi.org/project/pdfine)
[![PyPI License](https://img.shields.io/pypi/l/pdfine?labelColor=green&color=8A2BE2)](https://pypi.org/project/pdfine)
[![PyPI Wheel](https://img.shields.io/pypi/wheel/pdfine?style=plastic&labelColor=green&color=8A2BE2)](https://pypi.org/project/pdfine/#files)
-----

## Table of Contents

- [Overview](#overview) 
- [Installation](#installation)
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

PDFine is **for now, ver simple**, it does one thing (well actually two things :)), and try to does it well, it **merges** multiple PDF
files into one single PDF file and, it **compresses** one or multiple PDF files.

---

## Installation

### Prerequisites

- `python` 3.8 or higher
- `pip` or `pipx` package manager

> [!NOTE] On some Linux distros you will be required to install `tkinter` python's standard built-in GUIs library.

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

---

## License

`pdfine` is distributed under the terms of the [GPL-2.0-only](https://spdx.org/licenses/GPL-2.0-only.html) license.

---