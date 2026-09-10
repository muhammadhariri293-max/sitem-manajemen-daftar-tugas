# ==========================================
# SISTEM MANAJEMEN DAFTAR TUGAS
# Program sederhana untuk menambah,
# melihat, menghapus tugas, dan melihat
# statistik jumlah tugas.
# ==========================================

# List untuk menyimpan semua tugas
daftar_tugas = []

# Fungsi untuk menambahkan tugas baru
def tambah_tugas():
    tugas = input("Masukkan tugas: ")  # Meminta pengguna memasukkan nama tugas
    daftar_tugas.append(tugas) # Menambahkan tugas ke dalam list
    print("Tugas berhasil ditambahkan!") # Menampilkan pesan berhasil dalam menambahkan tugas

# Fungsi untuk menampilkan daftar tugas
def lihat_tugas():
    if len(daftar_tugas) == 0:  # Mengecek apakah daftar tugas kosong
        print("Belum ada tugas.")
    else:
        print("\nDaftar Tugas:")
        for i in range(len(daftar_tugas)):  # Menampilkan seluruh tugas sesuai dengan nomor urut
            print(f"{i+1}. {daftar_tugas[i]}")

# Fungsi untuk menghapus tugas
def hapus_tugas():
    lihat_tugas() # Menampilkan daftar tugas terlebih dahulu diambil dari fungsi lihat_tugas() di atas

    if len(daftar_tugas) > 0: # Hanya dijalankan jika ada tugas yang bisa dihapus 

        try:
            nomor = int(input("Masukkan nomor tugas yang ingin dihapus: ")) # Meminta nomor tugas yang ingin dihapus

            if 1 <= nomor <= len(daftar_tugas): # Memastikan nomor yang dimasukkan valid
                                                # Menghapus tugas berdasarkan indeks
                                                # Karena indeks dimulai dari 0,
                                                # maka nomor dikurangi 1
                daftar_tugas.pop(nomor - 1)
                print("Tugas berhasil dihapus!")    
            else:
                print("Nomor tugas tidak valid!")

        except ValueError:   # Menangani kesalahan jika input bukan angka
            print("Masukkan angka yang benar!")

# Fungsi untuk menampilkan statistik tugas
def statistik():
    print("\n=== STATISTIK ===") # Menampilkan jumlah seluruh tugas
    print("Total Tugas :", len(daftar_tugas))

# Program utama
# Perulangan akan terus berjalan sampai
# pengguna memilih menu keluar
while True:
    
    # Menampilkan judul program
    print("=" * 45) 
    print(f"{'SISTEM MANAJEMEN DAFTAR TUGAS':^45}")
    print("=" * 45)
    
    # Menampilkan menu pilihan kepada pengguna
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Statistik")
    print("5. Keluar")

     # Meminta pengguna memilih menu
    pilihan = input("Pilih menu: ")
    
    # Struktur percabangan untuk menentukan
    # fungsi yang akan dijalankan
    if pilihan == "1":   # Memanggil fungsi tambah_tugas
        tambah_tugas()
    elif pilihan == "2":     # Memanggil fungsi lihat_tugas
        lihat_tugas()
    elif pilihan == "3":     # Memanggil fungsi hapus_tugas
        hapus_tugas()
    elif pilihan == "4":     # Memanggil fungsi statistik
        statistik()
    elif pilihan == "5":     # Memanggil fungsi keluar
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak tersedia.")