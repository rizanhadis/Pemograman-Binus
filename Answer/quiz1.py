import re

def tampilkan_menu():
    print("\nSelamat datang di MysticMix!")
    print("1. Menambah Bahan Ramuan")
    print("2. Menghapus Bahan Ramuan")
    print("3. Meracik Ramuan")
    print("4. Keluar dari MysticMix")

def validasi_bahan(nama):
    return bool(re.fullmatch(r"[a-zA-Z ]+", nama))

def tambah_bahan(bahan):
    nama = input("Masukkan nama bahan ramuan: ").strip()
    if not nama:
        print("Nama bahan tidak boleh kosong!")
    elif not validasi_bahan(nama):
        print("Nama bahan tidak boleh mengandung angka atau simbol!")
    elif nama in bahan:
        print("Bahan sudah terdaftar!")
    else:
        bahan.add(nama)
        print(f"Bahan '{nama}' berhasil ditambahkan!")

def hapus_bahan(bahan):
    if not bahan:
        print("Tidak ada bahan ramuan yang kamu punya.")
        return
    print("Daftar bahan ramuan:")
    for item in bahan:
        print(f"- {item}")
    nama = input("Masukkan nama bahan yang ingin dihapus: ").strip()
    if nama not in bahan:
        print("Bahan tidak ditemukan!")
    else:
        konfirmasi = input(f"Apakah yakin ingin menghapus '{nama}'? (Y/N): ").upper()
        while konfirmasi not in ['Y', 'N']:
            print("Pilihan tidak valid!")
            konfirmasi = input(f"Apakah yakin ingin menghapus '{nama}'? (Y/N): ").upper()
        if konfirmasi == "Y":
            bahan.remove(nama)
            print(f"Bahan '{nama}' berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan.")

def racik_ramuan(bahan):
    if not bahan:
        print("Tidak ada bahan ramuan yang kamu punya.")
        return
    print("Daftar bahan ramuan:")
    for item in bahan:
        print(f"- {item}")
    pilihan = set()
    while True:
        nama = input("Pilih bahan (ketik 'selesai' jika sudah): ").strip()
        if nama.lower() == 'selesai':
            break
        if nama not in bahan:
            print("Bahan tidak ditemukan!")
        elif nama in pilihan:
            print("Bahan sudah dipilih!")
        else:
            pilihan.add(nama)
    if pilihan:
        print(f"Ramuan berhasil diracik dengan bahan: {', '.join(pilihan)}")
    else:
        print("Ramuan gagal diracik.")

def main():
    bahan = set()
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ").strip()
        if pilihan == "1":
            tambah_bahan(bahan)
        elif pilihan == "2":
            hapus_bahan(bahan)
        elif pilihan == "3":
            racik_ramuan(bahan)
        elif pilihan == "4":
            print("Keluar dari MysticMix. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak tersedia.")
        input("Tekan ENTER untuk melanjutkan...")

if __name__ == "__main__":
    main()