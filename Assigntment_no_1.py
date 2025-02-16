import math

def hitung_luas_lingkaran():
    radius = float(input("Masukkan jari-jari lingkaran: "))
    luas_lingkaran = math.pi * radius ** 2
    print(f"Luas lingkaran dengan jari-jari {radius} adalah {luas_lingkaran:.2f}")
    print("_____________________________")
    print(" ")

def hitung_statistik():
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    angka3 = float(input("Masukkan angka ketiga: "))
    total = angka1 + angka2 + angka3
    rata_rata = total / 3
    maksimum = max(angka1, angka2, angka3)
    minimum = min(angka1, angka2, angka3)
    print(f"Total: {total}, Rata-rata: {rata_rata:.2f}, Maksimum: {maksimum}, Minimum: {minimum}")
    print("_____________________________")
    print(" ")

def konversi_hari():
    jumlah_hari = int(input("Masukkan jumlah hari: "))
    tahun = jumlah_hari // 365
    sisa_hari = jumlah_hari % 365
    bulan = sisa_hari // 30
    hari = sisa_hari % 30
    print(f"{jumlah_hari} hari = {tahun} tahun, {bulan} bulan, {hari} hari")

def main():
    while True:
        print("Menu:")
        print("1. Hitung luas lingkaran")
        print("2. Hitung total, rata-rata, maksimum, dan minimum")
        print("3. Konversi jumlah hari")
        print("4. Jalankan semua operasi")
        print("5. Keluar")
        pilihan = input("Pilih operasi (1-5): ")
        
        if pilihan == "1":
            hitung_luas_lingkaran()
        elif pilihan == "2":
            hitung_statistik()
        elif pilihan == "3":
            konversi_hari()
        elif pilihan == "4":
            hitung_luas_lingkaran()
            hitung_statistik()
            konversi_hari()
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
        print("\n")

if __name__ == "__main__":
    main()
