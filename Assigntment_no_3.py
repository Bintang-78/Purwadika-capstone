# 1. Menentukan kategori usia
umur = int(input("Masukkan umur: "))
if umur < 13:
    kategori = "Anak-anak"
elif 13 <= umur <= 19:
    kategori = "Remaja"
elif 20 <= umur <= 59:
    kategori = "Dewasa"
else:
    kategori = "Lansia"
print(f"Kategori usia: {kategori}")

# 2. Menentukan apakah angka positif/negatif dan genap/ganjil
angka = int(input("Masukkan angka: "))
if angka > 0:
    status = "Positif"
elif angka < 0:
    status = "Negatif"
else:
    status = "Nol"

if angka % 2 == 0:
    jenis = "Genap"
else:
    jenis = "Ganjil"

print(f"Angka {angka} adalah {status} dan {jenis}.")