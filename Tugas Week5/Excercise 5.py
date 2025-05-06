
#nomor 1
# n = int(input("Jumlah mahasiswa: "))
# data = []

# for _ in range(n):
#     nama = input("Nama: ").strip()
#     nim = input("NIM: ").strip()
#     kelas = input("Kelas: ").strip()
#     data.append(f"{nama}-{nim}-{kelas}")

# with open("dataMahasiswa.txt", "w") as file:
#     file.write("\n".join(data))




# nomor 2
# max_score = -1
# max_nama = ""
# max_hari = ""
# with open("/Users/huanxin/Pemograman Binus/Answer/scores.txt", "r") as file:
#     for line in file:
#         line = line.strip()
#         if line:
#             parts = line.split('#')
#             if len(parts) != 3:
#                 continue  # Lewati baris tidak valid
#             nama, hari, score_str = parts
#             try:
#                 score = int(score_str)
#             except ValueError:
#                 continue  
#             if score > max_score:
#                 max_score = score
#                 max_nama = nama
#                 max_hari = hari

# print(f"Nama: {max_nama}")
# print(f"Hari: {max_hari}")
# print(f"Score: {max_score}")


#nomor 3
total = 0
counter_line = 0
try:
    with open("/Users/huanxin/Pemograman Binus/Answer/numbers.txt", "r") as file:
        for line in file:
            counter_line += 1
            stripped_line = line.strip()
            
            if not stripped_line:
                continue  # Lewati baris kosong
            
            try:
                num = int(stripped_line)
                total += num
                print(f"Number: {num}")
            except ValueError:
                print(f"Peringatan: baris {counter_line} bukan integer, dilewati.")
except FileNotFoundError:
    print("File numbers.txt tidak ditemukan.")
else:
    print(f"Total: {total}")
    
    