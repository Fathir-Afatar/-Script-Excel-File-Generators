# Excel File Generator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pandas](https://img.shields.io/badge/pandas-3.1.0-darkgreen.svg)](https://pandas.pydata.org/)
[![OpenPyXL](https://img.shields.io/badge/openpyxl-3.1.5-brightgreen.svg)](https://openpyxl.readthedocs.io/)

> Created by: Fathir Afatar

A lightweight, purely script-based utility designed to automatically generate structured mock Excel datasets mimicking real-world transaction structures. Perfect for testing reconciliation tools, data pipelines, or bulk processing scripts without risking sensitive data or compliance breaches.

---

## 💡 About & Motivation

Manually creating structured Excel files with specific columns, custom transaction codes, and realistic values for testing is tedious, time-consuming, and exhausting. More importantly, using real financial or production data introduces severe privacy risks, potential data leaks, and legal liabilities. 

This tool solves that problem by providing a purely programmatic, headless approach—**no bulky applications, no complex GUI, just clean and efficient Python scripts**. Originally built as a test-data generator for benchmarking the **ReferMatch** reconciliation project, this utility automates data structuring, preserves strict confidentiality, and safely eliminates the need for actual production records during testing.

## ✨ Key Features

* **Multi-Format Mock Generation:** Instantly generates two distinct `.xlsx` files per execution mimicking real financial systems:
  1. **Bank Statement-style File:** Structured like traditional bank transaction histories.
  2. **Virtual Account (VA)-style File:** Formatted to mirror Virtual Account transaction logs.
* **Configurable Parameters:** Easily customize transaction prefixes (e.g., `"CTH"`, `"MSL"`), suffix codes (e.g., `"XYZ"`, `"AHG"`), and custom nominal amounts (e.g., `134000`, `120000`).
* **Headless & Script-Only:** Lightweight execution with zero GUI overhead, built using robust data-processing libraries.

## 🛠️ Tech Stack & Dependencies

Built with **Python** and powered by the following core libraries:

* `pandas = 3.1.0` (Data manipulation and structuring)
* `openpyxl = 3.1.5` & `et_xmlfile = 2.0.0` (Excel file generation engine)
* `numpy = 2.5.4` (Numerical operations and mock value generation)
* `python-dateutil = 4.0.0` & `tzdata = 2026.6` (Date and timezone handling)

## 📦 Getting Started

### Prerequisites

Ensure you have Python installed on your system along with pip.

### Installation

1. Clone or download this repository to your local machine.
```
git clone https://github.com/Fathir-Afatar/-Script-Excel-File-Generators.git
```
2. Create Virtual Enviroment (recomended)
```
python -m venv venv
source venv/bin/activate
```
3. Install the required dependencies:

```bash
pip install requirements.txt
```

## 🚀 Usage

This tool runs as a straightforward command-line script. Before running, you can configure your custom transaction codes, prefixes/suffixes, and nominal parameters directly inside the script variables.

To execute the generator, run:

```bash
python -m dummy_transaksi
```

### Output Structure

Once executed, the script will output two structured mock Excel files ready for your testing and reconciliation workflows:

* Bank transaction ledger file (`.xlsx`)
* Virtual Account transaction log file (`.xlsx`)

## 📜 License
This project is open-source and available under the [MIT License](./LICENSE). You are free to use, modify, and distribute it, provided proper credit is given original author: Fathir Afatar.

## Contributing & Contact

Contributions, suggestions, and feature request are welcome!
- Report bugs or submit pull request on the [GitHub Repository](https://github.com/Fathir-Afatar/pdf-unlocker-by-fathir)

- If you find this project helful, please consider giving a ⭐ on GitHub! 