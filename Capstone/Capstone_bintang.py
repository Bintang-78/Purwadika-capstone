students = []  # Menyimpan data nilai siswa dalam list


def create_student():
    while True:
        student_id = input("Masukkan ID Siswa (huruf & angka): ")
        if any(student['id'] == student_id for student in students):
            print("Data already exists! Gunakan ID lain.")
            continue
        break
    
    while True:
        name = input("Masukkan nama siswa: ")
        if not name.replace(" ", "").isalpha():
            print("Nama hanya boleh berisi huruf!")
            continue
        break
    
    while True:
        try:
            score = float(input("Masukkan nilai siswa: "))
            break
        except ValueError:
            print("Nilai harus berupa angka!")
    
    print(f"\nData yang dimasukkan:\nID: {student_id}\nNama: {name}\nNilai: {score}")
    save = input("Simpan data? (y/n): ").strip().lower()
    if save == 'y':
        students.append({"id": student_id, "name": name, "score": score})
        print("Data successfully saved!\n")
    else:
        print("Data tidak disimpan, kembali ke menu utama.\n")


def read_students():
    if not students:
        print("Data siswa kosong.\n")
    else:
        print("Daftar Nilai Siswa:")
        for idx, student in enumerate(students, start=1):
            print(f"{idx}. ID: {student['id']} - {student['name']} - {student['score']}")
        print()


def update_student():
    student_id = input("Masukkan ID siswa yang ingin diubah: ")
    for student in students:
        if student['id'] == student_id:
            while True:
                update_choice = input("Apa yang ingin diubah? (nama/nilai): ").strip().lower()
                if update_choice == "nama":
                    while True:
                        new_name = input("Masukkan nama baru: ")
                        if not new_name.replace(" ", "").isalpha():
                            print("Nama hanya boleh berisi huruf!")
                            continue
                        break
                    student['name'] = new_name
                    print("Nama siswa berhasil diperbarui!\n")
                    return
                elif update_choice == "nilai":
                    while True:
                        try:
                            new_score = float(input("Masukkan nilai baru: "))
                            break
                        except ValueError:
                            print("Nilai harus berupa angka!")
                    student['score'] = new_score
                    print("Nilai siswa berhasil diperbarui!\n")
                    return
                else:
                    print("Pilihan tidak valid, silakan pilih 'nama' atau 'nilai'.")
    print("Siswa tidak ditemukan.\n")


def delete_student():
    student_id = input("Masukkan ID siswa yang ingin dihapus: ")
    for student in students:
        if student['id'] == student_id:
            students.remove(student)
            print("Data siswa berhasil dihapus!\n")
            return
    print("Siswa tidak ditemukan.\n")


def main_menu():
    while True:
        print("\nMenu Utama:")
        print("1. Tambah Data Siswa")
        print("2. Lihat Data Siswa")
        print("3. Ubah Data Siswa")
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
