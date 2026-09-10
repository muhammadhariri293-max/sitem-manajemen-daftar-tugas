# ==========================================
# SISTEM MANAJEMEN DAFTAR TUGAS (TO-DO LIST)
# ==========================================

tugas_list = []
id_tugas = set()

# Fungsi tambah tugas
def tambah_tugas():
    print("\n=== TAMBAH TUGAS ===")

    while True:
        try:
            idt = int(input("Masukkan ID Tugas: "))
            if idt in id_tugas:
                print("ID sudah digunakan!")
            else:
                break
        except ValueError:
            print("Masukkan angka yang valid!")

    nama = input("Masukkan nama tugas: ")
    prioritas = input("Masukkan prioritas (Tinggi/Sedang/Rendah): ")

    tugas = {
        "id": idt,
        "nama": nama,
        "prioritas": prioritas,
        "status": "Belum Selesai"
    }

    tugas_list.append(tugas)
    id_tugas.add(idt)

    print("Tugas berhasil ditambahkan!")


# Fungsi lihat tugas
def lihat_tugas():
    print("\n=== DAFTAR TUGAS ===")

    if len(tugas_list) == 0:
        print("Belum ada tugas.")
        return

    for tugas in tugas_list:
        print("-" * 40)
        print("ID        :", tugas["id"])
        print("Nama      :", tugas["nama"])
        print("Prioritas :", tugas["prioritas"])
        print("Status    :", tugas["status"])


# Fungsi tandai selesai
def tandai_selesai():
    print("\n=== TANDAI TUGAS SELESAI ===")

    id_cari = int(input("Masukkan ID Tugas: "))

    for tugas in tugas_list:
        if tugas["id"] == id_cari:
            tugas["status"] = "Selesai"
            print("Tugas berhasil diselesaikan!")
            return

    print("Tugas tidak ditemukan!")


# Fungsi hapus tugas
def hapus_tugas():
    print("\n=== HAPUS TUGAS ===")

    id_cari = int(input("Masukkan ID Tugas: "))

    for tugas in tugas_list:
        if tugas["id"] == id_cari:
            tugas_list.remove(tugas)
            id_tugas.remove(id_cari)

            print("Tugas berhasil dihapus!")
            return

    print("Tugas tidak ditemukan!")


# Fungsi cari tugas
def cari_tugas():
    print("\n=== CARI TUGAS ===")

    keyword = input("Masukkan nama tugas: ").lower()

    ditemukan = False

    for tugas in tugas_list:
        if keyword in tugas["nama"].lower():

            info = (
                tugas["id"],
                tugas["nama"],
                tugas["status"]
            )

            print("\nDitemukan:")
            print("ID     :", info[0])
            print("Nama   :", info[1])
            print("Status :", info[2])

            ditemukan = True

    if not ditemukan:
        print("Tugas tidak ditemukan.")


# Fungsi statistik
def statistik():
    total = len(tugas_list)
    selesai = 0

    for tugas in tugas_list:
        if tugas["status"] == "Selesai":
            selesai += 1

    belum = total - selesai

    print("\n=== STATISTIK ===")
    print("Total Tugas          :", total)
    print("Tugas Selesai        :", selesai)
    print("Belum Selesai        :", belum)


# Program utama
while True:

    print("\n")
    print("=" * 45)
    print(" SISTEM MANAJEMEN DAFTAR TUGAS ")
    print("=" * 45)
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Tandai Selesai")
    print("4. Hapus Tugas")
    print("5. Cari Tugas")
    print("6. Statistik")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        tambah_tugas()

    elif pilihan == "2":
        lihat_tugas()

    elif pilihan == "3":
        tandai_selesai()

    elif pilihan == "4":
        hapus_tugas()

    elif pilihan == "5":
        cari_tugas()

    elif pilihan == "6":
        statistik()

    elif pilihan == "7":
        print("\nTerima kasih telah menggunakan program!")
        break

    else:
        print("Pilihan tidak valid!")