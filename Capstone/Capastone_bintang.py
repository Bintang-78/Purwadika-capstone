students = []  # Menyimpan data nilai siswa dalam list

def create_student():
    name = input("Masukkan nama siswa: ")
    score = float(input("Masukkan nilai siswa: "))
    students.append({"name": name, "score": score})
    print("Data siswa berhasil ditambahkan!\n")

def read_students():
    if not students:
        print("Data siswa kosong.\n")
    else:
        print("Daftar Nilai Siswa:")
        for idx, student in enumerate(students, start=1):
            print(f"{idx}. {student['name']} - {student['score']}")
        print()

def update_student():
    name = input("Masukkan nama siswa yang ingin diubah nilainya: ")
    for student in students:
        if student['name'] == name:
            new_score = float(input("Masukkan nilai baru: "))
            student['score'] = new_score
            print("Nilai siswa berhasil diperbarui!\n")
            return
    print("Siswa tidak ditemukan.\n")

def delete_student():
    name = input("Masukkan nama siswa yang ingin dihapus: ")
    for student in students:
        if student['name'] == name:
            students.remove(student)
            print("Data siswa berhasil dihapus!\n")
            return
    print("Siswa tidak ditemukan.\n")

def main_menu():
    while True:
        print("\nMenu Utama:")
        print("1. Tambah Data Siswa")
        print("2. Lihat Data Siswa")
        print("3. Ubah Nilai Siswa")
        print("4. Hapus Data Siswa")
        print("5. Keluar")
        choice = input("Pilih menu (1-5): ")
        
        if choice == '1':
            create_student()
        elif choice == '2':
            read_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")


main_menu()
