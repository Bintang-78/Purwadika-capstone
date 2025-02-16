# 1. Mengubah string menjadi integer dan menambahkannya dengan angka tetap
angka_str = input("Masukkan angka dalam bentuk string: ")
angka_int = int(angka_str)
hasil_penjumlahan = angka_int + 10
print(f"Hasil penjumlahan {angka_int} + 10 adalah {hasil_penjumlahan}")

# 2. Mengonversi input pengguna dari desimal ke bilangan bulat dan bilangan pecahan
angka_desimal = input("Masukkan angka dalam bentuk desimal: ")
angka_desimal = angka_desimal.replace(",", ".")  # Mengganti koma dengan titik jika ada
angka_float = float(angka_desimal)
angka_integer = int(angka_float)  # Konversi ke integer setelah menjadi float

print(f"Bilangan bulat: {angka_integer}")
print(f"Bilangan pecahan: {angka_float}")