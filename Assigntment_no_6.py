# Program Kasir Sederhana untuk Toko Kelontong

def calculate_discount(total):
    if total > 200000:
        return 0.2  # Diskon 20%
    elif total > 100000:
        return 0.1  # Diskon 10%
    return 0.0  # Tidak ada diskon

# Meminta jumlah jenis barang
jumlah_barang = int(input("Masukkan jumlah jenis barang yang dibeli: "))

daftar_belanja = []
total_belanja = 0

# Input barang
for i in range(jumlah_barang):
    print(f"\nBarang ke-{i+1}:")
    nama = input("Nama barang: ")
    harga = int(input("Harga per unit (Rp): "))
    jumlah = int(input("Jumlah yang dibeli: "))
    subtotal = harga * jumlah
    daftar_belanja.append((nama, harga, jumlah, subtotal))
    total_belanja += subtotal

# Menghitung diskon
diskon_persen = calculate_discount(total_belanja)
diskon = total_belanja * diskon_persen
total_setelah_diskon = total_belanja - diskon

# Menampilkan daftar belanja
print("\nDaftar Belanja:")
for item in daftar_belanja:
    print(f"{item[0]} - {item[1]} x {item[2]} = Rp{item[3]}")

print(f"\nTotal belanja sebelum diskon: Rp{total_belanja}")
if diskon > 0:
    print(f"Diskon ({diskon_persen * 100}%): Rp{diskon}")
print(f"Total belanja setelah diskon: Rp{total_setelah_diskon}")

# Memastikan pembayaran cukup
while True:
    uang_dibayarkan = int(input("Masukkan jumlah uang yang dibayarkan: "))
    if uang_dibayarkan >= total_setelah_diskon:
        kembalian = uang_dibayarkan - total_setelah_diskon
        print(f"Pembayaran berhasil! Kembalian: Rp{kembalian}")
        break
    else:
        print("Uang yang dimasukkan kurang, silakan coba lagi.")
