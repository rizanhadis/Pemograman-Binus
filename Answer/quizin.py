# # import re

# # def tampilkan_menu():
# #     print("\nSelamat datang di MysticMix!")
# #     print("1. Menambah Bahan Ramuan")
#     print("2. Menghapus Bahan Ramuan")
#     print("3. Meracik Ramuan")
#     print("4. Keluar dari MysticMix")

# def validasi_bahan(nama):
#     return bool(re.fullmatch(r"^[a-zA-Z ]+$", nama))

# def tambah_bahan(bahan):
#     nama = input("Masukkan nama bahan ramuan: ").strip()
#     if not nama:
#         print("Nama bahan ramuan tidak boleh kosong!")
#     elif not validasi_bahan(nama):
#         print("Nama bahan ramuan tidak boleh mengandung simbol dan angka!")
#     elif nama in bahan:
#         print(f"Bahan '{nama}' sudah ada.")
#     else:
#         bahan.append(nama)
#         print(f"Bahan '{nama}' berhasil ditambahkan!")

# def hapus_bahan(bahan):
#     if not bahan:
#         print("Tidak ada bahan ramuan yang kamu punya.")
#         return
    
#     print("List bahan ramuan:")
#     for item in bahan:
#         print(f"> {item}")
    
#     nama = input("\nMasukkan bahan ramuan yang ingin dihapus: ").strip()
#     if nama not in bahan:
#         print(f"Mohon maaf, bahan '{nama}' tidak ditemukan!")
#     else:
#         while True:
#             konfirmasi = input(f"Apakah kamu yakin ingin menghapus '{nama}'? (Y/N): ")
#             if konfirmasi == "Y":
#                 bahan.remove(nama)
#                 print(f"Bahan '{nama}' berhasil dihapus!")
#                 break
#             elif konfirmasi == "N":
#                 print(f"Bahan '{nama}' tidak jadi untuk dihapus.")
#                 break
#             else:
#                 print("Mohon maaf, Pilihan tidak valid! Harap masukkan Y atau N.")

# def racik_ramuan(bahan):
#     if not bahan:
#         print("Tidak ada bahan ramuan yang kamu punya.")
#         return
    
#     print("\List bahan ramuan:")
#     for item in bahan:
#         print(f"> {item}")
    
#     pilihan = []
#     while True:
#         nama = input("\nPilih bahan (ketik 'selesai' jika sudah): ").strip()
#         if nama.lower() == "selesai":
#             break
#         if nama not in bahan:
#             print(f"Bahan '{nama}' tidak ditemukan!")
#         elif nama in pilihan:
#             print(f"Bahan '{nama}' sudah dipilih!")
#         else:
#             pilihan.append(nama)
    
#     if pilihan:
#         print("\nMeracik ramuan dengan bahan:")
#         for item in pilihan:
#             print(f"> {item}")
#         print("Ramuan berhasil diracik!")
#     else:
#         print("Ramuan gagal diracik.")

# def main():
#     bahan = []
#     while True:
#         tampilkan_menu()
#         pilihan = input("\nPilih menu (1-4): ").strip()
#         if pilihan == "1":
#             tambah_bahan(bahan)
#         elif pilihan == "2":
#             hapus_bahan(bahan)
#         elif pilihan == "3":
#             racik_ramuan(bahan)
#         elif pilihan == "4":
#             print("\nHave a nice day yaaa :),")
#             break
#         else:
#             print("Mohon maaf, pilihan tidak tersedia.")
#         input("\nKlik ENTER untuk melanjutkan...")

# if __name__ == "__main__":
#     main(dsd







jam = int(input("jumlah jam="))
menit = jam 