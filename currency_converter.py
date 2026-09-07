#soal nomor 3

#data kurs: 'mata uang' : [harga beli, harga jual]
kurs = {
    "AUD": [9810, 9840],
    "CNY": [2048, 2055],
    "EUR": [15865, 15895],
    "GBP": [17630, 17700],
    "HKD": [1810, 1817],
    "JPY": [129.90, 130.60],
    "MYR": [3430, 3450],
    "SAR": [3750, 3770],
    "SGD": [10390, 10410],
    "USD": [14130, 14160]
}

#input dari pengguna
transaksi = input("jenis transaksi (buy/sale): ").lower()
mata_uang = input("mata uang (contoh: USD, SGD, EUR): ").upper()
jumlah = float(input("jumlah uang: "))

#validasi kurs tersedia
if mata_uang not in kurs:
    print("mata uang tidak ditemukan.")
else:
    beli, jual = kurs[mata_uang]
    
    if transaksi == "buy":
        hasil = jumlah * beli
        print(f"hasil konversi: {hasil:.2f} IDR")
    elif transaksi == "sale":
        hasil = jumlah / jual
        print(f"hasil konversi: {hasil:.2f} {mata_uang}")
    else:
        print("jenis transaksi tidak valid.")
