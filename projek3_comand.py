# ==========================================
# SISTEM MANAJEMEN DAFTAR TUGAS
# Program sederhana untuk menambah,
# melihat, menghapus tugas, dan melihat
# statistik jumlah tugas.
# ==========================================

# List untuk menyimpan semua tugas
daftar_tugas = []


# ==========================================
# Fungsi untuk menambahkan tugas baru
# ==========================================
def tambah_tugas():

    # Meminta pengguna memasukkan nama tugas
    tugas = input("Masukkan tugas: ")

    # Menambahkan tugas ke dalam list
    daftar_tugas.append(tugas)

    # Menampilkan pesan berhasil
    print("Tugas berhasil ditambahkan!")


# ==========================================
# Fungsi untuk menampilkan daftar tugas
# ==========================================
def lihat_tugas():

    # Mengecek apakah daftar tugas kosong
    if len(daftar_tugas) == 0:
        print("Belum ada tugas.")

    else:
        print("\nDaftar Tugas:")

        # Menampilkan seluruh tugas dengan nomor urut
        for i in range(len(daftar_tugas)):
            print(f"{i+1}. {daftar_tugas[i]}")


# ==========================================
# Fungsi untuk menghapus tugas
# ==========================================
def hapus_tugas():

    # Menampilkan daftar tugas terlebih dahulu
    lihat_tugas()

    # Hanya dijalankan jika ada tugas
    if len(daftar_tugas) > 0:

        try:

            # Meminta nomor tugas yang ingin dihapus
            nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))

            # Memastikan nomor yang dimasukkan valid
            if 1 <= nomor <= len(daftar_tugas):

                # Menghapus tugas berdasarkan indeks
                # Karena indeks dimulai dari 0,
                # maka nomor dikurangi 1
                daftar_tugas.pop(nomor - 1)

                print("Tugas berhasil dihapus!")

            else:
                print("Nomor tugas tidak valid!")

        # Menangani kesalahan jika input bukan angka
        except ValueError:
            print("Masukkan angka yang benar!")


# ==========================================
# Fungsi untuk menampilkan statistik tugas
# ==========================================
def statistik():

    print("\n=== STATISTIK ===")

    # Menampilkan jumlah seluruh tugas
    print("Total Tugas :", len(daftar_tugas))


# ==========================================
# PROGRAM UTAMA
# ==========================================
# Perulangan akan terus berjalan sampai
# pengguna memilih menu keluar
# ==========================================
while True:

    # Menampilkan judul program
    print("=" * 45)
    print(f"{'SISTEM MANAJEMEN DAFTAR TUGAS':^45}")
    print("=" * 45)

    # Menampilkan menu
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Statistik")
    print("5. Keluar")

    # Meminta pengguna memilih menu
    pilihan = input("Pilih menu: ")

    # Struktur percabangan untuk menentukan
    # fungsi yang akan dijalankan
    if pilihan == "1":

        # Memanggil fungsi tambah tugas
        tambah_tugas()

    elif pilihan == "2":

        # Memanggil fungsi lihat tugas
        lihat_tugas()

    elif pilihan == "3":

        # Memanggil fungsi hapus tugas
        hapus_tugas()

    elif pilihan == "4":

        # Memanggil fungsi statistik
        statistik()

    elif pilihan == "5":

        # Mengakhiri program
        print("Program selesai.")
        break

    else:

        # Jika pilihan tidak tersedia
        print("Pilihan tidak tersedia.")