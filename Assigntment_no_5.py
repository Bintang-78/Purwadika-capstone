# 1. List: Memasukkan lima nama teman dan menampilkannya satu per satu
nama_teman = []
for i in range(5):
    nama = input(f"Masukkan nama teman ke-{i+1}: ")
    nama_teman.append(nama)

print("\nDaftar nama teman:")
for nama in nama_teman:
    print(nama)

# 2. Tuple: Menyimpan nama dan tanggal lahir
nama_saya = "Bintang Richardo"
tanggal_lahir = "10 Oktober 2000"
data_diri = (nama_saya, tanggal_lahir)
print(f"\nNama saya {data_diri[0]}, lahir pada {data_diri[1]}.")

# 3. Dictionary: Menyimpan dan menampilkan nama serta umur lima orang
umur_orang = {}
for i in range(5):
    nama = input(f"Masukkan nama orang ke-{i+1}: ")
    umur = int(input(f"Masukkan umur {nama}: "))
    umur_orang[nama] = umur

print("\nData umur:")
for nama, umur in umur_orang.items():
    print(f"Nama: {nama}, Umur: {umur}")

# 4. Set: Menghitung union, intersection, dan subset dua set angka
set1 = set(map(int, input("Masukkan 5 angka untuk set pertama (pisahkan dengan spasi): ").split()))
set2 = set(map(int, input("Masukkan 5 angka untuk set kedua (pisahkan dengan spasi): ").split()))

union_set = set1 | set2
intersection_set = set1 & set2
subset_check = set1.issubset(set2) or set2.issubset(set1)

print(f"\nUnion: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Apakah salah satu set merupakan subset dari yang lain? {subset_check}")
