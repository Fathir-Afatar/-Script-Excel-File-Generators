# Standard Library
import random
import os

# Third-party
import pandas as pd

# Determine the current folder location
output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(output_folder, exist_ok=True)

# Bank style generator
def generate_transaksi_bank(n, starting_saldo=1000000):
    """Generates synthetic bank transaction data and saves it as an Excel file.

    This function simulates a sequence of bank transactions (debits and credits)
    with randomized remarks, amounts, and automatic balance updates. The resulting
    dataset is saved as an Excel spreadsheet in the designated output folder.

    Args:
        n (int): The number of transaction rows to generate.
        starting_saldo (int, optional): The initial bank account balance before 
            any transactions occur. Defaults to 1000000.

    Returns:
        pd.DataFrame: A DataFrame containing the columns 'Remark', 'Tanggal Transaksi',
            'Debit', 'Kredit', and 'Saldo'.

    Raises:
        OSError: If the function fails to open the output folder automatically.
    """
    kode_awal = ["CTH", "MSL", "DMY"]
    suffixes = ["XYZ", "AHG", "RL", "RQE"]
    nominal_set = [135000, 195000, 185000, 165000, 135000, 175000]

    remarks, tanggal_list, debit_list, kredit_list, saldo_list = [], [], [], [], []

    saldo = starting_saldo
    dates = pd.date_range(start="2025-07-01", periods=n, freq="5min")

    for _ in range (n):
        kode = random.choice(kode_awal)
        nomor = str(random.randint(1000000000000, 9999999999999)) # 13 digit angka
        suffix = random.choice(suffixes)
        remark = f"{kode}{nomor}{suffix}IN"
        tansaksi_tipe = random.choices(["debit", "kredit"], weights=[30,70])[0]
        nominal = random.choice(nominal_set)

        if tansaksi_tipe == "debit":
            debit = nominal
            kredit = 0
            saldo += debit
        else:
            debit = 0
            kredit = nominal
            saldo -= kredit

        remarks.append(remark)
        tanggal_list.append(dates[1])
        debit_list.append(debit)
        saldo_list.append(saldo)
        kredit_list.append(kredit)
    
    df_bank = pd.DataFrame({
        "Remark": remarks,
        "Tanggal Transaksi":tanggal_list,
        "Debit": debit_list,
        "Kredit": kredit_list,
        "Saldo": saldo_list
    })

    # Save to the "data" folder
    path_bank = os.path.join(output_folder, "transaksi.xlsx")
    df_bank.to_excel(path_bank, index=False)
    print("Transaction file.xlsx was successfully created in:", path_bank)

    # Automatically open output folder
    os.startfile(output_folder)

    return df_bank

def generate_referensi_from_kredit(df_bank):
    """Extracts credit transactions to create an order reference spreadsheet.

    Filters the provided bank transaction DataFrame for rows where credit actions
    occurred, extracts the 13-digit numeric code from the 'Remark' column, and 
    saves the compiled information into an Excel file.

    Args:
        df_bank (pd.DataFrame): The source bank transaction DataFrame containing 
            at least 'Kredit', 'Remark', and 'Tanggal Transaksi' columns.

    Returns:
        None
    """
    referensi = []
    jumlah_list = []
    tanggal_list = []

    for _, row in df_bank.iterrows():
        if row["Kredit"] > 0:
            nomor = ''.join(filter(str.isdigit, row["Remark"])) # Take number from Remark

            if len(nomor) >=13:
                referensi.append(nomor[:13]) # Cut to 13 digit

                jumlah_list.append(row["Kredit"])
                tanggal_list.append(row["Tanggal Transaksi"])

    df_referensi = pd.DataFrame({
        "Nomor Referensi": referensi,
        "Tanggal Order": tanggal_list,
        "Total Harga": jumlah_list
    })


    path_ref = os.path.join(output_folder, "referensi.xlsx")
    df_referensi.to_excel(path_ref, index=False)
    print("Reference file.xlsx was successfully created in:", path_ref)

if __name__ == "__main__":
    df_transaksi = generate_transaksi_bank(n=1000)
    generate_referensi_from_kredit(df_transaksi)

# To generate the dummy excel file
# python -m dummy_transaksi