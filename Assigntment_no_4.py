# 1. Program menggunakan while loop untuk meminta input angka hingga angka negatif dimasukkan
total = 0
while True:
    angka = int(input("Masukkan angka (masukkan angka negatif untuk berhenti): "))
    if angka < 0:
        break
    total += angka
print(f"Total dari semua angka yang dimasukkan: {total}")

# 2. Menggunakan for loop untuk menghitung total dan rata-rata angka dalam list
angka_list = list(map(int, input("Masukkan angka-angka dalam list, pisahkan dengan spasi: ").split()))
total_list = 0
for angka in angka_list:
    total_list += angka
rata_rata = total_list / len(angka_list) if angka_list else 0
print(f"Total angka dalam list: {total_list}")
print(f"Rata-rata angka dalam list: {rata_rata:.2f}")
