#soal 1: tunjangan hari raya (thr) karyawan

#input dari user
lama_kerja = int(input("masukkan lama kerja dalam bulan: "))
gaji_pokok = float(input("masukkan gaji pokok: "))

#proses perhitungan thr
if lama_kerja >= 12:
    thr = gaji_pokok
else:
    thr = (lama_kerja / 12) * gaji_pokok

#output hasil perhitungan
print("thr yang diterima adalah: ", round(thr, 2))
