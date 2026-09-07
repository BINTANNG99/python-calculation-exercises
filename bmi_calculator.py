#soal nomor 2

#input berat (kg) dan tinggi (meter)
berat = float(input("masukkan berat badan (kg): "))
tinggi = float(input("masukkan tinggi badan (m): "))

#hitung nilai bmi
bmi = berat / (tinggi ** 2)

#tentukan kategori
if bmi < 18.5:
    kategori = "underweight"
elif bmi < 25:
    kategori = "normal"
elif bmi < 30:
    kategori = "overweight"
else:
    kategori = "obesity"

#tampilkan hasil
print(f"nilai bmi anda: {bmi:.2f}")
print(f"kategori: {kategori}")
