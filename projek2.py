# List untuk menyimpan tugas
daftar_tugas = []

# Fungsi tambah tugas
def tambah_tugas():
    tugas = input("Masukkan tugas: ")
    daftar_tugas.append(tugas)
    print("Tugas berhasil ditambahkan!")

# Fungsi melihat tugas
def lihat_tugas():
    if len(daftar_tugas) == 0:
        print("Belum ada tugas.")
    else:
        print("\nDaftar Tugas:")
        for i in range(len(daftar_tugas)):
            print(f"{i+1}. {daftar_tugas[i]}")

# Fungsi hapus tugas
def hapus_tugas():
    lihat_tugas()

    if len(daftar_tugas) > 0:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        daftar_tugas.pop(nomor - 1)
        print("Tugas berhasil dihapus!")
        
# Fungsi statistik
def statistik():
    total = len(daftar_tugas)
    selesai = 0

    for tugas in daftar_tugas:
        if tugas["status"] == "Selesai":
            selesai += 1

    belum = total - selesai

    print("\n=== STATISTIK ===")
    print("Total Tugas          :", total)
    print("Tugas Selesai        :", selesai)
    print("Belum Selesai        :", belum)


# Program utama
while True:
    print("\n=== TO-DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Statistik")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_tugas()

    elif pilihan == "2":
        lihat_tugas()

    elif pilihan == "3":
        hapus_tugas()

    elif pilihan == "4":
        statistik()

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")